# Tamil Grammar

* To learn Tamil grammar step by step using Tamil Nadu school books
* For school students, easy to read, review and test themselves in mobile/computer
* For others who want to learn Tamil grammar, start from 6th std book / 5th and go step by step
* Prepare PPT/PDF/Slides/....
* **Prepare quiz to review the topics**
* The content is same as school text books. **Value add**
  * **Presentation in multiple formats**
  * **Practice Quiz for each of the topic based on the content generated using AI and review the quiz**

## What are needed

* Content from school books - pdf/epub/html?
* Starting with 10th std book

## What are the steps?

1. Is EPUB/HTML book available instead of PDF?
2. If yes, download it.
3. <https://www.tntextbooks.in/p/10th-books.html>
4. Extract the EPUB to a directory, so that all are html files and other files present
5. For each html, can it be converted to markdown?
6. Loop through all html in the directory and convert to markdown using pandoc command
7. Store in markdown directory.
8. Extract from each markdown, the content needed
9. Create new markdown files from the content
10. Use it to produce
  * PPT
  * PDF
  * Slides
  * Other formats
  * Quiz
11. **The main purpose is to produce Quiz for each of the lesson that could be used in mobile**
  * No login
  * No app installation
  * Browser alone should be sufficient

## commands

* command:  `python epub_to_markdown.py <input.epub> <output_directory>`

```cmd
python epub_to_markdown.py D:\git\tamil-grammar-school\temp\Class_10_Tamil_StateBoard.epub D:\git\tamil-grammar-school\temp\10-html
```
