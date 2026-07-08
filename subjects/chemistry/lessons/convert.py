#!/usr/bin/env python3
"""Convert lesson .md files to .html with MathJax support."""
import re, os

HTML_HEADER = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — IB Chemistry HL</title>
<script>window.MathJax = {{ loader: {{load: ['[tex]/mhchem']}}, tex: {{packages: {{'[+]': ['mhchem']}}}} }};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>
<style>
  :root {{ --bg: #fdfcf9; --text: #1a1a1a; --accent: #2c5f2d; --border: #d4c5a9; }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Palatino', 'Georgia', serif; background: var(--bg); color: var(--text); max-width: 820px; margin: 0 auto; padding: 2rem 1.5rem; font-size: 17px; line-height: 1.7; }}
  h1 {{ font-size: 1.7rem; color: var(--accent); margin-bottom: 0.5rem; }}
  h2 {{ font-size: 1.25rem; color: var(--accent); border-bottom: 2px solid var(--border); padding-bottom: 0.3rem; margin: 2rem 0 1rem; }}
  h3 {{ font-size: 1.1rem; color: #444; margin: 1.3rem 0 0.5rem; }}
  p, li {{ margin-bottom: 0.6rem; }}
  ul, ol {{ padding-left: 1.8rem; margin-bottom: 1rem; }}
  .worked {{ background: #f0f7f0; border-left: 4px solid #2c5f2d; padding: 1rem 1.2rem; margin: 1rem 0; border-radius: 0 6px 6px 0; }}
  .worked strong {{ color: #2c5f2d; }}
  .answer {{ background: #fefdf7; border: 1px solid var(--border); padding: 0.8rem 1.2rem; margin: 0.5rem 0; border-radius: 6px; }}
  .nav {{ display: flex; justify-content: space-between; margin: 3rem 0 1rem; padding-top: 1rem; border-top: 2px solid var(--border); font-size: 0.9rem; }}
  .nav a {{ color: #1a5c9e; text-decoration: none; }}
  .nav a:hover {{ text-decoration: underline; }}
  .definition {{ background: #fdf5e6; border-left: 4px solid #d4a017; padding: 0.6rem 1rem; margin: 0.8rem 0; border-radius: 0 6px 6px 0; }}
  table {{ border-collapse: collapse; margin: 0.8rem 0; width: 100%; }}
  th, td {{ border: 1px solid var(--border); padding: 0.4rem 0.6rem; text-align: left; }}
  th {{ background: #f0f0f0; }}
  @media print {{ body {{ font-size: 14px; }} .nav {{ display: none; }} }}
</style>
</head>
<body>
'''

HTML_FOOTER = '''
</body>
</html>'''

def md_to_html(md_text, lesson_num):
    """Convert markdown content to HTML body."""
    lines = md_text.split('\n')
    html_lines = []
    in_worked = False
    in_definition = False
    in_table = False
    in_list = False
    list_type = None  # 'ul' or 'ol'
    prev_blank = True
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Handle worked divs
        if line.strip().startswith('<div class="worked">'):
            in_worked = True
            html_lines.append('<div class="worked">')
            i += 1
            continue
        if line.strip() == '</div>' and in_worked:
            in_worked = False
            html_lines.append('</div>')
            i += 1
            continue
        if line.strip().startswith('<div class="definition">'):
            in_definition = True
            html_lines.append('<div class="definition">')
            i += 1
            continue
        if line.strip() == '</div>' and in_definition:
            in_definition = False
            html_lines.append('</div>')
            i += 1
            continue
            
        # Headers
        if line.startswith('# ') and not line.startswith('## '):
            # Don't output h1 since it's in the header template
            i += 1
            continue
        elif line.startswith('### '):
            text = line[4:]
            html_lines.append(f'<h3>{convert_inline(text)}</h3>')
            i += 1
            continue
        elif line.startswith('## '):
            text = line[3:]
            html_lines.append(f'<h2>{convert_inline(text)}</h2>')
            i += 1
            continue
        
        # Horizontal rules
        if line.strip() == '---':
            html_lines.append('<hr>')
            i += 1
            continue
        
        # Tables
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                html_lines.append('<table>')
            # Skip separator lines (containing ---)
            if re.match(r'^\|[\s\-:|]+\|$', line.strip()):
                i += 1
                continue
            cells = [c.strip() for c in line.strip().split('|')[1:-1]]
            is_header = all(c.startswith('**') and c.endswith('**') for c in cells if c)
            tag = 'th' if is_header else 'td'
            clean_cells = [c.strip('*').strip() for c in cells]
            html_lines.append('<tr>')
            for c in clean_cells:
                html_lines.append(f'<{tag}>{convert_inline(c)}</{tag}>')
            html_lines.append('</tr>')
            i += 1
            # Check if next line is still table
            if i < len(lines) and '|' in lines[i] and lines[i].strip().startswith('|'):
                continue
            else:
                html_lines.append('</table>')
                in_table = False
            continue
        elif in_table and not ('|' in line and line.strip().startswith('|')):
            html_lines.append('</table>')
            in_table = False
        
        # Strong/bold in worked examples
        if line.strip().startswith('**') and '**' in line[2:]:
            # This is a bold line
            text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line.strip())
            html_lines.append(f'<p>{convert_inline(text)}</p>')
            i += 1
            continue
        
        # Ordered lists
        m = re.match(r'^(\d+)\.\s+(.+)$', line.strip())
        if m:
            if not in_list or list_type != 'ol':
                if in_list:
                    html_lines.append(f'</{list_type}>')
                html_lines.append('<ol>')
                in_list = True
                list_type = 'ol'
            html_lines.append(f'<li>{convert_inline(m.group(2))}</li>')
            i += 1
            continue
        
        # Unordered lists
        if re.match(r'^[\-\*]\s+', line.strip()):
            text = re.sub(r'^[\-\*]\s+', '', line.strip())
            if not in_list or list_type != 'ul':
                if in_list:
                    html_lines.append(f'</{list_type}>')
                html_lines.append('<ul>')
                in_list = True
                list_type = 'ul'
            html_lines.append(f'<li>{convert_inline(text)}</li>')
            i += 1
            continue
        
        # Close list if we were in one
        if in_list and line.strip() == '':
            html_lines.append(f'</{list_type}>')
            in_list = False
            list_type = None
            i += 1
            continue
        elif in_list and not re.match(r'^[\-\*\d]', line.strip()):
            html_lines.append(f'</{list_type}>')
            in_list = False
            list_type = None
        
        # Display math (block) $$...$$
        if line.strip().startswith('$$') and line.strip().endswith('$$'):
            math = line.strip()[2:-2]
            html_lines.append(f'<p style="text-align:center;margin:0.8rem 0;">$${math}$$</p>')
            i += 1
            continue
        
        # Regular paragraphs
        stripped = line.strip()
        if stripped == '':
            html_lines.append('')
            i += 1
            continue
        
        # Skip if it looks like a continuation
        html_lines.append(f'<p>{convert_inline(stripped)}</p>')
        i += 1
    
    # Close any open tags
    if in_list:
        html_lines.append(f'</{list_type}>')
    if in_table:
        html_lines.append('</table>')
    if in_worked:
        html_lines.append('</div>')
    if in_definition:
        html_lines.append('</div>')
    
    return '\n'.join(html_lines)


def convert_inline(text):
    """Convert inline markdown to HTML within a line."""
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Inline math $...$ (but not $$)
    # Protect display math first
    text = re.sub(r'\$\$(.+?)\$\$', r'DISPLAYMATHPLACEHOLDER\1DISPLAYMATHEND', text)
    text = re.sub(r'\$(.+?)\$', r'$$\1$$', text)
    text = text.replace('DISPLAYMATHPLACEHOLDER', '$$').replace('DISPLAYMATHEND', '$$')
    return text


def convert_file(md_path, html_path, lesson_num):
    with open(md_path, 'r') as f:
        md_text = f.read()
    
    # Extract title from first # line
    title_match = re.search(r'^#\s+(.+)$', md_text, re.MULTILINE)
    title = title_match.group(1) if title_match else f'Lesson {lesson_num}'
    
    body = md_to_html(md_text, lesson_num)
    
    # Get previous and next lesson numbers
    prev_num = lesson_num - 1
    next_num = lesson_num + 1
    nav_html = f'''<div class="nav">
<a href="lesson_{prev_num:02d}.html">← Lesson {prev_num}</a>
<a href="lesson_{next_num:02d}.html">Lesson {next_num} →</a>
</div>'''
    
    full_html = HTML_HEADER.format(title=title) + '\n' + body + '\n' + nav_html + '\n' + HTML_FOOTER
    
    with open(html_path, 'w') as f:
        f.write(full_html)
    
    print(f'  Generated {html_path} ({len(full_html)} chars)')


if __name__ == '__main__':
    base = '/Users/a1/Desktop/studying_ChemistryHL/lessons'
    for num in range(32, 42):
        md_path = os.path.join(base, f'lesson_{num:02d}.md')
        html_path = os.path.join(base, f'lesson_{num:02d}.html')
        if os.path.exists(md_path):
            print(f'Converting lesson_{num:02d}.md...')
            convert_file(md_path, html_path, num)
        else:
            print(f'WARNING: {md_path} not found!')
    print('Done!')
