# CLI Tool Usage: Book-to-Site Converter

This CLI tool automates the process of converting a PDF textbook into an interactive learning website.

## Prerequisites
Ensure you have the following installed:
- `python3`
- `node.js`
- `pdftotext` (via `poppler-utils`)
- `wkhtmltopdf` (or `weasyprint` for better results)
- `pandoc` (for EPUB generation)

## Step-by-Step Commands

### 1. Initialize a New Project
This sets up the required directory structure and boilerplate files.
```bash
python3 cli.py init
```

### 2. Add a Chapter from PDF
Provide the path to the PDF, a short ID (like `ch1`), and the full title of the chapter.
```bash
python3 cli.py add ./path/to/my-chapter.pdf ch1 "Introduction to Science"
```
*Note: This command extracts text and creates JSON templates in the `src/` directory. You should manually review and edit `src/topics-ch1.json` and `src/quiz-ch1.json` to refine the content.*

### 3. Build the Website and Documents
This generates the interactive HTML pages, consolidated PDFs (via WeasyPrint), and the EPUB e-book (via Pandoc).
```bash
python3 cli.py build
```

### 4. View the Result
Open the dashboard in your web browser:
```bash
# On Linux
xdg-open src/index.html

# On Windows (Browser)
explorer.exe src\index.html
```

## Advanced Customization
- **Style:** Modify `src/style.css` to change the look and feel.
- **Logic:** Update `src/app.js` to change how stages are rendered.
- **Data:** Edit the `.json` files in `src/` to update lesson content or quiz questions.
