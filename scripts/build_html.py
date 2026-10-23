import datetime
import re
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET

import markdown

from organise_content import (
    ROOT, CONTENT_DIR, HOME_DIR, organise_content, publication_date, read_blog
)

POSTS_DIR = ROOT / "posts"
TPL_DIR = ROOT / "templates"
SITE_URL = "https://lmpkessels.com"
DEFAULT_IMAGE = "/assets/default.png"

SECTION_LABELS = {
    "math": "Mathematics",
    "algos": "Algorithms",
    "blockchain": "Blockchain",
    "comp-sci": "Comp-sci",
    "homepage": "lkessels blog",
    "misc": "lkessels blog",
}

SECTION_TITLES = {
    "math": "Mathematics | lkessels blog",
    "algos": "Algorithms | lkessels blog",
    "blockchain": "Blockchain | lkessels blog",
    "comp-sci": "Comp-sci | lkessels blog",
    "homepage": "All posts | lkessels blog",
    "misc": "lkessels Misc | lkessels blog",
}


def slugify(value):
    value = str(value).lower().strip().replace(" ", "-")
    value = re.sub(r"[^a-z0-9-]", "", value)
    return re.sub(r"-{2,}", "-", value).strip("-")


def fmt_date_h(value):
    return value.strftime("%Y %b %d")


def label_for(section):
    return SECTION_LABELS.get(section, section.replace("-", " ").title())


def safe_alt(value, limit=420):
    value = re.sub(r"<[^>]+>", "", str(value))
    return re.sub(r"\s+", " ", value).strip()[:limit]


def dedupe(items):
    seen, result = set(), []
    for item in items:
        if item[2] not in seen:
            seen.add(item[2])
            result.append(item)
    return result


def list_items(posts):
    ordered = dedupe(sorted(posts, key=lambda item: item[0], reverse=True))
    return "\n".join(
        f'<li class="post-li"><span class="post-date">{fmt_date_h(d)}</span> '
        f'<h2 class="h2-home"><a href="{escape(url, quote=True)}" '
        f'class="content-header">{escape(title)}</a></h2></li>'
        for d, title, url in ordered
    )


def build():
    post_template = (TPL_DIR / "post.html").read_text(encoding="utf-8")
    home_template = (TPL_DIR / "homepage.html").read_text(encoding="utf-8")
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    HOME_DIR.mkdir(parents=True, exist_ok=True)
    all_posts, by_section = [], {}

    for md_path in sorted(POSTS_DIR.rglob("*.md")):
        metadata, body_md = read_blog(md_path)
        directory, section, _ = organise_content(md_path, metadata)
        published = publication_date(metadata, md_path)
        slug = slugify(metadata.get("slug") or md_path.stem)
        if not slug:
            raise ValueError(f"Missing or invalid slug in {md_path}")
        title = str(metadata.get("title") or md_path.stem)
        desc = str(metadata.get("description") or "")[:160]
        image = str(metadata.get("image") or DEFAULT_IMAGE)
        alt = safe_alt(metadata.get("alternative") or desc or slug.replace("-", " "))
        html_title = str(metadata.get("html_title") or f"{title} | lkessels blog")
        body_html = markdown.markdown(body_md, extensions=["tables", "fenced_code"])
        relative_url = f"/content/{published:%Y/%m}/{slug}.html"
        canonical = f"{SITE_URL}{relative_url}"

        html_out = (post_template
            .replace("$html_title$", escape(html_title, quote=True))
            .replace("$title$", escape(title))
            .replace("$date$", fmt_date_h(published))
            .replace("$body$", body_html)
            .replace("$desc$", escape(desc, quote=True))
            .replace("$canonical$", escape(canonical, quote=True))
            .replace("$image$", escape(image, quote=True))
            .replace("$alternative$", escape(alt, quote=True)))
        post_file = directory / f"{slug}.html"
        post_file.write_text(html_out, encoding="utf-8")
        print("Built post:", post_file)

        item = (published, title, relative_url)
        all_posts.append(item)
        by_section.setdefault(section, []).append(item)

    root_home = (home_template
        .replace("$html_title$", "lkessels | blog")
        .replace("$section$", "lkessels blog")
        .replace("$posts$", list_items(all_posts)))
    (ROOT / "index.html").write_text(root_home, encoding="utf-8")

    for section, posts in by_section.items():
        label = label_for(section)
        section_html = (home_template
            .replace("$html_title$", escape(SECTION_TITLES.get(section, f"{label} | lkessels blog")))
            .replace("$section$", escape(label))
            .replace("$posts$", list_items(posts)))
        section_file = HOME_DIR / f"{section}.html"
        section_file.write_text(section_html, encoding="utf-8")
        print("Built section:", section_file)

    namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"
    custom_namespace = "https://lmpkessels.com/ns"
    ET.register_namespace("", namespace)
    ET.register_namespace("custom", custom_namespace)
    urlset = ET.Element(f"{{{namespace}}}urlset")
    for published, title, url in dedupe(sorted(all_posts, key=lambda item: item[0], reverse=True)):
        entry = ET.SubElement(urlset, f"{{{namespace}}}url")
        ET.SubElement(entry, f"{{{namespace}}}loc").text = f"{SITE_URL}{url}"
        ET.SubElement(entry, f"{{{namespace}}}lastmod").text = published.isoformat()
        ET.SubElement(entry, f"{{{custom_namespace}}}title").text = title
        ET.SubElement(entry, f"{{{custom_namespace}}}date").text = published.isoformat()
    ET.ElementTree(urlset).write(ROOT / "sitemap.xml", encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    build()
