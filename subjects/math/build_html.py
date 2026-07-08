#!/usr/bin/env python3
"""Convert lesson .md to .html with proper template."""
import re, sys, os

def md_to_html(md_path, html_path, lesson_num, title):
    with open(md_path, 'r') as f:
        md = f.read()
    
    lines = md.split('\n')
    out = []
    in_math_block = False
    in_list = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Skip the very first # heading
        if line.startswith('# ') and not any(x.startswith('<h') for x in out):
            i += 1
            continue
        
        # Code blocks
        if line.startswith('```'):
            i += 1
            continue
        
        # Math blocks $$
        if line.startswith('$$'):
            if not in_math_block:
                out.append('<div class="math-block">$$')
                in_math_block = True
            else:
                out.append('$$</div>')
                in_math_block = False
            i += 1
            continue
        
        # Headings
        if line.startswith('### '):
            text = line[4:]
            if in_list:
                out.append('</ul>')
                in_list = False
            out.append(f'<h3>{text}</h3>')
        elif line.startswith('## '):
            text = line[3:]
            if in_list:
                out.append('</ul>')
                in_list = False
            out.append(f'<h2>{text}</h2>')
        elif line.startswith('# '):
            text = line[2:]
            if in_list:
                out.append('</ul>')
                in_list = False
            out.append(f'<h1>{text}</h1>')
        
        # List items
        elif line.startswith('- '):
            if not in_list:
                out.append('<ul>')
                in_list = True
            text = line[2:]
            out.append(f'<li>{text}</li>')
        
        # Blockquotes
        elif line.startswith('> '):
            if in_list:
                out.append('</ul>')
                in_list = False
            text = line[2:]
            out.append(f'<blockquote><p>{text}</p></blockquote>')
        
        # Horizontal rules
        elif line.strip() == '---':
            if in_list:
                out.append('</ul>')
                in_list = False
            out.append('<hr>')
        
        # Empty lines
        elif line.strip() == '':
            if in_list:
                out.append('</ul>')
                in_list = False
            out.append('')
        
        # Regular paragraph
        else:
            if in_list:
                out.append('</ul>')
                in_list = False
            processed = line
            # bold: **...**
            processed = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', processed)
            if processed.strip():
                out.append(f'<p>{processed}</p>')
            else:
                out.append('')
        
        i += 1
    
    if in_list:
        out.append('</ul>')
    
    body = '\n'.join(out)
    
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lesson {lesson_num} — {title}</title>
<script>MathJax={{tex:{{inlineMath:[['$','$']],displayMath:[['$$','$$']]}}}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>
<style>body{{max-width:800px;margin:40px auto;font-family:'Times New Roman',Georgia,serif;font-size:17px;line-height:1.7;padding:0 20px;color:#1a1a1a;}}h1{{font-size:22px;border-bottom:2px solid #333;padding-bottom:8px;margin-top:36px;}}h2{{font-size:19px;margin-top:28px;color:#2c3e50;}}h3{{font-size:17px;margin-top:22px;color:#444;}}p{{margin:0.6em 0;}}li{{margin:0.3em 0 0.3em 20px;}}.math-block{{text-align:center;margin:1em 0;overflow-x:auto;}}b{{color:#222;}}.nav{{text-align:center;margin:30px 0;font-size:14px;}}.nav a{{margin:0 8px;color:#3498db;text-decoration:none;}}blockquote{{border-left:3px solid #ccc;margin:0.8em 0;padding-left:16px;color:#555;}}hr{{border:none;border-top:1px solid #ddd;margin:24px 0;}}</style></head><body>
<div class="nav"><a href="index.html">← Back to Index</a></div>

{body}

<div class="nav"><a href="index.html">← Back to Index</a></div>
</body></html>'''
    
    with open(html_path, 'w') as f:
        f.write(html)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: build_html.py md_path html_path title")
        sys.exit(1)
    lesson_num = os.path.basename(sys.argv[1]).replace('lesson','').replace('.md','')
    md_to_html(sys.argv[1], sys.argv[2], lesson_num, sys.argv[3])
