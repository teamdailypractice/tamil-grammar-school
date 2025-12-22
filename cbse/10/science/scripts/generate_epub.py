import json
import os
import subprocess

def block_to_markdown(block):
    if block['type'] == 'heading':
        return f"{ '#' * block['level']} {block['content']}\n\n"
    elif block['type'] == 'text':
        return f"{block['content']}\n\n"
    elif block['type'] == 'list':
        md = ""
        for item in block['items']:
            md += f"- {item}\n"
        return md + "\n"
    elif block['type'] == 'activity':
        md = "::: {{.activity style='background: #fffbeb; border-left: 5px solid #f59e0b; padding: 1em; margin: 1em 0;'}}\n"
        md += f"**{block['title']}**\n\n"
        md += f"{block['content']}\n\n"
        if 'warning' in block:
            md += f"*CAUTION: {block['warning']}*\n"
        md += ":::\n\n"
        return md
    return ""

def main():
    json_path = os.path.join(os.getcwd(), 'scripts', 'lessons.json')
    output_dir = os.path.join(os.getcwd(), 'public', 'downloads')
    
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    for lesson in lessons:
        print(f"Generating EPUB for {lesson['id']}...")
        
        md_content = f"% {lesson['title']}\n"
        md_content += f"% Chapter {lesson['chapterNumber']} - {lesson['subject']}\n\n"
        
        for block in lesson['content']:
            md_content += block_to_markdown(block)
            
        temp_md_file = f"temp_{lesson['id']}.md"
        with open(temp_md_file, 'w', encoding='utf-8') as f:
            f.write(md_content)
            
        output_file = os.path.join(output_dir, f"{lesson['id']}.epub")
        
        # For EPUB, --webtex is very robust as it converts math to images
        # that work on almost all e-readers.
        cmd = [
            'pandoc',
            temp_md_file,
            '-o',
            output_file,
            '--toc',
            '--webtex', # Most compatible math for EPUB
            '--metadata', f"title={lesson['title']}",
            '--metadata', "lang=en"
        ]
        
        try:
            subprocess.run(cmd, check=True)
            print(f"Saved to {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error running pandoc: {e}")
        finally:
            if os.path.exists(temp_md_file):
                os.remove(temp_md_file)

if __name__ == "__main__":
    main()