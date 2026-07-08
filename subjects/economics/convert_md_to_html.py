#!/usr/bin/env python3
"""Convert lesson .md files to .html using the IB Economics SL template."""
import re
import sys
import os

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — IB Economics SL</title>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>
<style>
  body {{ font-family: Georgia, 'Times New Roman', serif; font-size: 17px; line-height: 1.8; color: #1a1a1a; background: #fdfcf9; max-width: 850px; margin: 0 auto; padding: 2rem 1.5rem; }}
  h1 {{ font-size: 1.8rem; color: #2c6b4f; border-bottom: 2px solid #2c6b4f; padding-bottom: 0.4rem; }}
  h2 {{ font-size: 1.3rem; color: #2c6b4f; margin-top: 2rem; }}
  h3 {{ font-size: 1.1rem; color: #333; }}
  .nav {{ display: flex; justify-content: space-between; padding: 0.7rem 0; border-bottom: 1px solid #ddd; margin-bottom: 1.5rem; font-size: 0.9rem; }}
  .nav a {{ color: #2c6b4f; text-decoration: none; }} .nav a:hover {{ text-decoration: underline; }}
  .ib-tip {{ background: #e8f5e9; border-left: 4px solid #2c6b4f; padding: 0.8rem 1rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }}
  .problem {{ background: #fff; border: 1px solid #ddd; padding: 1rem 1.2rem; margin: 0.8rem 0; border-radius: 6px; }}
  .answer {{ background: #f9fafb; border-left: 3px solid #888; padding: 0.8rem 1rem; margin: 0.5rem 0 1.2rem 1rem; border-radius: 0 4px 4px 0; }}
  .evaluate {{ background: #fff8e1; border: 1px solid #ffc107; padding: 1rem 1.2rem; margin: 1.5rem 0; border-radius: 6px; }}
  table {{ border-collapse: collapse; width: 100%; margin: 1rem 0; }} th, td {{ border: 1px solid #ccc; padding: 0.5rem 0.7rem; text-align: left; }} th {{ background: #e8f0ec; }}
  .misconception {{ background: #fef3f2; border-left: 4px solid #d93025; padding: 0.8rem 1rem; margin: 1rem 0; border-radius: 0 6px 6px 0; }}
  @media print {{ body {{ font-size: 12pt; }} .nav {{ display: none; }} }}
</style>
</head>
<body><div class="nav"><a href="{prev}">← Previous</a><a href="index.html">Index</a><a href="{next}">Next →</a></div>
{body}
<div class="nav"><a href="{prev}">← Previous</a><a href="index.html">Index</a><a href="{next}">Next →</a></div>
</body></html>'''

def md_to_html(text):
    """Convert basic markdown to HTML."""
    lines = text.split('\n')
    result = []
    i = 0
    in_table = False
    table_rows = []
    in_evaluate = False
    
    while i < len(lines):
        line = lines[i]
        
        # Evaluate section
        if line.startswith('## Evaluate') or line.startswith('### Evaluate'):
            in_evaluate = True
            result.append('<div class="evaluate">')
            result.append(f'<h2>{line.strip("# ")}</h2>')
            i += 1
            continue
        
        if in_evaluate and line.startswith('##') and not line.startswith('###'):
            in_evaluate = False
            result.append('</div>')
            # fall through to process this heading
        
        # IB Exam Tip
        if line.startswith('## IB Exam Tip'):
            result.append('<div class="ib-tip">')
            result.append(f'<h2>{line.strip("# ")}</h2>')
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith('##') and not lines[i].startswith('---'):
                result.append(f'<p>{lines[i]}</p>')
                i += 1
            result.append('</div>')
            continue
        
        # Misconception paragraphs
        if 'common mistake students make' in line.lower() or 'common pitfall' in line.lower():
            result.append(f'<div class="misconception"><p>{line}</p>')
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith('##') and not lines[i].startswith('---'):
                result.append(f'<p>{lines[i]}</p>')
                i += 1
            result.append('</div>')
            continue
        
        # Headings
        if line.startswith('# '):
            result.append(f'<h1>{line[2:]}</h1>')
        elif line.startswith('## '):
            result.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('### '):
            result.append(f'<h3>{line[4:]}</h3>')
        elif line.startswith('---'):
            result.append('<hr>')
        elif line.startswith('**') and line.endswith('**'):
            result.append(f'<p><strong>{line[2:-2]}</strong></p>')
        # Problem
        elif line.startswith('**Problem'):
            result.append(f'<div class="problem"><p><strong>{line[2:]}</strong></p>')
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith('**Answer') and not lines[i].startswith('## '):
                if lines[i].startswith('**Problem'):
                    break
                result.append(f'<p>{lines[i]}</p>')
                i += 1
            result.append('</div>')
            continue
        # Answer
        elif line.startswith('**Answer'):
            result.append(f'<div class="answer"><p><strong>{line[2:]}</strong></p>')
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith('**Answer') and not lines[i].startswith('## ') and not lines[i].startswith('---'):
                if lines[i].startswith('**Problem'):
                    break
                result.append(f'<p>{lines[i]}</p>')
                i += 1
            result.append('</div>')
            continue
        # Table row
        elif '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(line)
            # Check if next line is still a table
            if i + 1 < len(lines) and '|' in lines[i+1] and lines[i+1].strip().startswith('|'):
                i += 1
                continue
            else:
                # End of table
                result.append('<table>')
                for r_idx, row in enumerate(table_rows):
                    cells = [c.strip() for c in row.split('|')[1:-1]]
                    tag = 'th' if r_idx == 0 or (r_idx == 1 and all(set(c.strip()) <= {'-', ':', ' '} for c in cells)) else 'td'
                    if r_idx == 1 and all(set(c.strip()) <= {'-', ':', ' '} for c in cells):
                        continue  # skip separator row
                    result.append('<tr>')
                    for cell in cells:
                        result.append(f'<{tag}>{cell}</{tag}>')
                    result.append('</tr>')
                result.append('</table>')
                in_table = False
                table_rows = []
        # Bold text paragraphs
        elif line.startswith('**'):
            result.append(f'<p><strong>{line.strip("*")}</strong></p>')
        # Empty line
        elif not line.strip():
            pass  # skip empty lines
        # Regular paragraph
        elif line.strip():
            # Check if line contains bold markers
            processed = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
            result.append(f'<p>{processed}</p>')
        
        i += 1
    
    if in_evaluate:
        result.append('</div>')
    
    return '\n'.join(result)

def get_title(md_path):
    with open(md_path, 'r') as f:
        first_line = f.readline().strip()
    if first_line.startswith('# '):
        return first_line[2:]
    return os.path.basename(md_path)

def get_prev_next(lesson_num):
    prev_num = lesson_num - 1
    next_num = lesson_num + 1
    # Map lesson numbers to filenames
    names = {
        13: ('lesson_12.html', 'lesson_14.html'),
        14: ('lesson_13.html', 'lesson_15.html'),
        15: ('lesson_14.html', 'lesson_16.html'),
        16: ('lesson_15.html', 'lesson_17.html'),
        17: ('lesson_16.html', 'lesson_18.html'),
        18: ('lesson_17.html', 'lesson_19.html'),
    }
    prev_f, next_f = names.get(lesson_num, (f'lesson_{prev_num}.html', f'lesson_{next_num}.html'))
    return prev_f, next_f

def convert_file(md_path):
    with open(md_path, 'r') as f:
        md_content = f.read()
    
    title = md_content.split('\n')[0].strip('# ')
    body = md_to_html(md_content)
    
    # Extract lesson number
    import re
    match = re.search(r'Lesson[_\s]*(\d+)', md_path)
    if match:
        lesson_num = int(match.group(1))
    else:
        lesson_num = 13
    
    prev_f, next_f = get_prev_next(lesson_num)
    
    html = TEMPLATE.format(title=title, body=body, prev=prev_f, next=next_f)
    
    html_path = md_path.replace('.md', '.html')
    with open(html_path, 'w') as f:
        f.write(html)
    
    print(f"Converted: {md_path} -> {html_path}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for path in sys.argv[1:]:
            convert_file(path)
    else:
        print("Usage: python convert.py file1.md file2.md ...")
