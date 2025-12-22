# CBSE Class 10 Science - Interactive Learning Platform

An interactive educational website built with Next.js 14, designed for CBSE Class 10 Science students.

## Features

*   **Subject Dashboard**: Navigate through Chemistry, Physics, and Biology chapters.
*   **Interactive Lessons**: Read lessons with structured content, images, and activities.
*   **Quizzes**: Test your knowledge with immediate feedback and explanation.
*   **Flashcards**: Revise key concepts with flip-cards.
*   **Progress Tracking**: Automatically saves your progress and quiz scores (local storage).
*   **Offline Support**: Download high-quality PDFs of lessons.

## Getting Started

1.  **Install Dependencies**:
    ```bash
    npm install
    ```

2.  **Run Development Server**:
    ```bash
    npm run dev
    ```
    Open [http://localhost:3000](http://localhost:3000) in your browser.

## Data & Content Management

The lesson content is stored in `src/data/lessons.ts`.

### Generating Offline PDFs & EPUBs

To generate the downloadable files (stored in `public/downloads/`), follow these steps:

1.  **Export Data to JSON**:
    ```bash
    npx tsx scripts/export_data.ts
    ```
    This creates `scripts/lessons.json`.

2.  **Generate PDFs**:
    ```bash
    python3 scripts/generate_pdf.py
    ```
    *Note: Requires `weasyprint` python library.*

3.  **Generate EPUBs**:
    ```bash
    python3 scripts/generate_epub.py
    ```
    *Note: Requires `pandoc` to be installed.*

## Project Structure

*   `src/app`: Next.js App Router pages.
*   `src/components`: React components (Quiz, Flashcards, etc.).
*   `src/data`: Content source.
*   `public/images`: Extracted lesson images.
*   `scripts`: Utilities for data export and PDF generation.

## License

Private
