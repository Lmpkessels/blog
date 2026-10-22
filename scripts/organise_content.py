from datetime import date
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"
HOME_DIR = CONTENT_DIR / "homepages"


def read_blog(blog_md):
    """Read YAML front matter and Markdown body from a published article."""
    path = Path(blog_md)
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n(.*)\Z", text, re.S)
    if not match:
        raise ValueError(f"Missing or invalid YAML front matter: {path}")
    metadata = yaml.safe_load(match.group(1))
    if not isinstance(metadata, dict):
        raise ValueError(f"YAML front matter must be a mapping: {path}")
    return metadata, match.group(2)


def publication_date(metadata, path):
    value = metadata.get("date")
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            pass
    raise ValueError(f"Missing or invalid publication date in {path}")


def section_name(metadata, path):
    section = metadata.get("section")
    if not isinstance(section, str) or not section.strip():
        raise ValueError(f"Missing section in {path}")
    section = section.strip().lower()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", section):
        raise ValueError(f"Invalid section identifier {section!r} in {path}")
    return section


def organise_content(blog_md, metadata=None):
    """Ensure article and section output directories exist; return their paths."""
    path = Path(blog_md)
    if metadata is None:
        metadata, _ = read_blog(path)
    published = publication_date(metadata, path)
    section = section_name(metadata, path)
    directory = CONTENT_DIR / published.strftime("%Y/%m")
    directory.mkdir(parents=True, exist_ok=True)
    HOME_DIR.mkdir(parents=True, exist_ok=True)
    section_page = HOME_DIR / f"{section}.html"
    # The builder generates the section page from all articles, not an empty placeholder.
    return directory, section, section_page
