# Interactive Biology Learning Application Development Steps

This document outlines the steps taken to create an interactive, trackable Biology learning experience for 9th-grade students, based on a provided PDF textbook.

## 1. Content Extraction

-   **Listed Directory Contents**: Confirmed the location of the source PDF (`iesc105-biology-01.pdf`) within the `ncert-09-science-book/` directory.
-   **Extracted Text**: Used `pdftotext` to extract textual content from `ncert-09-science-book/iesc105-biology-01.pdf` and saved it to `src/biology-chapter-1.txt`.
-   **Created Image Directory**: Created a dedicated directory `src/images/` to store extracted images.
-   **Extracted Images**: Utilized `pdfimages` to extract all images from the PDF, saving them as PNG files into `src/images/`.
-   **Counted Images**: Verified the number of extracted images.
-   **Removed Temporary Text File**: Deleted `src/biology-chapter-1.txt` after content extraction.

## 2. Application Scaffolding

-   **`index.html` Creation**: Created the main HTML file (`src/index.html`), establishing the basic structure of the learning application, including links to CSS and JavaScript files, a header with a title, a progress bar container, a main content area, and navigation buttons.
-   **`style.css` Creation**: Created the CSS stylesheet (`src/style.css`) to provide initial styling for the application's layout, progress bar, buttons, and content elements.
-   **`app.js` Creation**: Initiated the main JavaScript file (`src/app.js`) to manage the application's interactive logic.
-   **`quiz.json` Creation**: Created a JSON file (`src/quiz.json`) to store quiz questions and answers.

## 3. Core Learning Experience Implementation

-   **Topic and Stage Definition**: Defined the first topic, "The Fundamental Unit of Life," in `src/app.js` with 25 sequential learning stages. These stages incorporate both text content and references to extracted images (`images/-001.png`, `images/-053.png`).
-   **Quiz Integration**: Integrated logic within `app.js` to render quiz questions dynamically from `quiz.json` at a designated stage.
-   **Quiz Styling**: Added specific CSS rules to `src/style.css` to enhance the appearance and readability of quiz questions and answer options.
-   **Progress Tracking**: Implemented a visible progress bar in `index.html` and developed JavaScript logic in `app.js` to update it based on the current stage and overall progress.
-   **Navigation Controls**: Added "Previous" and "Next" buttons with corresponding JavaScript functions in `app.js` to navigate through learning stages and topics.
-   **Quiz Data Fetching**: Included asynchronous JavaScript code in `app.js` to fetch quiz data from `quiz.json` upon application load.

## 4. Quiz and Exam System

-   **Dummy Quiz Data**: Populated `src/quiz.json` with 5 sample quiz questions for the "Introduction to Cells" topic, including options and correct answers.
-   **Exam Page (`exam.html`)**: Created a dedicated HTML file (`src/exam.html`) for the exam mode, featuring a title, a timer display, and a content area for exam questions.
-   **Exam Logic (`exam.js`)**: Developed JavaScript logic in `src/exam.js` to:
    -   Fetch quiz data from `quiz.json`.
    -   Render exam questions (initially using the 5 questions from the first topic).
    -   Implement a 20-minute countdown timer.
    -   Handle exam submission and display the score.

## 5. Download Functionality

-   **Download Page (`download.html`)**: Created an HTML page (`src/download.html`) where users can access various download options.
-   **Download Logic (`download.js`)**: Developed JavaScript functions in `src/download.js` to simulate the download of article and quiz content in different formats (PDF, Google Slides, Reveal.js slides) by creating and downloading temporary text/HTML files.

## 6. Navigation and Project Cleanup

-   **Inter-page Navigation**: Added consistent navigation links (Home, Exam, Downloads) to the headers of `src/index.html`, `src/exam.html`, and `src/download.html`.
-   **Navigation Styling**: Applied CSS styling to the navigation links in `src/style.css` for better visual integration.
-   **Archiving (and Deletion)**: Created a `biology-learning-app.zip` archive of the `src` directory for potential distribution (and subsequently deleted it as per instructions).

This markdown file now serves as a comprehensive record of the development process.
