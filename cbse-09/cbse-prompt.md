### Role & Objective

You are tasked with creating an **interactive, trackable Biology learning experience in English** for **9th grade students**, based on the content of a provided PDF textbook.

The final output must function as a **self-paced digital textbook**, with progress tracking, quizzes, exam mode, and offline access.

---

## 1. Content Extraction Rules (Strict)

1. **All topics in the PDF must be covered.**
2. **No topic may be skipped or merged.**
3. Topics must appear in the **exact same order** as in the PDF.
4. **All images in the PDF must be extracted and included**:

   * Download images in **good quality**
   * Each image must appear near the relevant content
   * Provide a **clear description/explanation** for every image
5. **QR codes must be ignored and excluded** entirely.

---

## 2. Article Structure & Learning Flow

6. Create a **new, original article** based on the extracted content (do not copy PDF layout verbatim).
7. Present the content as a **multi-stage guided learning experience**.
8. For **each topic**:

   * Split the topic into **25 sequential learning stages**
   * Each stage should represent a **small, digestible unit of learning**
9. Ensure the experience is:

   * Step-by-step
   * Clean and readable
   * Easy for 9th-grade students to understand
10. Display a **visible progress bar** indicating:

    * Current stage
    * Completed stages
    * Overall topic progress

---

## 3. Technology & Implementation Requirements

11. Implement the learning experience using:

    * **HTML**
    * **CSS**
    * **JavaScript**
12. Use browser-based storage (**localStorage or IndexedDB**) to:

    * Save student progress
    * Track completed stages
    * Restore progress when the student revisits the page

---

## 4. Quiz System – Practice Mode

13. For **each topic**, create **5 quiz questions**.
14. Quiz behavior:

    * Each time the article is opened:

      * Questions must be **randomly selected**
      * Answer options must be **randomly shuffled**
15. Quiz data handling:

    * All quiz questions and answers must be stored in a **separate JSON file**
    * Correct answers **must not be hard-coded** in HTML or JavaScript
    * JavaScript should dynamically load and evaluate quizzes from JSON

---

## 5. Exam Mode

16. Create a **separate Exam Page (HTML)** with the following rules:

    * Questions sourced from the **same quiz JSON file**
    * **50 questions total**
    * **20-minute time limit**
    * Answer options shuffled on every attempt
17. Include a **clearly visible link** to the Exam Page from the main article.

---

## 6. Engagement, Feedback & Motivation

18. Provide positive feedback and celebration when students:

    * Complete an individual stage
    * Complete a topic
    * Reach major milestones
19. The learning experience should feel:

    * Enjoyable
    * Motivating
    * Visually rewarding
    * Suitable for independent, self-paced study

---

## 7. Experience Benchmark

20. The final experience should resemble:

    * **Gemini Storybook–style guided content**
    * **Livebook-style step-by-step learning**
    * Modern **interactive digital textbooks with progress tracking**

---

## 8. Offline & Downloadable Access

21. The full article content must be available for **offline download** in the following formats:

    * PDF
    * Google Slides
    * Reveal.js slides
22. All quiz questions (including correct answers) must be downloadable as **one consolidated document** in:

    * PDF
    * Google Slides
    * Reveal.js slides
23. Create a **separate Download Page (HTML)** where students can:

    * Download the article in all supported formats
    * Download the quiz content in all supported formats

---

## 9. Quality Expectations

24. Language must be:

    * Age-appropriate for 9th grade
    * Clear and instructional
    * Free of unnecessary jargon
25. The solution must be:

    * Modular
    * Maintainable
    * Easy to extend with new chapters or subjects later

---

## Source PDF File

The book pdf is available in:  ./ncert-09-science-book/iesc105-biology-01.pdf


## Later added

the user should be able to see the list of  topics and should be able to navigate to the specific topic