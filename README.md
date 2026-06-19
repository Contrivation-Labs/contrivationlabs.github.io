# Contrivation Labs — Company Website

**Live site:** [contrivation-labs.github.io/contrivationlabs.github.io](https://contrivation-labs.github.io/contrivationlabs.github.io/)
**Repository:** [github.com/Contrivation-Labs/contrivationlabs.github.io](https://github.com/Contrivation-Labs/contrivationlabs.github.io)

> **No coding or terminal experience needed.** Every change is made through the GitHub website. Once saved, the live site updates automatically within ~60 seconds.

---

## Table of Contents

1. [File Structure](#file-structure)
2. [Edit Website Text](#edit-website-text)
3. [Replace or Add Images & Videos](#replace-or-add-images--videos)
4. [Section-by-Section Guide](#section-by-section-guide)
   - [Hero (Banner)](#hero-banner)
   - [About](#about)
   - [Awards & Grants](#awards--grants)
   - [Products](#products)
   - [Contact](#contact)
5. [Add a New Product](#add-a-new-product)
6. [Add a New Award](#add-a-new-award)
7. [Change Colours or Layout](#change-colours-or-layout)
8. [Commit & Deploy (no terminal)](#commit--deploy-no-terminal)
9. [Help & Resources](#help--resources)

---

## File Structure

| File | Direct link | What it controls |
|------|-------------|------------------|
| `index.html` | [Open on GitHub](https://github.com/Contrivation-Labs/contrivationlabs.github.io/blob/main/index.html) | All visible text, sections, buttons, and links |
| `styles.css` | [Open on GitHub](https://github.com/Contrivation-Labs/contrivationlabs.github.io/blob/main/styles.css) | All colours, fonts, spacing, and layout |
| `media/` | [Open on GitHub](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media) | All images and videos displayed on the site |

```
contrivationlabs.github.io/
│
├── index.html                        ← text, sections, links
├── styles.css                        ← colours, fonts, layout
│
└── media/
    ├── Logo_Contrivation Labs.JPG    ← company logo (nav + footer)
    ├── calyxtract_logo.png           ← CalyXtract product logo
    ├── Calyxtract-productpic1.JPG    ← product photo 1
    ├── Calyxtract-productpic2.JPG    ← product photo 2
    ├── birac.png                     ← BIRAC award badge
    ├── startup_karnataka.png         ← Startup Karnataka award badge
    └── pusa_krishi.png               ← Pusa Krishi award badge
```

**Rule of thumb:**
- Change **words or links** → edit `index.html`
- Change **colours, fonts, or spacing** → edit `styles.css`
- Add or replace **images/videos** → upload to `media/`

---

## Edit Website Text

All visible text on the site lives in [`index.html`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/blob/main/index.html).

1. Click the link above to open the file on GitHub
2. Click the **pencil icon** (✏️ Edit this file) in the top-right of the file view
3. Press **Ctrl+F** to open browser search and find the text you want to change
4. Make your edits
5. Click **Commit changes** (see [Commit & Deploy](#commit--deploy-no-terminal))

> **What are HTML tags?** Text on the page sits between angle-bracket tags, for example:
> `<p>This is a paragraph.</p>` or `<h1>This is a heading.</h1>`
> Only edit the words between the tags. Leave the tags themselves (`<p>`, `</p>`, etc.) untouched.

---

## Replace or Add Images & Videos

All media files live in the [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media) folder.

### Recommended formats and sizes

| Use | Format | Recommended size |
|-----|--------|-----------------|
| Company / product logos | PNG (transparent background preferred) | Max 500 px wide |
| Product photos | JPG | Max 1200 × 900 px |
| Award badges | PNG | Max 400 × 400 px |
| Demo video | MP4 (H.264) | Max 50 MB |

> Compress images before uploading at [squoosh.app](https://squoosh.app) to keep the site fast.

### Replace an existing image

1. Rename your new image to **exactly match** the filename it replaces (e.g. `Calyxtract-productpic1.JPG`)
2. Open [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media) on GitHub
3. Click **Add file → Upload files**
4. Drop in your file — GitHub overwrites the old one automatically when names match
5. Click **Commit changes**

### Add a new image

1. Upload the file to [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media)
2. Note the exact filename (e.g. `new-product-photo.JPG`)
3. Reference it in `index.html` as `src="media/new-product-photo.JPG"`

> **Naming rule:** No spaces in filenames. Use hyphens or underscores (e.g. `field-photo-2.jpg` not `field photo 2.jpg`).

### Embed a video

Upload the `.mp4` to `media/`, then add this block in `index.html` where you want the video to appear:

```html
<video controls width="100%">
  <source src="media/your-video.mp4" type="video/mp4" />
</video>
```

---

## Section-by-Section Guide

### Hero (Banner)

The full-width banner at the top of the page.

**Search for in `index.html`:** `<!-- HERO -->`

| What to change | What to find and edit |
|----------------|-----------------------|
| Main heading | Text inside `<h1>…</h1>` |
| Subtitle paragraph | `<p>` immediately below the `<h1>` |
| "View Products" button | Text inside `<a class="btn btn-primary">` |
| "Get in Touch" button | Text inside `<a class="btn btn-outline">` |

---

### About

Company description paragraphs, the four stat cards, and the vision statement banner.

**Search for in `index.html`:** `<!-- ABOUT -->`

| What to change | What to find and edit |
|----------------|-----------------------|
| Company description | Paragraphs inside `<div class="about-text">` |
| Stat card numbers | Text inside `<div class="stat-num">` |
| Stat card labels | `<p>` directly below each `<div class="stat-num">` |
| Vision statement | Text inside `<div class="vision-box">` |

---

### Awards & Grants

Three side-by-side award cards, each with a logo image, description, and grant amount.

**Search for in `index.html`:** `<!-- AWARDS -->`

Each card follows this pattern:
```html
<div class="award-card">
  <img src="media/birac.png" alt="BIRAC grant" />
  <p>Grant recipient under <strong>BIRAC</strong> — Ignite Innovate Incubate</p>
  <span class="award-amount">INR 5 Mn</span>
</div>
```

| What to change | What to find and edit |
|----------------|-----------------------|
| Award logo | Replace the image in `media/` or update `src="media/…"` |
| Description text | Text inside `<p>` |
| Grant amount | Text inside `<span class="award-amount">` |

---

### Products

The CalyXtract® product card: logo, two photos, description text, four benefit tiles, and savings pills.

**Search for in `index.html`:** `<!-- CATALOG -->`

| What to change | What to find and edit |
|----------------|-----------------------|
| Product logo | Replace `media/calyxtract_logo.png` in `media/` |
| Product name | `<h3>` inside `.product-header` |
| Product subtitle | `<p>` inside `.product-header` |
| Product photos | Replace `Calyxtract-productpic1.JPG` / `Calyxtract-productpic2.JPG` in `media/` |
| Product description | Text inside `<p class="product-desc">` |
| Benefit tile title | `<h4>` inside each `<div class="benefit">` |
| Benefit tile text | `<p>` inside each `<div class="benefit">` |
| Savings pills | Text inside each `<span class="saving-pill">` |

---

### Contact

Location, email, phone, social media buttons, and the enquiry form.

**Search for in `index.html`:** `<!-- CONTACT -->`

| What to change | What to find and edit |
|----------------|-----------------------|
| Email address | Update both `href="mailto:…"` and the visible link text |
| Phone number | Replace `+91 – XXXXX XXXXX` |
| Location | Text inside the Location `<span>` |
| Contact form | Sign up at [formspree.io](https://formspree.io), create a form, replace `YOUR_FORM_ID` in `action="https://formspree.io/f/YOUR_FORM_ID"` |

---

## Add a New Product

1. Open [`index.html`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/index.html) (link opens the editor directly)
2. Press **Ctrl+F** and search for `<!-- CATALOG -->`
3. Scroll to the closing `</section>` tag of the catalog section
4. Paste the template below just before `</section>` and fill in your details:

```html
<div class="product-card" style="margin-top: 2rem;">
  <div class="product-header">
    <img src="media/YOUR-PRODUCT-LOGO.png" alt="Product logo" />
    <div>
      <h3>Product Name</h3>
      <p>One-line description of the product</p>
    </div>
  </div>
  <div class="product-body">
    <div class="product-images">
      <img src="media/product-photo-1.JPG" alt="Product photo 1" />
      <img src="media/product-photo-2.JPG" alt="Product photo 2" />
    </div>
    <p class="product-desc">
      Full product description goes here.
    </p>
    <div class="benefits">
      <div class="benefit">
        <div class="benefit-icon">&#9881;</div>
        <div>
          <h4>Benefit Title</h4>
          <p>Short description of this benefit.</p>
        </div>
      </div>
      <!-- Copy the block above to add more benefit tiles -->
    </div>
  </div>
</div>
```

5. Upload the product logo and photos to [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media)
6. Commit the changes

---

## Add a New Award

1. Open [`index.html`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/index.html)
2. Press **Ctrl+F** and search for `<!-- AWARDS -->`
3. Inside `<div class="awards-grid">`, paste a new card before the closing `</div>`:

```html
<div class="award-card">
  <img src="media/YOUR-AWARD-LOGO.png" alt="Award name" />
  <p>Short description of the award or grant</p>
  <span class="award-amount">INR X Mn</span>
</div>
```

4. Upload the award logo to [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media)
5. Commit the changes

---

## Change Colours or Layout

All colours are defined as variables near the top of [`styles.css`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/styles.css) (link opens the editor).

Find this block and change any hex value to update that colour everywhere on the site:

```css
:root {
  --blue:       #1565C0;   /* Primary blue  — navbar, primary buttons       */
  --blue-light: #2196F3;   /* Accent blue   — borders, hover highlights      */
  --blue-pale:  #E3F2FD;   /* Pale blue     — About, Awards section bg       */
  --green:      #2E7D32;   /* Green         — savings pills                  */
  --red:        #C62828;   /* Red           — CTA buttons, grant amounts     */
  --dark:       #1A237E;   /* Dark navy     — hero bg, footer bg, headings   */
  --text:       #212121;   /* Dark grey     — body text                      */
  --muted:      #555555;   /* Mid grey      — secondary / caption text       */
  --white:      #ffffff;   /* White         — card backgrounds                */
}
```

Use [Google's colour picker](https://www.google.com/search?q=color+picker) or [coolors.co](https://coolors.co) to find hex codes for any colour.

---

## Commit & Deploy (no terminal)

### Editing a file (text or CSS)

1. Open the file on GitHub — use the direct editor links in [File Structure](#file-structure)
2. Make your changes in the editor
3. Click **Commit changes** (green button, top-right)
4. In the dialog: add an optional description → leave **"Commit directly to main"** selected → click **Commit changes**

### Uploading files (images, videos)

1. Go to [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media)
2. Click **Add file → Upload files**
3. Drag and drop your files, or click to browse
4. Scroll down → click **Commit changes**

### Checking the deployment

After committing, the site rebuilds automatically. To confirm it's live:

```
You commit a change
        ↓
GitHub Pages detects the push (~5 sec)
        ↓
Site rebuilds automatically (~30–60 sec)
        ↓
Live site updates ✅
```

1. Go to the [Actions tab](https://github.com/Contrivation-Labs/contrivationlabs.github.io/actions)
2. Wait for the **"pages build and deployment"** workflow to show a green ✅
3. Visit the [live site](https://contrivation-labs.github.io/contrivationlabs.github.io/) to verify

---

## Help & Resources

| I need to… | Link |
|------------|------|
| Edit page text | [Edit index.html](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/index.html) |
| Edit colours/layout | [Edit styles.css](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/styles.css) |
| Upload images or videos | [media/ folder](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media) |
| Check if my changes went live | [Actions tab](https://github.com/Contrivation-Labs/contrivationlabs.github.io/actions) |
| Set up the contact form | [Formspree](https://formspree.io) |
| Pick a colour hex code | [Google colour picker](https://www.google.com/search?q=color+picker) |
| Compress images before upload | [Squoosh](https://squoosh.app) |
| Learn HTML basics | [MDN HTML guide](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML) |
| Learn about GitHub Pages | [GitHub Pages docs](https://docs.github.com/en/pages) |
| How to edit files on GitHub | [GitHub editing docs](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files) |
| GitHub support | [GitHub Support](https://support.github.com) |
| AI assistant for changes | [Claude Code session](https://claude.ai/code/session_01UV9AYgpT46qTgkMJz5jMqJ) |

---

## Quick Reference

| I want to… | Edit this |
|------------|-----------|
| Change any text on the page | [`index.html`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/index.html) |
| Update the company logo | Replace `Logo_Contrivation Labs.JPG` in [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media) |
| Add or swap a product photo | Replace or upload in [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media) |
| Change a colour site-wide | [`styles.css`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/styles.css) — update the value in `:root` |
| Update contact email or phone | [`index.html`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/index.html) — search `TODO` |
| Add a new product | [`index.html`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/index.html) — see [Add a New Product](#add-a-new-product) |
| Add a new award | [`index.html`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/index.html) — see [Add a New Award](#add-a-new-award) |
