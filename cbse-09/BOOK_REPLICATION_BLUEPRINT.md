# Book Replication Blueprint: Interactive Learning Platform

This document serves as a master specification and prompt history summary to replicate or extend this interactive textbook platform for other subjects or classes.

## 1. Core Development Prompts Summary

The following logic was developed through a series of iterative prompts:

1.  **Phase 1: Foundation**: "Create a static-first web application for Class 9 Science. Use JSON files to store lesson content and quizzes. Implement a dashboard to select chapters."
2.  **Phase 2: Interactive Lessons**: "Develop an `app.js` that renders lessons stage-by-stage (text and quick quizzes). Use `localStorage` to save progress within a chapter."
3.  **Phase 3: Study Tools**: "Add a 'Track Progress' page showing % completion and quiz scores across all chapters. Create a 'Flashcards' tool and an 'Exam Mode' with practice and timed (20 min) options."
4.  **Phase 4: Global UX**: "Implement a consistent navigation menu (`navbar.js`) across all pages. Ensure the 'Chapter Home' link dynamically points to the last visited chapter."
5.  **Phase 5: State Persistence Fix**: "Fix the bug where navigating from Progress back to Chapter Home resets to Chapter 1. Use `localStorage` to persist the 'last-active-chapter' globally."
6.  **Phase 6: Mobile Optimization**: "Optimize the navigation bar for mobile. Instead of wrapping to multiple rows, use a single-row horizontal scroll with touch-friendly tab styling."

## 2. Technical Architecture

### Tech Stack
- **Structure**: Vanilla HTML/JS/CSS (Static).
- **State**: `localStorage` (Keys: `biology-ch[ID]-progress`, `biology-last-chapter`).
- **Data**: External JSON for Topics and Quizzes.

### File Schema Requirements

#### `topics-ch[ID].json`
```json
{
  "topics": [
    {
      "title": "Topic Name",
      "stages": [
        { "type": "text", "heading": "Sub-heading", "content": "Markdown-style text" },
        { "type": "quiz", "heading": "Knowledge Check" }
      ]
    }
  ]
}
```

#### `quiz-ch[ID].json`
```json
{
  "topics": [
    {
      "title": "Topic Name",
      "questions": [
        {
          "question": "What is...?",
          "options": ["A", "B", "C", "D"],
          "answer": "A"
        }
      ]
    }
  ]
}
```

## 3. Key UX Patterns to Replicate

- **Context-Aware Navigation**: The navbar must always know which chapter the user is "in." This is achieved by checking `URLSearchParams`, then `body[data-chapter]`, and finally `localStorage['last-chapter']`.
- **Progress Estimation**: Calculate % completion based on the current `topicIndex` and `stageIndex` relative to the total counts stored in the chapter's metadata JSON.
- **Mobile-First Menu**:
    ```css
    nav {
        flex-wrap: nowrap;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
    }
    ```
- **Exam Engine**: Logic to shuffle questions from the JSON bank, slice for a 50-question limit, and implement a countdown timer.

## 4. Master Prompt for New Book Preparation

> "I want to create an interactive textbook for [SUBJECT/CLASS]. Use a JSON-driven architecture where content is separated from the UI. Implement a stage-by-stage lesson renderer, a progress tracking dashboard using localStorage, and a study suite including flashcards and a timed exam mode. Ensure the UI is mobile-optimized with a horizontal-scrolling navigation bar and that the user's chapter context is persisted globally across all pages so they never lose their place."

---
*Generated based on CBSE-09 Science Platform development history.*
