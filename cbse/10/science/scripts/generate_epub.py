import json
import os
import subprocess

def block_to_markdown(block):
    if block['type'] == 'heading':
        return f"{ '#' * (block['level']+1)} {block['content']}\n\n"
    elif block['type'] == 'text':
        return f"{block['content']}\n\n"
    elif block['type'] == 'list':
        md = ""
        for item in block['items']:
            md += f"- {item}\n"
        return md + "\n"
    elif block['type'] == 'activity':
        md = f"> **{block['title']}**\n>\n"
        md += f"> {block['content']}\n"
        if 'warning' in block:
            md += f">\n> *CAUTION: {block['warning']}*\n"
        return md + "\n"
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
            
        temp_md_file = f"temp_epub_{lesson['id']}.md"
        with open(temp_md_file, 'w', encoding='utf-8') as f:
            f.write(md_content)
            
        output_file = os.path.join(output_dir, f"{lesson['id']}.epub")
        
        cmd = [
            'pandoc',
            temp_md_file,
            '-o',
            output_file,
            '--toc',
            '--webtex',
            '--metadata',
            f"title={lesson['title']}",
            '--metadata',
            "lang=en"
        ]
        
        try:
            subprocess.run(cmd, check=True)
            print(f"Saved to {output_file}")
        except Exception as e:
            print(f"EPUB failed: {e}")
        finally:
            if os.path.exists(temp_md_file):
                os.remove(temp_md_file)

if __name__ == "__main__":
    main()
