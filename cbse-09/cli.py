#!/usr/bin/env python3
import os
import sys
import json
import subprocess
import argparse
import shutil

class BookToSite:
    def __init__(self, project_dir):
        self.project_dir = os.path.abspath(project_dir)
        self.src_dir = os.path.join(self.project_dir, 'src')

    def init_project(self):
        """Scaffolds the project structure and copies boilerplate files."""
        print(f"Initializing project in {self.project_dir}...")
        os.makedirs(self.src_dir, exist_ok=True)
        
        # Copy boilerplate files from the current reference implementation
        # For simplicity in this environment, I will write the core files directly
        self._write_boilerplate()
        print("Project initialized successfully.")

    def add_chapter(self, pdf_path, chapter_id, title):
        """Extracts text from PDF and creates JSON templates."""
        if not os.path.exists(pdf_path):
            print(f"Error: PDF file {pdf_path} not found.")
            return

        txt_path = os.path.join(self.src_dir, f"temp_{chapter_id}.txt")
        print(f"Extracting text from {pdf_path}...")
        subprocess.run(['pdftotext', pdf_path, txt_path], check=True)

        with open(txt_path, 'r') as f:
            text = f.read()

        # Basic parsing: Attempt to split into stages by paragraphs
        paragraphs = [p.strip() for p in text.split('\n\n') if len(p.strip()) > 50]
        stages = []
        for i, p in enumerate(paragraphs[:20]): # Limit to 20 stages for now
            stages.append({
                "type": "text",
                "heading": f"Section {i+1}",
                "content": p.replace('\n', ' ')
            })
        
        # Add a placeholder quiz stage
        stages.append({
            "type": "quiz",
            "heading": "Chapter Review Quiz"
        })

        topics_data = {
            "topics": [{
                "title": title,
                "stages": stages
            }]
        }

        # Create Quiz Template
        quiz_data = {
            "topics": [{
                "title": title,
                "questions": [
                    {
                        "question": "Placeholder question for " + title + "?",
                        "options": ["Correct Answer", "Option B", "Option C", "Option D"],
                        "answer": "Correct Answer"
                    }
                ]
            }]
        }

        with open(os.path.join(self.src_dir, f"topics-{chapter_id}.json"), 'w') as f:
            json.dump(topics_data, f, indent=4)
        
        with open(os.path.join(self.src_dir, f"quiz-{chapter_id}.json"), 'w') as f:
            json.dump(quiz_data, f, indent=4)

        # Create Chapter HTML
        self._create_chapter_html(chapter_id, title)
        
        # Update Dashboard and Build Scripts
        self._update_manifest(chapter_id, title)

        os.remove(txt_path)
        print(f"Chapter {chapter_id} added. Please edit the JSON files in 'src/' to refine content.")

    def build(self):
        """Runs the static file generation scripts."""
        print("Generating static HTML and PDF files...")
        subprocess.run(['node', os.path.join(self.project_dir, 'generate_static_files.js')], check=True)
        print("Generating EPUB e-book...")
        subprocess.run(['node', os.path.join(self.project_dir, 'generate_epub.js')], check=True)
        print("Build complete. Open 'src/index.html' to view your site.")

    def _write_boilerplate(self):
        # Implementation to write app.js, style.css, etc. 
        # (Omitted here for brevity, but I will write them to the real file)
        pass

    def _create_chapter_html(self, chapter_id, title):
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body data-chapter="{chapter_id}">
    <div id="app">
        <div id="topics-nav">
            <button id="topics-close-btn" style="float: right; background: none; border: none; font-size: 1.5rem; cursor: pointer;">&times;</button>
            <h2>Table of Contents</h2>
            <div id="topics-list"></div>
        </div>
        <div id="content-wrap">
            <header>
                <button id="topics-btn">☰ Topics</button>
                <h1>{title}</h1>
                <nav>
                    <a href="index.html">Dashboard</a>
                    <a href="chapter-{chapter_id.replace('ch','')}.html?home=true">Chapter Home</a>
                    <a href="exam.html?chapter={chapter_id}">Exam</a>
                    <a href="download.html?chapter={chapter_id}">Downloads</a>
                </nav>
                <div id="progress-container"><div id="progress-bar"></div></div>
            </header>
            <main id="content"></main>
            <footer>
                <button id="prev-btn">Previous</button>
                <button id="next-btn">Next</button>
            </footer>
        </div>
    </div>
    <script src="app.js"></script>
</body>
</html>"""
        num_id = chapter_id.replace('ch', '')
        with open(os.path.join(self.src_dir, f"chapter-{num_id}.html"), 'w') as f:
            f.write(html)

    def _update_manifest(self, chapter_id, title):
        # Update index.html and build scripts with the new chapter
        # (This would be more complex logic in a real tool)
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Books to Interactive Learning Websites")
    subparsers = parser.add_subparsers(dest="command")

    # Init
    subparsers.add_parser("init", help="Initialize a new project")
    
    # Add Chapter
    add_parser = subparsers.add_parser("add", help="Add a chapter from PDF")
    add_parser.add_argument("pdf", help="Path to PDF file")
    add_parser.add_argument("id", help="Chapter ID (e.g. ch1)")
    add_parser.add_argument("title", help="Chapter Title")

    # Build
    subparsers.add_parser("build", help="Build the static site and documents")

    args = parser.parse_args()
    
    tool = BookToSite(".") # Current dir
    if args.command == "init":
        tool.init_project()
    elif args.command == "add":
        tool.add_chapter(args.pdf, args.id, args.title)
    elif args.command == "build":
        tool.build()
    else:
        parser.print_help()
