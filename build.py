import re, pathlib, datetime, markdown
import xml.etree.ElementTree as ET

# ---------- Paths ----------
ROOT       = pathlib.Path(__file__).parent
POSTS_DIR  = ROOT / "posts"
TPL_DIR    = ROOT / "templates"
OUT_DIR    = ROOT / "content"
HOME_DIR   = OUT_DIR / "0000"   # section homepages live here

SITE_URL   = "https://lmpkessels.com"

# ---------- Templates ----------
POST_TPL   = (TPL_DIR / "post.html").read_text(encoding="utf-8")
HOME_TPL   = (TPL_DIR / "homepage.html").read_text(encoding="utf-8")

# ---------- Defaults ----------
DEFAULT_IMAGE = "/assets/default.png"

# ---------- Regex ----------
FM_RE    = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.S)
FNAME_RE = re.compile(r"^(?P<y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})-(?P<slug>.+)\.md$", re.I)

SECTION_LABELS = {
    "math": "Mathematics",
    "hq": "lkessels blog",
    "thinking": "Thinking Vault",
    "misc": "lkessels blog",  # fallback
}
def label_for(sec: str) -> str:
    return SECTION_LABELS.get(sec.lower(), sec.title())

# ---------- Section Titles (for <title> in <head>) ----------
SECTION_TITLES = {
    "math": "Mathematics | lkessels blog",
    "thinking": "Thinking Vault | lkessels blog",
    "hq": "lkessels Headquarters | lkessels blog",
    "misc": "lkessels Misc | lkessels blog",
}

# ---------- Helpers ----------
def slugify(s: str) -> str:
    s = s.lower().strip().replace(" ", "-")
    s = re.sub(r"[^a-z0-9\-]", "", s)
    return re.sub(r"-{2,}", "-", s)

def fmt_date_h(d: datetime.date) -> str:
    return d.strftime("%Y %b %d")   # → "2025 Apr 16"

def parse_front_matter(text: str):
    m = FM_RE.match(text)
    if not m:
        return {}, text
    raw, body = m.groups()
    meta = {}
    for line in raw.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip().lower()] = v.strip()
    return meta, body

def parse_title(md_text: str, fallback: str) -> str:
    m = re.search(r"^\s*#\s+(.+)$", md_text, re.M)
    return m.group(1).strip() if m else fallback

def dedupe(items):
    seen, out = set(), []
    for d, t, u in items:
        if u not in seen:
            seen.add(u)
            out.append((d, t, u))
    return out

# ---------- Build ----------
def build():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    HOME_DIR.mkdir(parents=True, exist_ok=True)

    all_posts, by_section, by_month = [], {}, {}

    for md_path in sorted(POSTS_DIR.glob("*.md")):
        raw = md_path.read_text(encoding="utf-8")
        fm, body_md = parse_front_matter(raw)

        # --- defaults from filename ---
        m = FNAME_RE.match(md_path.name)
        if m:
            date = datetime.date(int(m["y"]), int(m["m"]), int(m["d"]))
            slug = slugify(m["slug"])
        else:
            date = datetime.date.today()
            slug = slugify(md_path.stem)

        # --- front matter overrides ---
        if "date" in fm:
            try: 
                date = datetime.date.fromisoformat(fm["date"])
            except ValueError: 
                pass
        if "slug" in fm:
            slug = slugify(fm["slug"])

        section = (fm.get("section") or "misc").lower()
        title   = fm.get("title") or parse_title(body_md, md_path.stem)
        desc    = (fm.get("description") or "")[:160]
        image   = fm.get("image", DEFAULT_IMAGE)

         # html_title logic
        if "html_title" in fm:
            post_html_title = fm["html_title"]
        else:
            post_html_title = f"{title} | lkessels blog"

        # convert Markdown
        md = markdown.Markdown(extensions=["tables", "fenced_code"])
        body_html = md.convert(body_md)

        # --- output path: /content/YYYY/YYYY-MM/slug.html ---
        year_dir   = OUT_DIR / f"{date.year}"
        month_code = f"{date.year}-{date.month:02d}"
        month_dir  = year_dir / month_code
        month_dir.mkdir(parents=True, exist_ok=True)

        post_file  = month_dir / f"{slug}.html"
        canonical  = f"{SITE_URL}/content/{date.year}/{month_code}/{slug}.html"

        html_out = (POST_TPL
            .replace("$html_title$", post_html_title)
            .replace("$title$", title)
            .replace("$date$", fmt_date_h(date))
            .replace("$body$", body_html)
            .replace("$desc$", desc)
            .replace("$canonical$", canonical)
            .replace("$image$", image)
        )

        post_file.write_text(html_out, encoding="utf-8")
        print("Built post:", post_file)

        url_abs = f"/content/{date.year}/{month_code}/{slug}.html"
        item = (date, title, url_abs)

        all_posts.append(item)
        by_section.setdefault(section, []).append(item)
        by_month.setdefault((date.year, date.month), []).append(item)

    # ----- Root homepage -----
    all_posts.sort(key=lambda x: x[0], reverse=True)
    all_posts = dedupe(all_posts)
    all_items = [
        f'<li class="post-li"><span class="post-date">{fmt_date_h(d)}</span> '  
        f'<h2><a href="{url}" class="content-header">{t}</a></h2></li>'
        for d, t, url in all_posts
    ]
    root_home = (HOME_TPL
        .replace("$html_title$", "lkessels | blog")   # <title> in <head>
        .replace("$section$", "lkessels | blog")
        .replace("$posts$", "\n".join(all_items))
    )
    (ROOT / "index.html").write_text(root_home, encoding="utf-8")

    # ----- Section pages (Math, etc) -----
    for sec, posts in by_section.items():
        posts.sort(key=lambda x: x[0], reverse=True)
        posts = dedupe(posts)
        items = [
            f'<li class="post-li"><span class="post-date">{fmt_date_h(d)}</span> '
            f'<h2><a href="{url}" class="content-header">{t}</a></h2></li>'
            for d, t, url in posts
        ]
        label = label_for(sec)
        html = (HOME_TPL
            .replace("$html_title$", SECTION_TITLES.get(sec, f"{label} | lkessels"))  # <title>
            .replace("$section$", label)
            .replace("$posts$", "\n".join(items))
        )
        (HOME_DIR / f"{sec}.html").write_text(html, encoding="utf-8")

    # ----- Sitemap ----- #
    nsmap = {"custom": "https://lmpkessels.com/ns"}
    urlset = ET.Element("urlset", {
        "xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9",
        **{f"xmlns:{k}": v for k, v in nsmap.items()}
    })

    for d, t, url in all_posts:
        url_el = ET.SubElement(urlset, "url")
        ET.SubElement(url_el, "loc").text = f"{SITE_URL}{url}"
        ET.SubElement(url_el, "lastmod").text = d.isoformat()
        ET.SubElement(url_el, "{https://lukefi.com/ns}title").text = t
        ET.SubElement(url_el, "{https://lukefi.com/ns}date").text = d.isoformat()

    sitemap_xml = ET.tostring(urlset, encoding="utf-8", xml_declaration=True)
    (ROOT / "sitemap.xml").write_bytes(sitemap_xml)


if __name__ == "__main__":
    build()
