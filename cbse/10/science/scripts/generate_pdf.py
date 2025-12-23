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
        return f"<h{block['level']+1}>{block['content']}</h{block['level']+1}>
"
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
        print(f"Error: {json_path} not found.")
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
    }
    body { 
        font-family: sans-serif; 
        line-height: 1.6; 
        color: #1f2937; 
    }
    """

    for lesson in lessons:
        print(f"Generating PDF for {lesson['id']}...")
        
        html_body = f"<h1>{lesson['title']}</h1>"
        html_body += f"<h2>Chapter {lesson['chapterNumber']} - {lesson['subject']}</h2>"
        for block in lesson['content']:
            html_body += block_to_html(block)
            
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
