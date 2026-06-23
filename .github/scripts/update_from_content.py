#!/usr/bin/env python3
"""
Reads content.md and uses Claude to update index.html accordingly.
Run by the content-to-site.yml workflow.
"""
import re
from pathlib import Path
import anthropic


def parse_content(text):
    """Strip comment lines, then return the cleaned content string."""
    lines = [l for l in text.splitlines() if not l.strip().startswith("#")]
    return "\n".join(lines).strip()


def call_claude(content_md: str, current_html: str) -> str:
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8192,
        system="""You update a company website's index.html based on a plain-text content file.

The content file uses sections like ## [HERO], ## [ABOUT], ## [AWARDS], ## [PRODUCT 1], ## [CONTACT].
Each section has key: value pairs that map to the website content.

The HTML has matching section markers: <!-- HERO -->, <!-- ABOUT -->, <!-- AWARDS -->, <!-- CATALOG -->, <!-- CONTACT -->.

Rules:
- Update ONLY the text content indicated by the content file
- Preserve ALL HTML tags, CSS classes, attributes, and structure exactly
- For products: [PRODUCT 1] maps to the first .product-card, [PRODUCT 2] would add a second, etc.
- For awards: each ### Award block maps to one .award-card in order
- image/photo/logo values are file paths — use them as-is in src attributes
- Return ONLY the raw HTML — no markdown fences, no explanation, no commentary""",
        messages=[{
            "role": "user",
            "content": f"""Content file (content.md):
{content_md}

Current index.html:
{current_html}

Return the complete updated index.html:"""
        }]
    )

    html = response.content[0].text.strip()
    # Strip markdown code fences if Claude added them
    html = re.sub(r"^```html\s*", "", html)
    html = re.sub(r"\s*```$", "", html)
    return html


def main():
    content_raw = Path("content.md").read_text(encoding="utf-8")
    content_md = parse_content(content_raw)

    current_html = Path("index.html").read_text(encoding="utf-8")

    print("Calling Claude to update index.html...")
    updated_html = call_claude(content_md, current_html)

    Path("index.html").write_text(updated_html, encoding="utf-8")
    print("index.html updated successfully.")


if __name__ == "__main__":
    main()
