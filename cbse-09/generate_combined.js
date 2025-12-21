const fs = require('fs');
const { execSync } = require('child_process');

const chapters = [
    { id: 'ch1', title: 'Chapter 1: Matter in Our Surroundings' },
    { id: 'ch2', title: 'Chapter 2: Is Matter Around Us Pure?' },
    { id: 'ch3', title: 'Chapter 3: Atoms and Molecules' },
    { id: 'ch4', title: 'Chapter 4: Structure of the Atom' },
    { id: 'ch5', title: 'Chapter 5: The Fundamental Unit of Life' },
    { id: 'ch6', title: 'Chapter 6: Tissues' },
    { id: 'ch7', title: 'Chapter 7: Motion' },
    { id: 'ch8', title: 'Chapter 8: Force and Laws of Motion' },
    { id: 'ch9', title: 'Chapter 9: Gravitation' },
    { id: 'ch10', title: 'Chapter 10: Work and Energy' },
    { id: 'ch11', title: 'Chapter 11: Sound' },
    { id: 'ch12', title: 'Chapter 12: Improvement in Food Resources' }
];

// Shared CSS for print styling
const css = `
    <style>
        @page { size: A4; margin: 2cm; }
        body { font-family: sans-serif; line-height: 1.6; color: #333; }
        
        /* Cover Page */
        .cover { text-align: center; margin-top: 30%; page-break-after: always; }
        .cover h1 { font-size: 3em; color: #2c3e50; margin-bottom: 0.5em; }
        .cover h2 { font-size: 1.8em; color: #7f8c8d; font-weight: normal; }
        
        /* Table of Contents */
        .toc { page-break-after: always; }
        .toc h1 { color: #2c3e50; border-bottom: 2px solid #2c3e50; padding-bottom: 10px; }
        .toc-item { margin-bottom: 10px; }
        .toc-item a { 
            text-decoration: none; 
            color: #333; 
            font-size: 1.1em; 
            display: flex; 
            justify-content: space-between; 
            border-bottom: 1px dotted #ccc;
        }
        .toc-item a::after { content: target-counter(attr(href), page); } /* WeasyPrint Magic: Adds page numbers! */
        
        /* Content */
        h1 { color: #2c3e50; border-bottom: 2px solid #eee; padding-bottom: 10px; margin-top: 3em; string-set: chapter content(); }
        h2 { color: #27ae60; margin-top: 2em; }
        h3 { color: #2980b9; margin-top: 1.5em; }
        p { margin-bottom: 1em; text-align: justify; }
        
        /* Bookmarks */
        h1 { bookmark-level: 1; bookmark-label: content(); }
        h2 { bookmark-level: 2; bookmark-label: content(); }
        
        /* Footer with page numbers */
        @page {
            @bottom-center {
                content: counter(page);
            }
        }
    </style>
`;

// --- 1. Generate Combined Textbook HTML ---
let masterArticleHtml = `<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Class 9 Science Textbook</title>${css}</head><body>`;

// Cover
masterArticleHtml += `
    <div class="cover">
        <h1>Class 9 Science</h1>
        <h2>Complete Interactive Textbook</h2>
    </div>
`;

// Table of Contents
masterArticleHtml += `
    <div class="toc">
        <h1>Table of Contents</h1>
        <div class="toc-item"><a href="#definitions">Definitions & Formulae</a></div>
        ${chapters.map(ch => `
            <div class="toc-item">
                <a href="#${ch.id}">${ch.title}</a>
            </div>
        `).join('')}
    </div>
`;

// 1.5 Add Definitions/Flashcards Section
const flashcardsData = JSON.parse(fs.readFileSync('src/flashcards.json', 'utf8'));
masterArticleHtml += `<h1 id="definitions">Definitions & Formulae</h1>`;
for (const subject in flashcardsData.subjects) {
    masterArticleHtml += `<h2>${subject}</h2>`;
    flashcardsData.subjects[subject].forEach(card => {
        masterArticleHtml += `
            <div style="margin-bottom: 15px; border-bottom: 1px solid #f0f0f0; padding-bottom: 5px;">
                <strong style="color: #2e7d32;">${card.term}:</strong> ${card.definition}
            </div>
        `;
    });
}

// Content
chapters.forEach(chapter => {
    const topicsFile = `src/topics-${chapter.id}.json`;
    if (fs.existsSync(topicsFile)) {
        const data = JSON.parse(fs.readFileSync(topicsFile, 'utf8'));
        // Use id for TOC linking
        masterArticleHtml += `<h1 id="${chapter.id}">${chapter.title}</h1>`;
        
        data.topics.forEach(topic => {
            masterArticleHtml += `<h2>${topic.title}</h2>`;
            topic.stages.forEach(stage => {
                if (stage.type === 'text') {
                    if (stage.heading) masterArticleHtml += `<h3>${stage.heading}</h3>`;
                    masterArticleHtml += `<p>${stage.content}</p>`;
                }
            });
        });
    }
});

masterArticleHtml += `</body></html>`;
fs.writeFileSync('src/science-class9-complete.html', masterArticleHtml);


// --- 2. Generate Combined Quiz HTML ---
let masterQuizHtml = `<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Class 9 Science Question Bank</title>${css}</head><body>`;

// Cover
masterQuizHtml += `
    <div class="cover">
        <h1>Class 9 Science</h1>
        <h2>Complete Question Bank (with Answers)</h2>
    </div>
`;

// Table of Contents
masterQuizHtml += `
    <div class="toc">
        <h1>Table of Contents</h1>
        ${chapters.map(ch => `
            <div class="toc-item">
                <a href="#${ch.id}">${ch.title}</a>
            </div>
        `).join('')}
    </div>
`;

// Content
chapters.forEach(chapter => {
    const quizFile = `src/quiz-${chapter.id}.json`;
    if (fs.existsSync(quizFile)) {
        const data = JSON.parse(fs.readFileSync(quizFile, 'utf8'));
        masterQuizHtml += `<h1 id="${chapter.id}">${chapter.title}</h1>`;
        
        data.topics.forEach(topic => {
            masterQuizHtml += `<h2>${topic.title}</h2>`;
            topic.questions.forEach((q, i) => {
                masterQuizHtml += `
                    <div style="background: #f9f9f9; padding: 10px; margin-bottom: 10px; border-radius: 5px; page-break-inside: avoid;">
                        <div style="font-weight: bold;">${i + 1}. ${q.question}</div>
                        <ul style="list-style: none; padding-left: 10px; margin: 5px 0;">
                            ${q.options.map(opt => `<li>○ ${opt}</li>`).join('')}
                        </ul>
                        <div style="color: green; font-weight: bold; margin-top: 5px;">Answer: ${q.answer}</div>
                    </div>
                `;
            });
        });
    }
});

masterQuizHtml += `</body></html>`;
fs.writeFileSync('src/science-class9-quiz-complete.html', masterQuizHtml);


// --- 3. Convert to PDF using WeasyPrint ---
try {
    console.log('Generating Combined Textbook PDF with WeasyPrint...');
    execSync('weasyprint src/science-class9-complete.html src/science-class9-textbook-complete.pdf');
    
    console.log('Generating Combined Quiz PDF with WeasyPrint...');
    execSync('weasyprint src/science-class9-quiz-complete.html src/science-class9-quiz-complete.pdf');
    
    console.log('Success! PDFs generated with bookmarks and correct links.');
} catch (error) {
    console.error('PDF Generation Error:', error.message);
}