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

let markdownContent = `---
title: Science 9th (Notes and Quiz) - NCERT - 2024-2025
author: Interactive Learning Series
rights: Creative Commons Attribution
language: en-US
...

# Preface

This e-book contains the complete interactive lessons and question banks for Class 9 Science.

`;

chapters.forEach(chapter => {
    // 1. Add Lesson Content
    const topicsFile = `src/topics-${chapter.id}.json`;
    if (fs.existsSync(topicsFile)) {
        const data = JSON.parse(fs.readFileSync(topicsFile, 'utf8'));
        
        markdownContent += `# ${chapter.title}\n\n`;
        
        data.topics.forEach(topic => {
            markdownContent += `## ${topic.title}\n\n`;
            topic.stages.forEach(stage => {
                if (stage.type === 'text') {
                    if (stage.heading) {
                        markdownContent += `### ${stage.heading}\n\n`;
                    }
                    markdownContent += `${stage.content}\n\n`;
                }
            });
        });
    }

    // 2. Add Quiz Content for this Chapter
    const quizFile = `src/quiz-${chapter.id}.json`;
    if (fs.existsSync(quizFile)) {
        const data = JSON.parse(fs.readFileSync(quizFile, 'utf8'));
        
        markdownContent += `## Practice Questions\n\n`;
        
        data.topics.forEach(topic => {
            markdownContent += `### ${topic.title} (Quiz)\n\n`;
            topic.questions.forEach((q, i) => {
                markdownContent += `**${i + 1}. ${q.question}**\n\n`;
                // List options as a bulleted list
                q.options.forEach(opt => {
                    markdownContent += `- ${opt}\n`;
                });
                markdownContent += `\n*Answer: ${q.answer}*\n\n---\n\n`;
            });
        });
    }
    
    // Add a page break between chapters (Pandoc handles this for EPUBs)
    markdownContent += `\n\n`; 
});

// Write Markdown file
const mdFile = 'src/science-class9-complete.md';
fs.writeFileSync(mdFile, markdownContent);
console.log(`Generated Markdown: ${mdFile}`);

// Convert to EPUB using Pandoc
try {
    console.log('Generating EPUB...');
    // --toc generates a Table of Contents based on headers
    // --metadata sets the cover info
    execSync(`pandoc ${mdFile} -o src/science-class9-complete.epub --toc --toc-depth=2`);
    console.log('Success: src/science-class9-complete.epub');
} catch (error) {
    console.error('Error running pandoc:', error.message);
}
