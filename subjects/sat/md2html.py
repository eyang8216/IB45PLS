#!/usr/bin/env python3
"""Convert markdown lesson files to HTML with MathJax and SAT styling."""
import sys
import re

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<script>
MathJax = {{
  tex: {{
    inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
    displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
  }}
}};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>
<style>
  :root {{
    --bg: #fafaf9;
    --text: #1a1a1a;
    --accent: #1a5276;
    --trap-bg: #fff3cd;
    --trap-border: #ffc107;
    --pattern-bg: #d1ecf1;
    --pattern-border: #17a2b8;
    --card: #ffffff;
    --border: #d0d0cb;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    font-size: 16px;
    line-height: 1.7;
    color: var(--text);
    background: var(--bg);
    max-width: 820px;
    margin: 0 auto;
    padding: 2rem 1.5rem;
  }}
  h1 {{ font-size: 1.8rem; color: var(--accent); border-bottom: 3px solid var(--accent); padding-bottom: 0.5rem; margin-bottom: 1rem; }}
  h2 {{ font-size: 1.35rem; color: var(--accent); margin: 2rem 0 0.8rem; border-bottom: 1px solid var(--border); padding-bottom: 0.3rem; }}
  h3 {{ font-size: 1.15rem; color: #333; margin: 1.5rem 0 0.5rem; }}
  p, li {{ margin: 0.5em 0; }}
  ul, ol {{ padding-left: 1.5rem; margin: 0.5em 0; }}
  .trap-box {{
    background: var(--trap-bg);
    border-left: 4px solid var(--trap-border);
    padding: 1rem 1.2rem;
    margin: 1.2rem 0;
    border-radius: 0 6px 6px 0;
    font-size: 0.95rem;
  }}
  .trap-box strong {{ color: #856404; }}
  .pattern-box {{
    background: var(--pattern-bg);
    border-left: 4px solid var(--pattern-border);
    padding: 1rem 1.2rem;
    margin: 1.2rem 0;
    border-radius: 0 6px 6px 0;
    font-size: 0.95rem;
  }}
  .pattern-box strong {{ color: #0c5460; }}
  .example {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1rem 1.3rem;
    margin: 1rem 0;
  }}
  .example h4 {{ color: var(--accent); margin-bottom: 0.3rem; }}
  .nav {{
    display: flex;
    justify-content: space-between;
    margin: 2.5rem 0 1rem;
    padding-top: 1rem;
    border-top: 1px solid var(--border);
  }}
  .nav a {{ color: var(--accent); text-decoration: none; }}
  .nav a:hover {{ text-decoration: underline; }}
  code {{ background: #f0f0f0; padding: 0.15em 0.4em; border-radius: 3px; font-size: 0.9em; }}
  strong {{ color: #222; }}
  @media print {{
    body {{ font-size: 14px; }}
    .nav {{ display: none; }}
  }}
</style>
</head>
<body>
{body}
<div class="nav">
<a href="lesson{prev}.html">← Previous Lesson</a>
<a href="index.html">📋 All Lessons</a>
<a href="lesson{next}.html">Next Lesson →</a>
</div>
</body>
</html>'''

def md_to_html(md_content, lesson_num, title):
    """Basic markdown to HTML conversion."""
    lines = md_content.strip().split('\n')
    html_lines = []
    i = 0
    in_list = False
    
    while i < len(lines):
        line = lines[i]
        
        # Title (h1)
        if line.startswith('# ') and not line.startswith('## '):
            html_lines.append(f'<h1>{line[2:]}</h1>')
            i += 1
            continue
        
        # h2
        if line.startswith('## '):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(f'<h2>{line[3:]}</h2>')
            i += 1
            continue
        
        # h3
        if line.startswith('### '):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(f'<h3>{line[3:]}</h3>')
            i += 1
            continue
        
        # SAT Trap Alert
        if line.strip().startswith('**SAT Trap Alert**') or line.strip().startswith('> **SAT Trap'):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append('<div class="trap-box">')
            content = line.replace('**SAT Trap Alert**', '<strong>🚨 SAT TRAP ALERT:</strong>').replace('> ', '')
            html_lines.append(f'<p>{content}</p>')
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith('#') and not lines[i].strip().startswith('> **'):
                html_lines.append(f'<p>{lines[i].replace("> ", "").strip()}</p>')
                i += 1
            html_lines.append('</div>')
            continue
        
        # Pattern Recognition
        if line.strip().startswith('**Pattern Recognition**') or line.strip().startswith('> **Pattern'):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append('<div class="pattern-box">')
            content = line.replace('**Pattern Recognition**', '<strong>🔍 PATTERN RECOGNITION:</strong>').replace('> ', '')
            html_lines.append(f'<p>{content}</p>')
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith('#') and not lines[i].strip().startswith('> **'):
                html_lines.append(f'<p>{lines[i].replace("> ", "").strip()}</p>')
                i += 1
            html_lines.append('</div>')
            continue
        
        # Worked Example
        if line.strip().startswith('### Worked Example') or line.strip().startswith('### Example'):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append('<div class="example">')
            html_lines.append(f'<h4>{line.strip("# ")}</h4>')
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith('##') and not lines[i].startswith('---'):
                if lines[i].startswith('- '):
                    html_lines.append(f'<li>{lines[i][2:]}</li>')
                elif lines[i].startswith('**'):
                    html_lines.append(f'<p>{lines[i]}</p>')
                elif lines[i].strip().startswith('```'):
                    i += 1
                    code_lines = []
                    while i < len(lines) and not lines[i].strip().startswith('```'):
                        code_lines.append(lines[i])
                        i += 1
                    html_lines.append(f'<pre><code>{"".join(code_lines)}</code></pre>')
                else:
                    html_lines.append(f'<p>{lines[i]}</p>')
                i += 1
            html_lines.append('</div>')
            continue
        
        # Horizontal rule
        if line.strip() == '---':
            html_lines.append('<hr>')
            i += 1
            continue
        
        # Lists
        if line.strip().startswith('- ') or line.strip().startswith('* '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            html_lines.append(f'<li>{line.strip()[2:]}</li>')
            i += 1
            continue
        
        if line.strip().startswith('1. ') or (line.strip() and line.strip()[0].isdigit() and '. ' in line.strip()[:4]):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            # Find number
            import re
            m = re.match(r'(\d+)\.\s', line.strip())
            if m:
                html_lines.append(f'<li>{line.strip()[len(m.group(0)):]}</li>')
            i += 1
            continue
        
        # Empty line
        if not line.strip():
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            i += 1
            continue
        
        # Regular paragraph
        if in_list:
            html_lines.append('</ul>')
            in_list = False
        html_lines.append(f'<p>{line.strip()}</p>')
        i += 1
    
    if in_list:
        html_lines.append('</ul>')
    
    body = '\n'.join(html_lines)
    
    prev_num = max(1, lesson_num - 1)
    next_num = lesson_num + 1
    
    return HTML_TEMPLATE.format(
        title=title,
        body=body,
        prev=f"{prev_num:02d}" if prev_num < 10 else str(prev_num),
        next=f"{next_num:02d}" if next_num < 10 else str(next_num)
    )

if __name__ == '__main__':
    # Usage: python md2html.py lesson1.md lesson1.html "Lesson 1: Title"
    import os
    if len(sys.argv) < 3:
        print("Usage: md2html.py <input.md> <output.html> [title]")
        sys.exit(1)
    
    with open(sys.argv[1], 'r') as f:
        md_content = f.read()
    
    title = sys.argv[3] if len(sys.argv) > 3 else os.path.basename(sys.argv[1])
    
    # Extract lesson number
    import re
    num_match = re.search(r'lesson(\d+)', sys.argv[1])
    lesson_num = int(num_match.group(1)) if num_match else 1
    
    html = md_to_html(md_content, lesson_num, title)
    
    with open(sys.argv[2], 'w') as f:
        f.write(html)
    
    print(f"Converted {sys.argv[1]} → {sys.argv[2]}")
