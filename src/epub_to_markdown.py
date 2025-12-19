import sys
import zipfile
import tempfile
import subprocess
from pathlib import Path


def extract_epub(epub_path: Path, extract_to: Path):
    with zipfile.ZipFile(epub_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


def convert_html_to_markdown(html_file: Path, output_md: Path, lua_filter: Path):
    output_md.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "pandoc",
        str(html_file),

        # Input → Output
        "-f", "html",
        "-t", "gfm",

        # Remove all metadata
        "--metadata=title:",
        "--metadata=author:",
        "--metadata=date:",

        # Clean markdown
        "--wrap=none",
        "--strip-comments",
        "--no-highlight",

        # HTML cleanup + enhancements
        "--lua-filter", str(lua_filter),

        "-o", str(output_md)
    ]

    subprocess.run(cmd, check=True)


def process_epub(epub_path: str, target_dir: str):
    epub_path = Path(epub_path).resolve()
    target_dir = Path(target_dir).resolve()
    target_dir.mkdir(parents=True, exist_ok=True)

    if not epub_path.exists():
        raise FileNotFoundError(f"EPUB not found: {epub_path}")

    with tempfile.TemporaryDirectory(prefix="epub_extract_") as tmp:
        tmp_path = Path(tmp)

        extract_epub(epub_path, tmp_path)

        html_files = list(tmp_path.rglob("*.html")) + list(tmp_path.rglob("*.xhtml"))
        if not html_files:
            print("No HTML/XHTML files found.")
            return

        # Lua filter with optional enhancements applied
        lua_filter = tmp_path / "clean_html.lua"
        lua_filter.write_text(
            """
-- Remove all raw HTML
function RawBlock(el) return {} end
function RawInline(el) return {} end
function Comment(el) return {} end

-- Remove all attributes (class, id, style)
function Attr(el)
  return pandoc.Attr("", {}, {})
end

-- Unwrap all divs (calibre layout junk)
function Div(el)
  return el.content
end

-- Unwrap all spans
function Span(el)
  return el.content
end

-- Remove empty paragraphs
function Para(el)
  if #el.content == 0 then
    return {}
  end
end

-- Normalize headings (h2→h1, h3→h2, etc.)
function Header(el)
  if el.level > 1 then
    el.level = el.level - 1
  end
  return el
end
""",
            encoding="utf-8"
        )

        for html_file in html_files:
            rel_path = html_file.relative_to(tmp_path)
            md_path = target_dir / rel_path.with_suffix(".md")

            print(f"Converting: {rel_path}")
            convert_html_to_markdown(html_file, md_path, lua_filter)

        print("✔ EPUB converted to clean, reader-visible Markdown")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:")
        print("  python epub_to_markdown_clean.py input.epub output_directory")
        sys.exit(1)

    process_epub(sys.argv[1], sys.argv[2])
