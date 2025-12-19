# EPUB to Clean Markdown Converter

## Overview

This Python script converts an **EPUB file** into **clean, reader-visible Markdown**.

It is designed to:
- Extract EPUB safely into a temporary folder
- Convert each HTML/XHTML file into Markdown
- Remove **all HTML tags**, layout junk, and metadata
- Eliminate Calibre-specific wrappers (`calibre1`, `calibre2`, etc.)
- Keep **only the text that is visible to the reader**
- Produce clean, readable Markdown suitable for:
  - Notes
  - Quiz generation
  - Publishing
  - Further text processing (Tamil / Sanskrit / English)

---

## Features

### ✅ What the script DOES

- Extracts EPUB (ZIP-based format)
- Processes **each chapter independently**
- Converts HTML → Markdown using Pandoc
- Cleans HTML using Pandoc Lua filters
- Removes:
  - `<div>`, `<span>`, `<meta>`, `<nav>`
  - Calibre-generated classes
  - Hidden / layout-only elements
  - YAML metadata headers
- Normalizes headings
- Removes empty paragraphs
- Preserves readable text flow

### ❌ What the script DOES NOT DO

- It does **not merge chapters** into one file
- It does **not infer reading order from OPF**
- It does **not include images**
- It does **not modify text content**

---

## Requirements

### Software Dependencies

- Python **3.8+**
- Pandoc **2.17+**

Check Pandoc installation:

```bash
pandoc --version
Below is **complete documentation in Markdown** for the final script
`epub_to_markdown_clean.py`, written as **user + developer documentation**.

You can **save this directly as** `EPUB_TO_MARKDOWN_DOCUMENTATION.md`
and convert it later using Pandoc if needed.

---

````markdown
# EPUB to Clean Markdown Converter

## Overview

This Python script converts an **EPUB file** into **clean, reader-visible Markdown**.

It is designed to:
- Extract EPUB safely into a temporary folder
- Convert each HTML/XHTML file into Markdown
- Remove **all HTML tags**, layout junk, and metadata
- Eliminate Calibre-specific wrappers (`calibre1`, `calibre2`, etc.)
- Keep **only the text that is visible to the reader**
- Produce clean, readable Markdown suitable for:
  - Notes
  - Quiz generation
  - Publishing
  - Further text processing (Tamil / Sanskrit / English)

---

## Features

### ✅ What the script DOES

- Extracts EPUB (ZIP-based format)
- Processes **each chapter independently**
- Converts HTML → Markdown using Pandoc
- Cleans HTML using Pandoc Lua filters
- Removes:
  - `<div>`, `<span>`, `<meta>`, `<nav>`
  - Calibre-generated classes
  - Hidden / layout-only elements
  - YAML metadata headers
- Normalizes headings
- Removes empty paragraphs
- Preserves readable text flow

### ❌ What the script DOES NOT DO

- It does **not merge chapters** into one file
- It does **not infer reading order from OPF**
- It does **not include images**
- It does **not modify text content**

---

## Requirements

### Software Dependencies

- Python **3.8+**
- Pandoc **2.17+**

Check Pandoc installation:

```bash
pandoc --version
````

---

## Script File

```
epub_to_markdown_clean.py
```

---

## Usage

```bash
python epub_to_markdown_clean.py input.epub output_directory/
```

### Example

```bash
python epub_to_markdown_clean.py tamil_book.epub md_output/
```

### Output Structure

```
md_output/
├── OEBPS/
│   ├── chapter1.md
│   ├── chapter2.md
│   └── text/
│       └── appendix.md
```

The directory structure inside the EPUB is preserved.

---

## How the Script Works (Step-by-Step)

### 1. EPUB Extraction

* EPUB is a ZIP archive
* Extracted using Python’s `zipfile` module
* Extraction happens in a **temporary directory**
* Temporary files are deleted automatically after execution

```python
zipfile.ZipFile(epub_path).extractall(temp_dir)
```

---

### 2. HTML/XHTML Discovery

The script searches recursively for:

* `.html`
* `.xhtml`

These files represent book chapters.

---

### 3. Pandoc Conversion

Each HTML file is converted using Pandoc:

```bash
pandoc input.html -f html -t gfm -o output.md
```

With additional options to:

* Remove metadata
* Disable syntax highlighting
* Prevent line wrapping

---

### 4. Lua Filter (Core Cleaning Logic)

A **Lua filter** is dynamically created and passed to Pandoc.

This filter operates on Pandoc’s **AST (Abstract Syntax Tree)**.

#### Key Cleanup Operations

##### Remove all raw HTML

```lua
function RawBlock(el) return {} end
function RawInline(el) return {} end
```

##### Remove comments

```lua
function Comment(el) return {} end
```

##### Strip all attributes (class, id, style)

```lua
function Attr(el)
  return pandoc.Attr("", {}, {})
end
```

##### Unwrap layout-only containers

```lua
function Div(el)
  return el.content
end

function Span(el)
  return el.content
end
```

This removes:

* `<div class="calibre3">`
* `<span class="calibre4">`
* Any layout wrappers

---

### 5. Optional Enhancements (Applied)

#### Remove empty paragraphs

```lua
function Para(el)
  if #el.content == 0 then
    return {}
  end
end
```

#### Normalize headings

```lua
function Header(el)
  if el.level > 1 then
    el.level = el.level - 1
  end
  return el
end
```

Effect:

* `h2 → h1`
* `h3 → h2`
* Cleaner Markdown hierarchy

---

## Output Guarantees

### Output Markdown Contains

✅ Headings
✅ Paragraphs
✅ Lists
✅ Tables (if present)
✅ Emphasis (bold / italic)

### Output Markdown Does NOT Contain

❌ HTML tags
❌ Calibre junk
❌ Metadata headers
❌ Navigation / TOC
❌ Hidden elements

---

## Before vs After Example

### Input HTML (from EPUB)

```html
<div class="calibre3">
  <span class="calibre4">இது ஒரு உரை.</span>
</div>
```

### Output Markdown

```markdown
இது ஒரு உரை.
```

---

## Why Pandoc + Lua Filter?

| Approach      | Reason                         |
| ------------- | ------------------------------ |
| Regex cleanup | Unsafe for HTML                |
| BeautifulSoup | Loses document semantics       |
| Pandoc AST    | Safe, structured, professional |

This approach is **industry-standard** for EPUB pipelines.

---

## Known Limitations

* Images are ignored
* Footnotes are kept as-is
* Reading order is filesystem-based (not OPF-based)

---

## Possible Extensions

* Merge all chapters into one Markdown file
* OPF-based reading order
* Image extraction
* Quiz generation from Markdown (Tamil supported)
* Typst / PDF generation
* CLI flags (`--single`, `--toc`, etc.)

---

## License

Free to use for:

* Personal projects
* Educational use
* Research and text processing

---

## Author Notes

This script is optimized for:

* EPUBs generated by Calibre
* Indian language texts (Tamil / Sanskrit)
* Clean downstream NLP or educational processing

```

---

If you want, I can next:

- Generate **quiz documentation** for Tamil Markdown  
- Convert this documentation into **PDF / HTML**
- Turn the script into a **CLI tool**
- Add **unit tests**

Just tell me 👍
```
