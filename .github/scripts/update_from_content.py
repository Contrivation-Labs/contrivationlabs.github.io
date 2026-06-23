#!/usr/bin/env python3
"""
Reads content.md, substitutes values into _template.html, writes index.html.
No external dependencies — pure Python stdlib.
"""
import html
import re
from pathlib import Path

BENEFIT_ICONS = ["&#9881;", "&#127798;", "&#128200;", "&#128176;", "&#10003;"]


def parse_content_md(text):
    """
    Parse content.md into a nested dict.
    Returns e.g. {
      "HERO":      {"tagline": "...", "subtext": "..."},
      "ABOUT":     {"description_1": "...", "stat_1_value": "..."},
      "AWARDS":    {"Award 1": {"image": "...", "description": "...", "amount": "..."}},
      "PRODUCT 1": {"logo": "...", "name": "...", ...},
      "CONTACT":   {"location": "...", "email": "...", "phone": "..."},
    }
    """
    data = {}
    current_section = None
    current_subsection = None

    for raw_line in text.splitlines():
        line = raw_line.strip()

        if not line:
            continue

        # Section header: ## [HERO], ## [PRODUCT 1], etc.
        if line.startswith("## [") and line.endswith("]"):
            current_section = line[4:-1].strip().upper()
            data[current_section] = {}
            current_subsection = None
            continue

        # Subsection header: ### Award 1
        if line.startswith("### "):
            current_subsection = line[4:].strip()
            if current_section is not None:
                data[current_section].setdefault(current_subsection, {})
            continue

        # Skip comment lines (must come after ## / ### checks above)
        if line.startswith("#"):
            continue

        # Key: value pair
        if ": " in line and current_section is not None:
            key, _, value = line.partition(": ")
            key = key.strip().lower()
            value = value.strip()
            if current_subsection:
                data[current_section][current_subsection][key] = value
            else:
                data[current_section][key] = value

    return data


def e(value):
    """HTML-escape a plain-text value from content.md."""
    return html.escape(value, quote=False)


def build_awards_block(awards_data):
    cards = []
    for key in sorted(awards_data.keys()):
        award = awards_data[key]
        image = award.get("image", "")
        description = e(award.get("description", ""))
        amount = e(award.get("amount", ""))
        cards.append(
            f'    <div class="award-card">\n'
            f'      <img src="{image}" alt="{e(key)}" />\n'
            f'      <p>{description}</p>\n'
            f'      <span class="award-amount">{amount}</span>\n'
            f'    </div>'
        )
    return "\n".join(cards)


def build_products_block(data):
    cards = []
    # Collect all PRODUCT N sections in order
    product_keys = sorted(
        [k for k in data if re.match(r"PRODUCT\s+\d+", k)],
        key=lambda k: int(re.search(r"\d+", k).group())
    )

    for section_key in product_keys:
        p = data[section_key]
        logo        = p.get("logo", "")
        name        = e(p.get("name", ""))
        subtitle    = e(p.get("subtitle", ""))
        photo_1     = p.get("photo_1", "")
        photo_2     = p.get("photo_2", "")
        description = e(p.get("description", ""))

        # Benefits
        benefits_html = ""
        for i in range(1, 10):
            title = p.get(f"benefit_{i}_title", "")
            text  = p.get(f"benefit_{i}_text", "")
            if not title:
                break
            icon = BENEFIT_ICONS[min(i - 1, len(BENEFIT_ICONS) - 1)]
            benefits_html += (
                f'        <div class="benefit">\n'
                f'          <div class="benefit-icon">{icon}</div>\n'
                f'          <div>\n'
                f'            <h4>{e(title)}</h4>\n'
                f'            <p>{e(text)}</p>\n'
                f'          </div>\n'
                f'        </div>\n'
            )

        # Savings pills
        savings_html = ""
        for i in range(1, 10):
            saving = p.get(f"saving_{i}", "")
            if not saving:
                break
            css = "saving-pill red-pill" if "↑" in saving else "saving-pill"
            savings_html += f'        <span class="{css}">{e(saving)}</span>\n'

        cards.append(
            f'  <div class="product-card">\n'
            f'    <div class="product-header">\n'
            f'      <img src="{logo}" alt="{name} logo" />\n'
            f'      <div>\n'
            f'        <h3>{name}</h3>\n'
            f'        <p>{subtitle}</p>\n'
            f'      </div>\n'
            f'    </div>\n'
            f'    <div class="product-body">\n'
            f'      <div class="product-images">\n'
            f'        <img src="{photo_1}" alt="{name} — photo 1" />\n'
            f'        <img src="{photo_2}" alt="{name} — photo 2" />\n'
            f'      </div>\n'
            f'      <p class="product-desc">{description}</p>\n'
            f'      <div class="benefits">\n'
            f'{benefits_html}'
            f'      </div>\n'
            f'      <div class="savings-bar">\n'
            f'{savings_html}'
            f'      </div>\n'
            f'    </div>\n'
            f'  </div>'
        )

    return "\n".join(cards)


