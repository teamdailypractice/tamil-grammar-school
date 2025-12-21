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

chapters.forEach(chapter => {
    console.log(`Processing ${chapter.id}...`);
    
    const topicsFile = `src/topics-${chapter.id}.json`;
    const quizFile = `src/quiz-${chapter.id}.json`;
    
    if (!fs.existsSync(topicsFile) || !fs.existsSync(quizFile)) {
        console.error(`Missing files for ${chapter.id}`);
        return;
    }

    const topicsData = JSON.parse(fs.readFileSync(topicsFile, 'utf8'));
    const quizData = JSON.parse(fs.readFileSync(quizFile, 'utf8'));

    // --- Generate Article HTML ---
    let articleHtml = `
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Biology ${chapter.title}</title>
        <style>
            body { font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: 2rem auto; padding: 0 1rem; color: #333; }
            h1 { text-align: center; border-bottom: 2px solid #333; padding-bottom: 10px; }
            h2 { color: #4CAF50; border-bottom: 1px solid #ccc; margin-top: 2rem; }
            h3 { color: #555; margin-top: 1.5rem; }
            p { margin-bottom: 1rem; }
            @media print {
                body { max-width: 100%; }
                h1, h2, h3 { page-break-after: avoid; }
            }
        </style>
    </head>
    <body>
        <h1>${chapter.title}</h1>
    `;

    topicsData.topics.forEach(topic => {
        articleHtml += `<h2>${topic.title}</h2>`;
        topic.stages.forEach(stage => {
            if (stage.type === 'text') {
                if (stage.heading) {
                    articleHtml += `<h3>${stage.heading}</h3>`;
                }
                articleHtml += `<p>${stage.content}</p>`;
            }
        });
    });

    articleHtml += `</body></html>`;
    const articleOut = `src/biology-${chapter.id}-article.html`;
    fs.writeFileSync(articleOut, articleHtml);
    console.log(`Generated ${articleOut}`);

    // --- Generate Quiz HTML ---
    let quizHtml = `
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Biology ${chapter.title} Quiz</title>
        <style>
            body { font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: 2rem auto; padding: 0 1rem; color: #333; }
            h1 { text-align: center; border-bottom: 2px solid #333; padding-bottom: 10px; }
            h2 { color: #4CAF50; border-bottom: 1px solid #ccc; margin-top: 2rem; }
            .question-box { background: #f9f9f9; padding: 15px; margin-bottom: 15px; border-radius: 5px; border-left: 4px solid #4CAF50; page-break-inside: avoid; }
            .question { font-weight: bold; margin-bottom: 10px; }
            ul { list-style-type: none; padding-left: 0; }
            li { margin-bottom: 5px; }
            .answer { margin-top: 10px; font-weight: bold; color: green; }
        </style>
    </head>
    <body>
        <h1>${chapter.title} Quiz</h1>
    `;

    quizData.topics.forEach(topic => {
        quizHtml += `<h2>${topic.title}</h2>`;
        topic.questions.forEach((q, i) => {
            quizHtml += `
                <div class="question-box">
                    <div class="question">${i + 1}. ${q.question}</div>
                    <ul>
                        ${q.options.map(opt => `<li>○ ${opt}</li>`).join('')}
                    </ul>
                    <div class="answer">Answer: ${q.answer}</div>
                </div>
            `;
        });
    });

    quizHtml += `</body></html>`;
    const quizOut = `src/biology-${chapter.id}-quiz.html`;
    fs.writeFileSync(quizOut, quizHtml);
    console.log(`Generated ${quizOut}`);

    // --- Generate PDFs using wkhtmltopdf ---
    try {
        console.log(`Converting ${chapter.id} HTML to PDF...`);
        execSync(`wkhtmltopdf ${articleOut} src/biology-${chapter.id}-article.pdf`);
        execSync(`wkhtmltopdf ${quizOut} src/biology-${chapter.id}-quiz.pdf`);
        console.log(`Successfully generated PDFs for ${chapter.id}`);
    } catch (error) {
        console.error('Error generating PDFs. Make sure wkhtmltopdf is installed.', error);
    }
});
