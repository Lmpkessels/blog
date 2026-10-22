import datetime
from pathlib import Path
import yaml

# Directories
ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "posts"

def create_blog():
    # Collect metadata
    filename = input("Filename: ").strip()
    title = input("Title: ").strip()
    section = input("Section: ").strip().lower()
    slug = input("Slug: ").strip()

    # Normalize filename and slug
    if not filename:
        raise ValueError("Filename cannot be empty")

    day = datetime.date.today().strftime("%d")

    filename = f"{day}-{filename}"

    if not filename.endswith(".md"):
        filename += ".md"

    slug = "-".join(slug.lower().split())

    if not slug:
        raise ValueError("Slug cannot be empty")

    # Construct metadata
    today = datetime.date.today()
    metadata = {
        "title": title,
        "html_title": f"{title} | Lmpkessels Blog",
        "description": "",
        "section": section,
        "image": "/assets/default.png",
        "alternative": "",
        "date": today.isoformat(),
        "slug": slug,
    }

    # Resolve destination directory
    if not POSTS_DIR.is_dir():
        raise FileNotFoundError(
            f"Drafts directory does not exist: {DRAFTS_DIR}"
        )

    directory = POSTS_DIR / today.strftime("%Y/%m")
    directory.mkdir(parents=True, exist_ok=True)

    filepath = directory / filename

    # Create Markdown file with YAML front matter
    with filepath.open("x", encoding="utf-8") as file:
        file.write("---\n")
        yaml.safe_dump(
            metadata,
            file,
            sort_keys=False,
            allow_unicode=True,
        )
        file.write("---\n\n")

    print(f"Markdown file for blog created at: {filepath}")


if __name__ == "__main__":
    create_blog()
