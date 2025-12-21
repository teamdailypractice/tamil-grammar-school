# Developer Documentation: Class 9 Science Interactive Platform

This document provides a technical overview of the application architecture, data structures, and build processes for developers.

## 1. Project Overview
The application is a client-side, static-first interactive learning platform for CBSE Class 9 Science. It features structured lessons, a dual-mode quiz system (Practice/Exam), progress tracking via `localStorage`, and automated offline document generation (PDF/EPUB).

## 2. Tech Stack
- **Frontend:** Vanilla HTML5, CSS3, JavaScript (ES6+).
- **Data Storage:** JSON files for lessons and quizzes.
- **Persistence:** Browser `localStorage`.
- **Generation Tools:**
  - `Node.js`: Coordination and static HTML generation.
  - `WeasyPrint`: High-quality PDF generation with bookmarks and internal links.
  - `Pandoc`: EPUB generation from Markdown.

## 3. Directory Structure
- `src/`: The core application files.
  - `index.html`: The main dashboard/menu.
  - `chapter-[ID].html`: Lesson entry points for specific chapters.
  - `app.js`: Main logic for lesson rendering, navigation, and sidebar.
  - `exam.html` / `exam.js`: The quiz engine (Practice and Timed modes).
  - `download.html`: Dynamic download interface.
  - `topics-ch[ID].json`: Structured content for each chapter.
  - `quiz-ch[ID].json`: Question bank for each chapter.
  - `style.css`: Unified styling for the platform.
- `generate_static_files.js`: Script to generate standalone HTML and PDF files.
- `generate_epub.js`: Script to generate the comprehensive EPUB e-book.

## 4. Data Schemas

### Topics JSON (`topics-ch[ID].json`)
```json
{
  "topics": [
    {
      "title": "Topic Name",
      "stages": [
        { "type": "text", "heading": "Sub-heading", "content": "Text body..." },
        { "type": "quiz", "heading": "Quick Quiz" }
      ]
    }
  ]
}
```

### Quiz JSON (`quiz-ch[ID].json`)
```json
{
  "topics": [
    {
      "title": "Topic Name",
      "questions": [
        {
          "question": "Question text?",
          "options": ["Opt 1", "Opt 2", "Opt 3", "Opt 4"],
          "answer": "Opt 1"
        }
      ]
    }
  ]
}
```

## 5. Core Logic Implementation

### Multi-Chapter Support
- The application uses URL parameters (`?chapter=ch6`) to identify the context.
- Individual chapter HTML files use a `data-chapter` attribute on the `<body>` tag to signal `app.js` which JSON data to fetch.

### Progress Tracking
- Stored in `localStorage` using keys formatted as `biology-ch[ID]-progress`.
- **Versioning:** An `APP_VERSION` constant is used. If the version in storage mismatches the app version, progress is reset to prevent crashes from schema changes.

### PDF Generation
- Uses **WeasyPrint**. 
- Advanced CSS attributes like `target-counter(attr(href), page)` are used to generate dynamic page numbers in the Table of Contents.
- Headings are mapped to `bookmark-level` to create a native PDF outline.

### EPUB Generation
- Uses **Pandoc**.
- A custom Node script iterates through all JSON files, converts the content into a single Markdown file with metadata (YAML front matter), and calls Pandoc to generate the `.epub`.

## 6. Maintenance and Expansion

### Adding a New Chapter
1. **Prepare Data:** Create `src/topics-chX.json` and `src/quiz-chX.json`.
2. **Create Page:** Copy `src/chapter-5.html` to `src/chapter-X.html` and update the `data-chapter` attribute.
3. **Update Dashboard:** Add the new chapter to the list in `src/index.html`.
4. **Update Build Scripts:** Add the new chapter ID to the `chapters` array in both `generate_static_files.js` and `generate_epub.js`.
5. **Generate:** Run `node generate_static_files.js` and `node generate_epub.js`.

## 7. Build Commands
- **Regenerate PDFs/HTMLs:** `node generate_static_files.js`
- **Regenerate EPUB:** `node generate_epub.js`
- **Full Refresh:** Run both scripts.
