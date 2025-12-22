import json
import os
import subprocess
import re

def render_math_to_html(tex, display_mode):
    try:
        result = subprocess.run(
            ['node', 'scripts/render_math.js', tex, str(display_mode).lower()],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Error rendering math: {e}")
        return tex

def block_to_html(block):
    if block['type'] == 'heading':
        return f"<h{block['level']+2}>{block['content']}</h{block['level']+2}>\n"
    elif block['type'] == 'text':
        text = block['content']
        text = re.sub(r'\$\$(.*?)\$\$', lambda m: f"<div class='math-display'>{render_math_to_html(m.group(1), True)}</div>", text, flags=re.DOTALL)
        text = re.sub(r'\$(.*?)\$', lambda m: render_math_to_html(m.group(1), False), text)
        return f"<p>{text.replace('\n', '<br>')}</p>\n"
    elif block['type'] == 'list':
        html = "<ul>\n"
        for item in block['items']:
            item_text = re.sub(r'\$(.*?)\$', lambda m: render_math_to_html(m.group(1), False), item)
            html += f"<li>{item_text}</li>\n"
        html += "</ul>\n"
        return html
    elif block['type'] == 'activity':
        content = block['content']
        content = re.sub(r'\$(.*?)\$', lambda m: render_math_to_html(m.group(1), False), content)
        html = f"<div class='activity'>\n"
        html += f"<h3>{block['title']}</h3>\n"
        html += f"<p>{content}</p>\n"
        if 'warning' in block:
            html += f"<div class='warning'><strong>CAUTION:</strong> {block['warning']}</div>\n"
        html += "</div>\n"
        return html
    return ""

def main():
    json_path = os.path.join(os.getcwd(), 'scripts', 'lessons.json')
    output_dir = os.path.join(os.getcwd(), 'public', 'downloads')
    
    if not os.path.exists(json_path):
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    katex_css_path = os.path.join(os.getcwd(), 'node_modules', 'katex', 'dist', 'katex.min.css')
    with open(katex_css_path, 'r') as kf:
        katex_css = kf.read()

    css_content = katex_css + """
    @page { 
        size: A4; 
        margin: 2.5cm; 
        @bottom-right { content: "Page " counter(page) " of " counter(pages); font-size: 9pt; color: #6b7280; } 
    }
    body { font-family: sans-serif; line-height: 1.6; color: #1f2937; }
    h1 { color: #111827; border-bottom: 2px solid #3b82f6; padding-bottom: 0.5rem; }
    h2 { color: #1e40af; border-bottom: 1px solid #e5e7eb; margin-top: 2rem; page-break-before: always; }
    h3 { color: #1e3a8a; margin-top: 1.5rem; }
    .activity { background-color: #fffbeb; border-left: 5px solid #f59e0b; padding: 1.5rem; margin: 1.5rem 0; border-radius: 0.5rem; }
    .math-display { text-align: center; margin: 1.5em 0; display: block; width: 100%; }
    .katex-html { white-space: nowrap; }
    .flashcard { border: 1px solid #e5e7eb; padding: 1rem; margin-bottom: 1rem; border-radius: 0.5rem; background: #f9fafb; }
    .flashcard-q { font-weight: bold; color: #3b82f6; margin-bottom: 0.5rem; }
    .formula-item { padding: 1rem; background: #f3f4f6; margin-bottom: 0.5rem; border-radius: 0.25rem; }
    """

    for lesson in lessons:
        print(f"Generating Comprehensive PDF for {lesson['id']}...")
        
        # 1. Title
        html_body = f"<h1>{lesson['title']}</h1>"
        html_body += f"<p>Chapter {lesson['chapterNumber']} - {lesson['subject']}</p>"
        
        # 2. Main Content
        html_body += "<h2>Lesson Content</h2>"
        for block in lesson['content']:
            html_body += block_to_html(block)
            
        # 3. Summary (What you have learnt)
        html_body += "<h2>What you have learnt</h2>"
        html_body += "<ul>"
        for item in lesson['summary']:
            html_body += f"<li>{item}</li>"
        html_body += "</ul>"
        
        # 4. Quick Revision (Formulae & Equations)
        html_body += "<h2>Quick Revision: Equations & Formulae</h2>"
        for item in lesson['formulae']:
            rendered = re.sub(r'\$\$(.*?)\$\$', lambda m: render_math_to_html(m.group(1), True), item, flags=re.DOTALL)
            html_body += f"<div class='formula-item'>{rendered}</div>"
            
        # 5. Flashcards
        html_body += "<h2>Flashcards</h2>"
        for card in lesson['flashcards']:
            html_body += f"<div class='flashcard'><div class='flashcard-q'>Q: {card['front']}</div><div>A: {card['back']}</div></div>"
            
        # 6. Exercises
        html_body += "<h2>Exercises</h2>"
        for item in lesson['exercises']:
            html_body += f"<p>{item.replace('\n', '<br>')}</p>"
            
        full_html = f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{css_content}</style></head><body>{html_body}</body></html>"
        output_file = os.path.join(output_dir, f"{lesson['id']}.pdf")
        
        try:
            from weasyprint import HTML
            HTML(string=full_html, base_url=os.getcwd()).write_pdf(output_file)
            print(f"Saved to {output_file}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()