def main():
    content_raw  = Path("content.md").read_text(encoding="utf-8")
    template     = Path("_template.html").read_text(encoding="utf-8")
    data         = parse_content_md(content_raw)

    hero    = data.get("HERO", {})
    about   = data.get("ABOUT", {})
    awards  = data.get("AWARDS", {})
    contact = data.get("CONTACT", {})

    replacements = {
        # Hero
        "{{HERO_TAGLINE}}":       e(hero.get("tagline", "")),
        "{{HERO_SUBTEXT}}":       e(hero.get("subtext", "")),
        "{{HERO_BTN_PRIMARY}}":   e(hero.get("button_primary", "View Products")),
        "{{HERO_BTN_SECONDARY}}": e(hero.get("button_secondary", "Get in Touch")),
        # About — descriptions
        "{{ABOUT_DESC_1}}": e(about.get("description_1", "")),
        "{{ABOUT_DESC_2}}": e(about.get("description_2", "")),
        "{{ABOUT_DESC_3}}": e(about.get("description_3", "")),
        # About — stats
        "{{ABOUT_STAT_1_VALUE}}": e(about.get("stat_1_value", "")),
        "{{ABOUT_STAT_1_LABEL}}": e(about.get("stat_1_label", "")),
        "{{ABOUT_STAT_2_VALUE}}": e(about.get("stat_2_value", "")),
        "{{ABOUT_STAT_2_LABEL}}": e(about.get("stat_2_label", "")),
        "{{ABOUT_STAT_3_VALUE}}": e(about.get("stat_3_value", "")),
        "{{ABOUT_STAT_3_LABEL}}": e(about.get("stat_3_label", "")),
        "{{ABOUT_STAT_4_VALUE}}": e(about.get("stat_4_value", "")),
        "{{ABOUT_STAT_4_LABEL}}": e(about.get("stat_4_label", "")),
        # About — vision
        "{{ABOUT_VISION}}": e(about.get("vision", "")),
        # Awards and products — generated blocks
        "{{AWARDS_BLOCK}}":   build_awards_block(awards),
        "{{PRODUCTS_BLOCK}}": build_products_block(data),
        # Contact
        "{{CONTACT_LOCATION}}": e(contact.get("location", "")),
        "{{CONTACT_EMAIL}}":    e(contact.get("email", "")),
        "{{CONTACT_PHONE}}":    e(contact.get("phone", "")),
    }

    output = template
    for placeholder, value in replacements.items():
        output = output.replace(placeholder, value)

    # Warn about any missed placeholders
    missed = re.findall(r"\{\{[A-Z_0-9]+\}\}", output)
    if missed:
        print(f"Warning: unfilled placeholders: {missed}")

    with open("index.html", "w", encoding="utf-8", newline="\n") as f:
        f.write(output)
    print("index.html built from _template.html + content.md")


if __name__ == "__main__":
    main()
