#!/usr/bin/env python3
"""Convert markdown lesson files to HTML using the IB Economics SL template."""
import sys, re

TEMPLATE_TOP = '''<!DOCTYPE html>
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
<body>
<div class="nav"><a href="{prev}">← Previous</a><a href="index.html">Index</a><a href="{next}">Next →</a></div>
'''

TEMPLATE_BOTTOM = '''
<div class="nav"><a href="{prev}">← Previous</a><a href="index.html">Index</a><a href="{next}">Next →</a></div>
</body></html>
'''

def md_to_html(text):
    """Convert markdown to HTML for lesson content."""
    lines = text.split('\n')
    result = []
    in_table = False
    table_rows = []
    in_math = False
    math_buf = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Math blocks $$...$$
        if line.strip().startswith('$$') and not in_math:
            in_math = True
            math_buf = [line]
            i += 1
            continue
        if in_math:
            math_buf.append(line)
            if line.strip().endswith('$$'):
                in_math = False
                result.append('\n'.join(math_buf))
                math_buf = []
            i += 1
            continue
        
        # Inline math $...$ - keep as is (MathJax handles it)
        
        # Tables
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(line)
            # Check if next line continues the table
            if i + 1 < len(lines) and '|' in lines[i+1] and lines[i+1].strip().startswith('|'):
                i += 1
                continue
            else:
                # End of table, render it
                result.append(render_table(table_rows))
                table_rows = []
                in_table = False
                i += 1
                continue
        elif in_table:
            # Table ended
            result.append(render_table(table_rows))
            table_rows = []
            in_table = False
        
        # Headers
        if line.startswith('### '):
            result.append(f'<h3>{line[4:]}</h3>')
        elif line.startswith('## '):
            result.append(f'<h2>{line[2:]}</h2>')
        elif line.startswith('# '):
            result.append(f'<h1>{line[2:]}</h1>')
        # Horizontal rule
        elif line.strip() == '---':
            result.append('<hr>')
        # Empty line
        elif line.strip() == '':
            result.append('')
        # Bold
        else:
            # Process inline formatting
            processed = line
            processed = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', processed)
            # Wrap non-empty lines in <p> if not already a tag
            if processed.strip() and not processed.strip().startswith('<'):
                processed = f'<p>{processed}</p>'
            result.append(processed)
        
        i += 1
    
    # Handle leftover table
    if in_table and table_rows:
        result.append(render_table(table_rows))
    
    # Handle leftover math
    if in_math:
        result.append('\n'.join(math_buf))
    
    return '\n'.join(result)

def render_table(rows):
    """Render a markdown table as HTML."""
    if len(rows) < 2:
        return '<table>' + ''.join(f'<tr><td>{c.strip()}</td></tr>' for c in rows[0].split('|')[1:-1]) + '</table>'
    
    html = '<table>\n'
    # Header row
    cells = [c.strip() for c in rows[0].split('|')[1:-1]]
    html += '<thead><tr>' + ''.join(f'<th>{c}</th>' for c in cells) + '</tr></thead>\n'
    
    # Skip separator row (rows[1])
    html += '<tbody>\n'
    for row in rows[2:]:
        cells = [c.strip() for c in row.split('|')[1:-1]]
        html += '<tr>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>\n'
    html += '</tbody>\n</table>'
    return html


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("Usage: convert.py input.md output.html prev_url next_url title")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    prev_url = sys.argv[3]
    next_url = sys.argv[4]
    title = sys.argv[5]
    
    with open(input_file) as f:
        md_content = f.read()
    
    # Get title from first heading if not provided
    if not title:
        for line in md_content.split('\n'):
            if line.startswith('# '):
                title = line[2:]
                break
    
    html_content = md_to_html(md_content)
    
    top = TEMPLATE_TOP.format(title=title, prev=prev_url, next=next_url)
    bottom = TEMPLATE_BOTTOM.format(prev=prev_url, next=next_url)
    
    with open(output_file, 'w') as f:
        f.write(top + '\n' + html_content + '\n' + bottom)
    
    print(f"Converted {input_file} → {output_file}")
