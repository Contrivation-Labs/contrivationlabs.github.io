# Contrivation Labs — Company Website

**Live site:** [contrivation-labs.github.io/contrivationlabs.github.io](https://contrivation-labs.github.io/contrivationlabs.github.io/)
**Repository:** [github.com/Contrivation-Labs/contrivationlabs.github.io](https://github.com/Contrivation-Labs/contrivationlabs.github.io)

> **No coding or terminal experience needed.** Edit one plain-text file on GitHub, commit, and the rest is automatic — preview, review, and publish.

---

## Table of Contents

1. [How It Works](#how-it-works)
2. [File Structure](#file-structure)
3. [Edit Website Content](#edit-website-content)
4. [Section-by-Section Guide](#section-by-section-guide)
   - [Hero (Banner)](#hero-banner)
   - [About](#about)
   - [Awards & Grants](#awards--grants)
   - [Products](#products)
   - [Contact](#contact)
5. [Add a New Product](#add-a-new-product)
6. [Add a New Award](#add-a-new-award)
7. [Replace or Add Images & Videos](#replace-or-add-images--videos)
8. [Change Colours or Layout](#change-colours-or-layout)
9. [Review, Chat & Publish (no terminal)](#review-chat--publish-no-terminal)
10. [One-Time Setup](#one-time-setup)
11. [Help & Resources](#help--resources)

---

## How It Works

```
You edit content.md on GitHub and click Commit
              ↓
Claude reads your changes and updates the website HTML
              ↓
A Pull Request opens automatically (~2 min)
              ↓
A preview link is posted as a comment on the PR
              ↓
You (or anyone) can leave comments — Claude will make fixes
              ↓
Click Merge → live site updates ✅
```

**You never need to touch HTML.** All content lives in one plain-text file: `content.md`.

---

## File Structure

| File | Link | What it controls |
|------|------|-----------------|
| `content.md` ⭐ | [Open on GitHub](https://github.com/Contrivation-Labs/contrivationlabs.github.io/blob/main/content.md) | **All website text** — edit this to update the site |
| `styles.css` | [Open on GitHub](https://github.com/Contrivation-Labs/contrivationlabs.github.io/blob/main/styles.css) | Colours, fonts, spacing, layout |
| `index.html` | [Open on GitHub](https://github.com/Contrivation-Labs/contrivationlabs.github.io/blob/main/index.html) | Generated automatically — do not edit directly |
| `media/` | [Open on GitHub](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media) | All images and videos |

```
contrivationlabs.github.io/
│
├── content.md  ⭐               ← EDIT THIS to update website text
├── index.html                   ← auto-generated, do not edit
├── styles.css                   ← colours and layout only
│
└── media/
    ├── Logo_Contrivation Labs.JPG
    ├── calyxtract_logo.png
    ├── Calyxtract-productpic1.JPG
    ├── Calyxtract-productpic2.JPG
    ├── birac.png
    ├── startup_karnataka.png
    └── pusa_krishi.png
```

---

## Edit Website Content

All visible text on the site is controlled by [`content.md`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/blob/main/content.md).

### Steps

1. Open [`content.md`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/content.md) on GitHub (link opens the editor)
2. Find the section you want to update — sections are labelled `## [HERO]`, `## [ABOUT]`, etc.
3. Change the text to the right of the colon (e.g. `tagline: your new tagline here`)
4. Click **Commit changes** → leave the branch as `main` → click **Commit changes** again
5. A Pull Request opens in ~2 minutes with a live preview link

> **What are the `#` lines?** Lines starting with `#` are notes/instructions for editors — they are ignored by the system. Only lines with `key: value` pairs update the site.

---

## Section-by-Section Guide

### Hero (Banner)

**In `content.md`, find:** `## [HERO]`

| Key | What it changes |
|-----|----------------|
| `tagline` | The large heading text |
| `subtext` | The paragraph below the heading |
| `button_primary` | The red "View Products" button label |
| `button_secondary` | The outline "Get in Touch" button label |

---

### About

**In `content.md`, find:** `## [ABOUT]`

| Key | What it changes |
|-----|----------------|
| `description_1`, `_2`, `_3` | The three company description paragraphs |
| `stat_1_value` … `stat_4_value` | The large numbers in the four stat cards |
| `stat_1_label` … `stat_4_label` | The caption below each stat number |
| `vision` | The dark banner vision statement |

---

### Awards & Grants

**In `content.md`, find:** `## [AWARDS]`

Each `### Award N` block is one card on the site.

| Key | What it changes |
|-----|----------------|
| `image` | The award logo (must match a filename in `media/`) |
| `description` | The text below the logo |
| `amount` | The grant amount shown in red |

---

### Products

**In `content.md`, find:** `## [PRODUCT 1]`

| Key | What it changes |
|-----|----------------|
| `logo` | Product logo image |
| `name` | Product name (e.g. CalyXtract®) |
| `subtitle` | One-line description under the name |
| `photo_1`, `photo_2` | The two product photos |
| `description` | Full product description paragraph |
| `benefit_N_title` | Title of benefit tile N |
| `benefit_N_text` | Description of benefit tile N |
| `saving_1`, `saving_2` | The green/red savings pills |

---

### Contact

**In `content.md`, find:** `## [CONTACT]`

| Key | What it changes |
|-----|----------------|
| `location` | City, state, country |
| `email` | Contact email address |
| `phone` | Phone number |

> **Contact form:** Sign up at [formspree.io](https://formspree.io), create a form, then leave a comment on any PR asking Claude to update the form ID — it will do it for you.

---

## Add a New Product

1. Open [`content.md`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/content.md)
2. Copy the entire `## [PRODUCT 1]` block
3. Paste it below and rename the header to `## [PRODUCT 2]`
4. Fill in the new product's details
5. Upload the product images to [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media)
6. Commit `content.md` — the PR and preview will be created automatically

---

## Add a New Award

1. Open [`content.md`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/content.md)
2. Find `## [AWARDS]` and copy any existing `### Award N` block
3. Paste it below the last award and increment the number (e.g. `### Award 4`)
4. Fill in the image, description, and amount
5. Upload the award logo to [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media)
6. Commit `content.md`

---

## Replace or Add Images & Videos

Images are stored in [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media). The filenames in `content.md` must match exactly.

### Recommended formats and sizes

| Use | Format | Max size |
|-----|--------|----------|
| Company / product logos | PNG | 500 px wide |
| Product photos | JPG | 1200 × 900 px |
| Award badges | PNG | 400 × 400 px |
| Demo video | MP4 (H.264) | 50 MB |

> Compress images before uploading at [squoosh.app](https://squoosh.app) to keep the site fast.

### Replace an existing image

1. Rename your new image to **exactly match** the old filename (e.g. `Calyxtract-productpic1.JPG`)
2. Go to [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media) → **Add file → Upload files**
3. Drop in your file → **Commit changes** (GitHub overwrites the old one automatically)

### Add a new image

1. Upload to [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media)
2. Note the exact filename (no spaces — use hyphens instead)
3. Reference it in `content.md` as `image: media/your-filename.png`

---

## Change Colours or Layout

This is the only case where you edit `styles.css` instead of `content.md`.

Open [`styles.css`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/styles.css), find the `:root` block near the top, and change any hex value:

```css
:root {
  --blue:       #1565C0;   /* Primary blue  — navbar, buttons         */
  --blue-light: #2196F3;   /* Accent blue   — borders, highlights      */
  --blue-pale:  #E3F2FD;   /* Pale blue     — section backgrounds      */
  --green:      #2E7D32;   /* Green         — savings pills            */
  --red:        #C62828;   /* Red           — CTA buttons, amounts     */
  --dark:       #1A237E;   /* Dark navy     — hero bg, footer          */
  --text:       #212121;   /* Body text                                */
  --muted:      #555555;   /* Secondary text                           */
  --white:      #ffffff;   /* Card backgrounds                         */
}
```

Use [Google's colour picker](https://www.google.com/search?q=color+picker) to find hex codes.

> Editing `styles.css` directly deploys to the live site — no PR is created. Double-check your change before committing.

---

## Review, Chat & Publish (no terminal)

When you commit a change to `content.md`, a Pull Request is created automatically. Here is what to do with it:

### 1 — Check the preview

- Wait ~60 seconds after committing
- A bot will post a comment on the PR with a **preview link**
- Click the link to browse the full site before it goes live

### 2 — Request changes via comment

- If something looks wrong, **leave a comment** on the PR describing the fix
- Claude will read your comment, update the site, and the preview will refresh in ~60 seconds
- Examples of things you can ask:
  - *"The product description on the second paragraph should say X instead of Y"*
  - *"Can you make the vision statement shorter?"*
  - *"The award amount for BIRAC should be INR 6 Mn"*

### 3 — Publish

- When you're happy with the preview, click **Merge pull request**
- The live site updates within ~60 seconds

---

## One-Time Setup

> ⚠️ This only needs to be done **once** by someone with admin access to the repo.

The automated preview system requires GitHub Pages to serve from the `gh-pages` branch instead of `main`.

**Steps:**
1. Push all the new files to GitHub (if not done already)
2. Go to the repo → **Settings → Pages**
3. Under **Source**, change to: `Deploy from a branch` → branch: `gh-pages` → folder: `/ (root)`
4. Click **Save**
5. Make any small edit to `index.html` or `styles.css` on `main` — this triggers the first production deploy and creates the `gh-pages` branch
6. Previews will work on all future PRs automatically

You also need one GitHub Secret (may already be set):
- **Settings → Secrets and variables → Actions → New repository secret**
- Name: `ANTHROPIC_API_KEY` | Value: your Anthropic API key

---

## Help & Resources

| I need to… | Link |
|------------|------|
| Edit website content | [Edit content.md](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/content.md) |
| Upload images or videos | [media/ folder](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media) |
| Edit colours / layout | [Edit styles.css](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/styles.css) |
| See open Pull Requests | [Pull Requests tab](https://github.com/Contrivation-Labs/contrivationlabs.github.io/pulls) |
| Check deployment status | [Actions tab](https://github.com/Contrivation-Labs/contrivationlabs.github.io/actions) |
| Set up contact form | [Formspree](https://formspree.io) |
| Pick a colour hex code | [Google colour picker](https://www.google.com/search?q=color+picker) |
| Compress images | [Squoosh](https://squoosh.app) |
| GitHub Pages docs | [docs.github.com/pages](https://docs.github.com/en/pages) |
| GitHub support | [support.github.com](https://support.github.com) |
| AI assistant for changes | [Claude Code session](https://claude.ai/code/session_01UV9AYgpT46qTgkMJz5jMqJ) |

---

## Quick Reference

| I want to… | What to do |
|------------|-----------|
| Update any text on the site | Edit [`content.md`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/content.md) and commit |
| Add or change a product photo | Upload to [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media), update filename in `content.md` |
| Add a new award | Add a `### Award N` block in `content.md` |
| Add a new product | Add a `## [PRODUCT N]` block in `content.md` |
| Change a colour | Edit the `:root` block in [`styles.css`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/styles.css) |
| Fix something in a PR | Leave a comment on the PR — Claude will handle it |
| Publish changes | Merge the Pull Request |
