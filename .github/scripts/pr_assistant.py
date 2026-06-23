#!/usr/bin/env python3
"""
Responds to PR comments using Claude.
Answers questions or applies requested changes directly to the PR branch.
Run by the claude-assistant.yml workflow.
"""
import os
import re
import json
import subprocess
import urllib.request
from pathlib import Path
import anthropic


def gh_api(method, path, token, data=None):
    url = f"https://api.github.com{path}"
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(
        url, data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        method=method,
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def post_or_update_comment(body, pr, repo, token):
    marker = "<!-- claude-bot -->"
    full_body = f"{marker}\n{body}"
    comments = gh_api("GET", f"/repos/{repo}/issues/{pr}/comments", token)
    existing = next((c for c in comments if marker in c.get("body", "")), None)
    if existing:
        gh_api("PATCH", f"/repos/{repo}/issues/comments/{existing['id']}", token, {"body": full_body})
    else:
        gh_api("POST", f"/repos/{repo}/issues/{pr}/comments", token, {"body": full_body})


def git(*args):
    result = subprocess.run(["git"] + list(args), capture_output=True, text=True)
    return result.returncode == 0, result.stdout, result.stderr


def commit_and_push(author):
    git("config", "user.name", "github-actions[bot]")
    git("config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
    git("add", "index.html", "content.md")
    changed = subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode != 0
    if changed:
        git("commit", "-m", f"fix: apply change requested by @{author} [skip-claude]")
        git("push")
    return changed


def main():
    comment_body = os.environ["COMMENT_BODY"]
    author = os.environ["COMMENT_AUTHOR"]
    pr = os.environ["PR_NUMBER"]
    token = os.environ["GH_TOKEN"]
    repo = os.environ["REPO"]

    # Prevent bot loops
    if author == "github-actions[bot]" or "[skip-claude]" in comment_body:
        print("Bot comment — skipping.")
        return

    current_html = Path("index.html").read_text(encoding="utf-8")
    current_content = Path("content.md").read_text(encoding="utf-8")

    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8192,
        system="""You are an assistant helping maintain the Contrivation Labs company website.
You respond to comments left on GitHub Pull Requests.

You have access to both the content.md file (plain-text source) and the index.html file.

When the comment is a QUESTION: answer it clearly and concisely.

When the comment is a CHANGE REQUEST: apply the change. Update BOTH content.md and index.html
so they stay in sync. Return your response in this exact format:

REPLY: [1-2 sentence summary of what you changed]

UPDATED_CONTENT:
[complete updated content.md]

UPDATED_HTML:
[complete updated index.html]

For questions only:
REPLY: [your answer]

Preserve all HTML structure, CSS classes, and attributes. Never remove sections.""",
        messages=[{
            "role": "user",
            "content": f"""PR comment from @{author}: "{comment_body}"

Current content.md:
{current_content}

Current index.html:
{current_html}"""
        }]
    )

    text = response.content[0].text.strip()

    if "UPDATED_HTML:" in text:
        # Parse out the reply and updated files
        reply_match = re.search(r"REPLY:\s*(.*?)(?=UPDATED_CONTENT:|UPDATED_HTML:|$)", text, re.DOTALL)
        content_match = re.search(r"UPDATED_CONTENT:\s*(.*?)(?=UPDATED_HTML:|$)", text, re.DOTALL)
        html_match = re.search(r"UPDATED_HTML:\s*(.*?)$", text, re.DOTALL)

        reply = reply_match.group(1).strip() if reply_match else "Done."

        if content_match:
            new_content = content_match.group(1).strip()
            Path("content.md").write_text(new_content, encoding="utf-8")

        if html_match:
            new_html = html_match.group(1).strip()
            new_html = re.sub(r"^```html\s*", "", new_html)
            new_html = re.sub(r"\s*```$", "", new_html)
            Path("index.html").write_text(new_html, encoding="utf-8")

        committed = commit_and_push(author)
        if committed:
            comment = f"🤖 {reply}\n\nThe preview link in this PR will refresh in ~60 seconds."
        else:
            comment = f"🤖 {reply}\n\n_(No changes were needed.)_"
    else:
        reply = re.sub(r"^REPLY:\s*", "", text).strip()
        comment = f"🤖 {reply}"

    post_or_update_comment(comment, pr, repo, token)
    print("Done.")


if __name__ == "__main__":
    main()
