# Contrivation Labs — Company Website

**Live site:** [contrivation-labs.github.io/contrivationlabs.github.io](https://contrivation-labs.github.io/contrivationlabs.github.io/)
**Repository:** [github.com/Contrivation-Labs/contrivationlabs.github.io](https://github.com/Contrivation-Labs/contrivationlabs.github.io)

> Every change you commit to the `main` branch goes live automatically within ~60 seconds. No terminal or technical setup needed.

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

```
contrivationlabs.github.io/
│
├── index.html      ← All page content and structure (text, sections, links)
├── styles.css      ← All visual styling (colours, fonts, spacing, layout)
│
└── media/          ← All images and videos used on the site
    ├── Logo_Contrivation Labs.JPG
    ├── calyxtract_logo.png
    ├── Calyxtract-productpic1.JPG
    ├── Calyxtract-productpic2.JPG
    ├── birac.png
    ├── startup_karnataka.png
    └── pusa_krishi.png
```

**Rule of thumb:**
- Change **words or links** → edit [`index.html`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/blob/main/index.html)
- Change **colours, fonts, or spacing** → edit [`styles.css`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/blob/main/styles.css)
- Add or replace **images/videos** → upload to [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media)

---

## Edit Website Text

All visible text on the site lives in [`index.html`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/blob/main/index.html).

1. Open the file on GitHub using the link above
2. Click the **pencil icon** (✏️ Edit this file) in the top-right of the file view
3. Find the text you want to change using **Ctrl+F** (browser find)
4. Make your edits
5. Follow the [Commit & Deploy](#commit--deploy-no-terminal) steps at the bottom

> **Tip:** HTML text sits between tags like `<p>your text here</p>` or `<h1>your heading</h1>`. Only change the text between the tags — leave the tags themselves untouched.

---

## Replace or Add Images & Videos

All media files are stored in the [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media) folder.

### Replace an existing image

1. Prepare your new image with **the exact same filename** as the one it replaces (e.g. `Calyxtract-productpic1.JPG`)
2. Open [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media) on GitHub
3. Click **Add file → Upload files**
4. Drop in your new file — GitHub will overwrite the old one if the name matches
5. Scroll down and click **Commit changes**

### Add a new image or video

1. Upload the file to [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media) using the same steps above
2. Note the exact filename (e.g. `new-product-photo.JPG`)
3. Reference it in `index.html` as `src="media/new-product-photo.JPG"`

> **File naming:** Avoid spaces in filenames. Use hyphens or underscores instead (e.g. `product-photo-2.jpg` not `product photo 2.jpg`).

> **Video:** Upload the `.mp4` file to `media/` and embed it in `index.html` using:
> ```html
> <video controls width="100%">
>   <source src="media/your-video.mp4" type="video/mp4" />
> </video>
> ```

---

## Section-by-Section Guide

### Hero (Banner)

The large banner at the top of the page.

**Find in `index.html`:** look for `<!-- HERO -->`

| What to change | What to edit |
|----------------|--------------|
| Main heading | Text inside `<h1>...</h1>` |
| Subtitle paragraph | Text inside `<p>` below the `<h1>` |
| "View Products" button label | Text inside `<a class="btn btn-primary">` |
| "Get in Touch" button label | Text inside `<a class="btn btn-outline">` |

---

### About

Company description, stat cards, and the vision statement.

**Find in `index.html`:** look for `<!-- ABOUT -->`

| What to change | What to edit |
|----------------|--------------|
| Company description paragraphs | Text inside `<div class="about-text">` |
| Stat cards (year, location, %, etc.) | Numbers/text inside `<div class="stat-num">` and `<p>` within `.stat-card` |
| Vision statement | Text inside `<div class="vision-box">` |

---

### Awards & Grants

Three award cards with images and grant amounts.

**Find in `index.html`:** look for `<!-- AWARDS -->`

Each card looks like this:
```html
<div class="award-card">
  <img src="media/birac.png" alt="BIRAC grant" />
  <p>Grant recipient under <strong>BIRAC</strong> — Ignite Innovate Incubate</p>
  <span class="award-amount">INR 5 Mn</span>
</div>
```

| What to change | What to edit |
|----------------|--------------|
| Award logo image | Replace file in `media/` or update the `src="media/..."` path |
| Description text | Text inside `<p>` |
| Grant amount | Text inside `<span class="award-amount">` |

---

### Products

The CalyXtract® product card with images, description, and benefit tiles.

**Find in `index.html`:** look for `<!-- CATALOG -->`

| What to change | What to edit |
|----------------|--------------|
| Product logo | Replace `media/calyxtract_logo.png` in `media/` |
| Product name | Text inside `<h3>` in `.product-header` |
| Subtitle | Text inside `<p>` in `.product-header` |
| Product photos | Replace `Calyxtract-productpic1.JPG` / `Calyxtract-productpic2.JPG` in `media/` |
| Product description | Text inside `<p class="product-desc">` |
| Benefit tiles | Text inside each `<div class="benefit">` block |
| Savings pills | Text inside `<span class="saving-pill">` |

---

### Contact

Location, email, phone, social links, and the enquiry form.

**Find in `index.html`:** look for `<!-- CONTACT -->`

| What to change | What to edit |
|----------------|--------------|
| Email address | Replace both `href="mailto:..."` and the link text |
| Phone number | Replace `+91 – XXXXX XXXXX` with your number |
| Location | Text inside the Location `<span>` |
| Contact form | Sign up at [formspree.io](https://formspree.io), create a form, and replace `YOUR_FORM_ID` in `action="https://formspree.io/f/YOUR_FORM_ID"` |

---

## Add a New Product

1. Open [`index.html`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/blob/main/index.html) and click the pencil icon to edit
2. Find `<!-- CATALOG -->` using Ctrl+F
3. After the closing `</div>` of the last product card, paste this template and fill in your details:

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
    </div>
  </div>
</div>
```

4. Upload any new images to [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media)
5. Commit the changes

---

## Add a New Award

1. Open [`index.html`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/blob/main/index.html) and click the pencil icon
2. Find `<!-- AWARDS -->` using Ctrl+F
3. Inside `<div class="awards-grid">`, add a new card:

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

All colours are defined as variables at the top of [`styles.css`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/blob/main/styles.css).

Open the file, click the pencil icon, and find this block near the top:

```css
:root {
  --blue:       #1565C0;   /* Primary blue — nav, buttons */
  --blue-light: #2196F3;   /* Accent blue — borders, highlights */
  --blue-pale:  #E3F2FD;   /* Light blue — section backgrounds */
  --green:      #2E7D32;   /* Green — savings pills */
  --red:        #C62828;   /* Red — accent, amounts, CTA buttons */
  --dark:       #1A237E;   /* Dark navy — hero, footer, headings */
  --text:       #212121;   /* Body text */
  --muted:      #555;      /* Secondary text */
  --white:      #ffffff;
}
```

Change any hex value (e.g. `#1565C0`) to update that colour site-wide. Use [coolors.co](https://coolors.co) or [Google's color picker](https://www.google.com/search?q=color+picker) to find hex codes.

---

## Commit & Deploy (no terminal)

Every change on GitHub follows the same three steps:

### Step 1 — Open and edit the file

1. Go to the [repository](https://github.com/Contrivation-Labs/contrivationlabs.github.io)
2. Click the file you want to edit (`index.html`, `styles.css`, or a file in `media/`)
3. Click the **pencil icon** (✏️) in the top-right corner to open the editor

### Step 2 — Save your changes

1. When done editing, click the green **Commit changes** button (top-right)
2. In the dialog, optionally add a short description of what you changed (e.g. "Update contact email")
3. Leave **Commit directly to the `main` branch** selected
4. Click **Commit changes**

### Step 3 — Wait for deployment (~60 seconds)

1. Go to the [Actions tab](https://github.com/Contrivation-Labs/contrivationlabs.github.io/actions)
2. You'll see a workflow called **"pages build and deployment"** running
3. Once it shows a green ✅ checkmark, your changes are live
4. Visit the [live site](https://contrivation-labs.github.io/contrivationlabs.github.io/) to confirm

> **To upload files (images/videos):**
> Navigate to [`media/`](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media) → click **Add file → Upload files** → drag and drop → **Commit changes**

---

## Help & Resources

| Resource | Link |
|----------|------|
| This repository | [github.com/Contrivation-Labs/contrivationlabs.github.io](https://github.com/Contrivation-Labs/contrivationlabs.github.io) |
| Live website | [contrivation-labs.github.io/contrivationlabs.github.io](https://contrivation-labs.github.io/contrivationlabs.github.io/) |
| Deployment status | [Actions tab](https://github.com/Contrivation-Labs/contrivationlabs.github.io/actions) |
| Edit index.html | [Open in GitHub editor](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/index.html) |
| Edit styles.css | [Open in GitHub editor](https://github.com/Contrivation-Labs/contrivationlabs.github.io/edit/main/styles.css) |
| Upload media | [media/ folder](https://github.com/Contrivation-Labs/contrivationlabs.github.io/tree/main/media) |
| Contact form setup | [formspree.io](https://formspree.io) |
| Colour picker | [Google colour picker](https://www.google.com/search?q=color+picker) |
| HTML basics | [MDN HTML reference](https://developer.mozilla.org/en-US/docs/Web/HTML) |
| AI assistant for changes | [Claude Code session](https://claude.ai/code/session_01UV9AYgpT46qTgkMJz5jMqJ) |
