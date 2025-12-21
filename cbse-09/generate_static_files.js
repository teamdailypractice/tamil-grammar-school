const fs = require('fs');
const { execSync } = require('child_process');

const topicsData = JSON.parse(fs.readFileSync('src/topics.json', 'utf8'));
const quizData = JSON.parse(fs.readFileSync('src/quiz.json', 'utf8'));

// --- Generate Article HTML ---
let articleHtml = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Biology Chapter 5: The Fundamental Unit of Life</title>
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
    <h1>Chapter 5: The Fundamental Unit of Life</h1>
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
fs.writeFileSync('src/biology-article.html', articleHtml);
console.log('Generated src/biology-article.html');

// --- Generate Quiz HTML ---
let quizHtml = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Biology Chapter 5 Quiz</title>
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
    <h1>Chapter 5 Quiz: The Fundamental Unit of Life</h1>
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
fs.writeFileSync('src/biology-quiz.html', quizHtml);
console.log('Generated src/biology-quiz.html');

// --- Generate PDFs using wkhtmltopdf ---
try {
    console.log('Converting HTML to PDF...');
    execSync('wkhtmltopdf src/biology-article.html src/biology-article.pdf');
    execSync('wkhtmltopdf src/biology-quiz.html src/biology-quiz.pdf');
    console.log('Successfully generated src/biology-article.pdf and src/biology-quiz.pdf');
} catch (error) {
    console.error('Error generating PDFs. Make sure wkhtmltopdf is installed.', error);
}