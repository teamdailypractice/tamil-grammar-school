# Project Blueprint: CBSE Class 10 Science Platform

This document outlines the architecture and workflows for processing CBSE Science chapters into interactive web lessons and offline downloads (PDF/EPUB).

## 1. Tech Stack & Dependencies
- **Frontend**: Next.js 14 (App Router), TypeScript, Tailwind CSS.
- **Math Rendering**: KaTeX with `mhchem` extension (Web and PDF).
- **Offline Engines**: 
  - **PDF**: WeasyPrint + KaTeX Pre-rendering.
  - **EPUB**: Pandoc + WebTeX (Equation-to-Image conversion).

## 2. Core Data Interface (`src/data/lessons.ts`)
Every lesson entry must provide:
- `id`: unique string (e.g., `chem-01`).
- `subject`: 'Chemistry' | 'Physics' | 'Biology'.
- `title`: Chapter title.
- `chapterNumber`: integer.
- `content`: Array of `ContentBlock` (heading, text, list, activity).
- `summary`: Array of strings ("What you have learnt").
- `formulae`: Array of LaTeX strings (dedicated revision page).
- `flashcards`: Array of {id, front, back} objects.
- `quiz`: Array of {id, question, options, correctAnswer, explanation}.
- `exercises`: Array of strings (End-of-chapter questions).

## 3. Automation Pipeline

### Step A: Data Integration
- **Source**: `scripts/update_lesson_data.py`
- **Action**: Populates `src/data/lessons.ts`. 
- **Rule**: Use `$$\ce{...}$$` for chemical equations and `$...$` for inline math.

### Step B: JSON Bridge
- **Command**: `npx tsx scripts/export_data.ts`
- **Output**: `scripts/lessons.json` (Consumed by Python generators).

### Step C: PDF Generation
- **Script**: `scripts/generate_pdf.py`
- **Mechanism**: Calls `scripts/render_math.js` (Node) to pre-render KaTeX to HTML strings, then uses WeasyPrint to generate a paginated A4 PDF with bookmarks.

### Step D: EPUB Generation
- **Script**: `scripts/generate_epub.py`
- **Mechanism**: Uses Pandoc with `--webtex` to convert Markdown to a reflowable EPUB with embedded math images.

## 4. Workflow for New Chapters
1. Extract text: `pdftotext book/new-file.pdf scripts/temp_text.txt`.
2. Map content to the `get_content()`, `get_quiz()`, etc., functions in `scripts/update_lesson_data.py`.
3. Run the build chain:
   ```bash
   python3 scripts/update_lesson_data.py
   npx tsx scripts/export_data.ts
   python3 scripts/generate_pdf.py
   python3 scripts/generate_epub.py
   ```
4. Start dev server to verify: `npm run dev`.
