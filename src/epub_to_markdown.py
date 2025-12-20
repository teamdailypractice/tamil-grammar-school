import sys
import zipfile
import tempfile
import subprocess
from pathlib import Path
import re


HTML_TAG_RE = re.compile(r"</?[a-zA-Z][^>]*>")


def extract_epub(epub_path: Path, extract_to: Path):
    with zipfile.ZipFile(epub_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)


def convert_html_to_markdown(html_file: Path, output_md: Path, lua_filter: Path):
    output_md.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "pandoc",
        str(html_file),

        # Input → Output
        "-f", "html",
        "-t", "commonmark",   # ✅ VALID writer

        # Strip metadata
        "--metadata=title:",
        "--metadata=author:",
        "--metadata=date:",

        # Markdown hygiene
        "--wrap=none",
        "--strip-comments",
        "--no-highlight",

        # Extract images
        "--extract-media=.",

        # Lua cleanup
        "--lua-filter", str(lua_filter),

        "-o", str(output_md),
    ]

    subprocess.run(cmd, check=True)


def hard_strip_html(md_file: Path):
    """
    LAST-RESORT HTML REMOVAL.
    This guarantees no <span>, <table>, <tr>, etc survive.
    """
    text = md_file.read_text(encoding="utf-8", errors="ignore")

    # Preserve fenced code blocks
    blocks = {}
    def _store(match):
        key = f"__CODE_BLOCK_{len(blocks)}__"
        blocks[key] = match.group(0)
        return key

    text = re.sub(r"```.*?```", _store, text, flags=re.S)

    # Remove ALL remaining HTML tags
    text = re.sub(r"</?[a-zA-Z][^>]*>", "", text)

    # Restore code blocks
    for k, v in blocks.items():
        text = text.replace(k, v)

    md_file.write_text(text, encoding="utf-8")


def validate_markdown_no_html(md_file: Path):
    content = md_file.read_text(encoding="utf-8", errors="ignore")
    content = re.sub(r"```.*?```", "", content, flags=re.S)

    if HTML_TAG_RE.search(content):
        raise RuntimeError(
            f"\n❌ HTML detected in output Markdown:\n   {md_file}\n"
        )


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

        # -----------------------------------------------------
        # FINAL Lua filter
        # -----------------------------------------------------
        lua_filter = tmp_path / "clean_html.lua"
        lua_filter.write_text(
            r"""
-- =========================================================
-- AGGRESSIVE HTML REMOVAL FILTER
-- =========================================================

function RawBlock(el) return {} end
function RawInline(el) return {} end
function Comment(el) return {} end

function Attr(el)
  return pandoc.Attr("", {}, {})
end

-- DROP ALL spans completely
function Span(el)
  return {}
end

-- Unwrap divs
function Div(el)
  return el.content
end

function Para(el)
  if #el.content == 0 then
    return {}
  end
end

function Header(el)
  if el.level > 1 then
    el.level = el.level - 1
  end
  el.attr = pandoc.Attr("", {}, {})
  return el
end

function Image(el)
  return pandoc.Image(
    el.caption,
    el.src,
    "",
    pandoc.Attr("", {}, {})
  )
end

function Table(el)
  el.attr = pandoc.Attr("", {}, {})
  return el
end

function TableRow(el)
  el.attr = pandoc.Attr("", {}, {})
  return el
end

function TableCell(el)
  el.attr = pandoc.Attr("", {}, {})
  return el
end
""",
            encoding="utf-8",
        )

        converted = 0

        for html_file in html_files:
            rel_path = html_file.relative_to(tmp_path)
            md_path = target_dir / rel_path.with_suffix(".md")

            print(f"Converting: {rel_path}")
            convert_html_to_markdown(html_file, md_path, lua_filter)

            # 🔒 HARD GUARANTEE
            hard_strip_html(md_path)
            validate_markdown_no_html(md_path)

            converted += 1

        print(f"\n✔ Converted {converted} files")
        print("✔ GUARANTEED: ZERO HTML in Markdown")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:")
        print("  python epub_to_markdown_clean.py input.epub output_directory")
        sys.exit(1)

    process_epub(sys.argv[1], sys.argv[2])
