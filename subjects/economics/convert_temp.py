#!/usr/bin/env python3
"""Convert lesson .md files to .html using the gold-standard template."""
import re, os

lessons = {
    19: ("Positive Externalities — Production and Consumption", "lesson18.html", "lesson20.html"),
    20: ("Public Goods", "lesson19.html", "lesson21.html"),
    21: ("Government Responses to Market Failure — Full Evaluation", "lesson20.html", "lesson22.html"),
    22: ("Economic Activity and the Circular Flow Model", "lesson21.html", "lesson23.html"),
    23: ("Measuring GDP, GNI, and National Income", "lesson22.html", "lesson24.html"),
    24: ("The Business Cycle and Alternative Measures of Well-Being", "lesson23.html", "lesson25.html"),
}

def md_to_html(text):
    """Convert basic markdown to HTML for the lesson content."""
    lines = text.split('\n')
    result = []
    i = 0
    in_table = False
    in_code = False
    table_rows = []
    
    while i < len(lines):
        line = lines[i]
        
        # Code blocks
        if line.strip().startswith('```'):
            if in_code:
                result.append('</code></pre>')
                in_code = False
            else:
                result.append('<pre><code>')
                in_code = True
            i += 1
            continue
        
        if in_code:
            result.append(line)
            i += 1
            continue
        
        # Horizontal rules
        if line.strip() == '---':
            result.append('<hr>')
            i += 1
            continue
        
        # Headers
        m = re.match(r'^#### (.+)$', line)
        if m:
            result.append(f'<h4>{process_inline(m.group(1))}</h4>')
            i += 1
            continue
        
        m = re.match(r'^### (.+)$', line)
        if m:
            result.append(f'<h3>{process_inline(m.group(1))}</h3>')
            i += 1
            continue
        
        m = re.match(r'^## (.+)$', line)
        if m:
            result.append(f'<h2>{process_inline(m.group(1))}</h2>')
            i += 1
            continue
        
        m = re.match(r'^# (.+)$', line)
        if m:
            # Skip the main h1 — handled by template
            i += 1
            continue
        
        # Tables
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_rows = []
            # Skip separator rows like |---|---|
            if re.match(r'^\|[\s\-:|]+\|$', line.strip()):
                i += 1
                continue
            cells = [c.strip() for c in line.strip().split('|')[1:-1]]
            table_rows.append(cells)
            i += 1
            continue
        elif in_table:
            # End of table
            result.append('<table>')
            for ri, row in enumerate(table_rows):
                tag = 'th' if ri == 0 else 'td'
                result.append('<tr>')
                for cell in row:
                    result.append(f'<{tag}>{process_inline(cell)}</{tag}>')
                result.append('</tr>')
            result.append('</table>')
            in_table = False
            table_rows = []
            # Don't increment i — reprocess this line
            continue
        
        # Boxed equations
        if '\\boxed{' in line:
            line = line.replace('\\boxed{', '<span style="border:2px solid #2c6b4f; padding:2px 6px;">')
            line = line.replace('}', '</span>')
        
        # Display math $$...$$
        line = re.sub(r'\$\$(.+?)\$\$', r'$$\1$$', line)
        
        # Inline math $...$ (but not $$)
        line = re.sub(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', r'\\(\1\\)', line)
        
        # Bold
        line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
        
        # Empty line
        if line.strip() == '':
            result.append('')
            i += 1
            continue
        
        result.append(line)
        i += 1
    
    # Handle trailing table
    if in_table and table_rows:
        result.append('<table>')
        for ri, row in enumerate(table_rows):
            tag = 'th' if ri == 0 else 'td'
            result.append('<tr>')
            for cell in row:
                result.append(f'<{tag}>{process_inline(cell)}</{tag}>')
            result.append('</tr>')
        result.append('</table>')
    
    return '\n'.join(result)

def process_inline(text):
    """Process inline markdown formatting."""
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\$(.+?)\$', r'\\(\1\\)', text)
    text = re.sub(r'\\boxed\{([^}]+)\}', r'<span style="border:2px solid #2c6b4f; padding:2px 6px;">\1</span>', text)
    return text

def convert_lesson(num, title, prev_link, next_link):
    md_path = f'/Users/a1/Desktop/studying_EconomicsSL/lessons/lesson{num}.md'
    html_path = f'/Users/a1/Desktop/studying_EconomicsSL/lessons/lesson{num}.html'
    
    with open(md_path, 'r') as f:
        md_content = f.read()
    
    # Convert markdown to HTML
    body_html = md_to_html(md_content)
    
    # Build full HTML
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lesson {num}: {title} — IB Economics SL</title>
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
<body>
<div class="nav"><a href="{prev_link}">← Previous</a><a href="index.html">Index</a><a href="{next_link}">Next →</a></div>

<h1>Lesson {num}: {title}</h1>

{body_html}

<div class="nav"><a href="{prev_link}">← Previous</a><a href="index.html">Index</a><a href="{next_link}">Next →</a></div>
</body></html>'''
    
    with open(html_path, 'w') as f:
        f.write(html)
    
    print(f"Wrote {html_path}")

for num, (title, prev_link, next_link) in lessons.items():
    convert_lesson(num, title, prev_link, next_link)

print("Done!")
