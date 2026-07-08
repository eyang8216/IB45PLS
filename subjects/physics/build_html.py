#!/usr/bin/env python3
"""Convert all lesson .md files to .html with MathJax, navigation, and clean styling.
FIXED: MathJax config, subscript/superscript inside math blocks, escaping issues."""

import os
import re

LESSONS_DIR = "/Users/a1/Desktop/studying_PhysicsHL/lessons"

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<script>
MathJax = {{
  tex: {{
    inlineMath: [['$', '$']],
    displayMath: [['$$', '$$']]
  }},
  options: {{
    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']
  }}
}};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400&display=swap');
  
  :root {{
    --bg: #fdfcf9;
    --text: #1a1a1a;
    --accent: #2c5f2d;
    --border: #d0cec7;
    --code-bg: #f4f3ef;
    --callout-bg: #f0f7f0;
    --callout-border: #2c5f2d;
    --warning-bg: #fff8e6;
    --warning-border: #c4941a;
  }}
  
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  
  body {{
    font-family: 'Source Serif 4', Georgia, 'Times New Roman', serif;
    font-size: 17px;
    line-height: 1.7;
    color: var(--text);
    background: var(--bg);
    max-width: 780px;
    margin: 0 auto;
    padding: 2rem 1.5rem 4rem;
  }}
  
  h1 {{
    font-size: 2rem;
    font-weight: 700;
    margin: 0 0 1.5rem;
    padding-bottom: 0.75rem;
    border-bottom: 3px solid var(--accent);
    color: var(--accent);
  }}
  
  h2 {{
    font-size: 1.4rem;
    font-weight: 700;
    margin: 2.5rem 0 0.75rem;
    color: #1a1a1a;
  }}
  
  h3 {{
    font-size: 1.15rem;
    font-weight: 600;
    margin: 1.5rem 0 0.5rem;
  }}
  
  p {{ margin: 0 0 1rem; }}
  
  ul, ol {{ margin: 0 0 1rem 1.5rem; }}
  li {{ margin-bottom: 0.35rem; }}
  
  code {{
    background: var(--code-bg);
    padding: 0.15em 0.4em;
    border-radius: 3px;
    font-size: 0.9em;
    font-family: 'SF Mono', 'Consolas', 'Monaco', monospace;
  }}
  
  pre {{
    background: var(--code-bg);
    padding: 1rem 1.25rem;
    border-radius: 6px;
    overflow-x: auto;
    margin: 0 0 1rem;
    font-size: 0.85em;
    line-height: 1.5;
  }}
  
  pre code {{
    background: none;
    padding: 0;
    font-size: inherit;
  }}
  
  blockquote {{
    border-left: 4px solid var(--callout-border);
    background: var(--callout-bg);
    margin: 0 0 1rem;
    padding: 0.75rem 1.25rem;
    border-radius: 0 6px 6px 0;
  }}
  
  blockquote.warning {{
    border-left-color: var(--warning-border);
    background: var(--warning-bg);
  }}
  
  strong {{ font-weight: 700; }}
  
  hr {{
    border: none;
    border-top: 1px solid var(--border);
    margin: 2rem 0;
  }}
  
  .nav {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 2.5rem 0 1rem;
    padding-top: 1rem;
    border-top: 1px solid var(--border);
  }}
  
  .nav a {{
    color: var(--accent);
    text-decoration: none;
    font-weight: 600;
    padding: 0.4rem 0.8rem;
    border-radius: 4px;
    transition: background 0.2s;
  }}
  
  .nav a:hover {{ background: var(--callout-bg); }}
  
  .worked-example, .answer {{
    background: var(--code-bg);
    border-radius: 6px;
    padding: 1rem 1.25rem;
    margin: 0.75rem 0 1.25rem;
  }}
  
  .worked-example strong:first-child, .answer strong:first-child {{
    color: var(--accent);
  }}
  
  @media print {{
    body {{ font-size: 12pt; max-width: 100%; padding: 0; }}
    .nav {{ display: none; }}
    h1 {{ font-size: 18pt; }}
    h2 {{ font-size: 14pt; }}
  }}
  
  table {{
    border-collapse: collapse;
    width: 100%;
    margin: 0 0 1rem;
  }}
  
  th, td {{
    border: 1px solid var(--border);
    padding: 0.5rem 0.75rem;
    text-align: left;
  }}
  
  th {{
    background: var(--code-bg);
    font-weight: 700;
  }}
</style>
</head>
<body>

<nav class="nav">
  <a href="index.html">← Lesson Index</a>
  {prev_link}
  {next_link}
</nav>

{content}

<nav class="nav">
  <a href="index.html">← Lesson Index</a>
  {prev_link}
  {next_link}
</nav>

</body>
</html>'''


def protect_math_spans(text):
    """Replace $...$ and $$...$$ spans with placeholders to protect from regex processing."""
    placeholders = []
    
    def replace_display(m):
        placeholders.append(m.group(0))
        return f'\x00DISPLAY{len(placeholders)-1}\x00'
    
    def replace_inline(m):
        placeholders.append(m.group(0))
        return f'\x00INLINE{len(placeholders)-1}\x00'
    
    # Protect $$...$$ first (display math)
    text = re.sub(r'\$\$[^$]+\$\$', replace_display, text)
    # Then protect $...$ (inline math)
    text = re.sub(r'\$[^$]+\$', replace_inline, text)
    
    return text, placeholders

def restore_math_spans(text, placeholders):
    """Restore math spans from placeholders."""
    for i, ph in enumerate(placeholders):
        text = text.replace(f'\x00INLINE{i}\x00', ph)
        text = text.replace(f'\x00DISPLAY{i}\x00', ph)
    return text


def md_to_html(md_text):
    """Simple markdown-to-HTML converter for lesson files."""
    lines = md_text.split('\n')
    
    # First, join all lines and protect math spans
    full_text = '\n'.join(lines)
    full_text, math_placeholders = protect_math_spans(full_text)
    lines = full_text.split('\n')
    
    out = []
    in_code_block = False
    in_list = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Code blocks
        if line.strip().startswith('```'):
            if in_code_block:
                out.append('</code></pre>')
                in_code_block = False
            else:
                out.append('<pre><code>')
                in_code_block = True
            i += 1
            continue
        
        if in_code_block:
            out.append(line)
            i += 1
            continue
        
        # Headers
        if line.startswith('#### '):
            out.append(f'<h4>{process_inline(line[5:])}</h4>')
        elif line.startswith('### '):
            out.append(f'<h3>{process_inline(line[4:])}</h3>')
        elif line.startswith('## '):
            out.append(f'<h2>{process_inline(line[3:])}</h2>')
        elif line.startswith('# '):
            out.append(f'<h1>{process_inline(line[2:])}</h1>')
        
        # Horizontal rules
        elif line.strip() == '---':
            out.append('<hr>')
        
        # Blockquotes
        elif line.startswith('> '):
            cls = ' class="warning"' if '⚠' in line or 'CRITICAL' in line or 'IMPORTANT' in line else ''
            out.append(f'<blockquote{cls}>{process_inline(line[2:])}</blockquote>')
        
        # Tables
        elif '|' in line and line.strip().startswith('|'):
            out.append(process_table(lines, i))
            while i < len(lines) and '|' in lines[i]:
                i += 1
            continue
        
        # Lists
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            if not in_list:
                out.append('<ul>')
                in_list = 'ul'
            content = re.sub(r'^[\s]*[-*]\s+', '', line)
            out.append(f'<li>{process_inline(content)}</li>')
        elif re.match(r'^\s*\d+[.)]\s', line.strip()):
            if not in_list:
                out.append('<ol>')
                in_list = 'ol'
            content = re.sub(r'^\s*\d+[.)]\s+', '', line.strip())
            out.append(f'<li>{process_inline(content)}</li>')
        else:
            if in_list:
                out.append(f'</{in_list}>')
                in_list = False
            
            if line.strip() == '':
                out.append('')
            else:
                out.append(f'<p>{process_inline(line)}</p>')
        
        i += 1
    
    if in_list:
        out.append(f'</{in_list}>')
    if in_code_block:
        out.append('</code></pre>')
    
    result = '\n'.join(out)
    # Restore math spans
    result = restore_math_spans(result, math_placeholders)
    return result


def process_table(lines, start_idx):
    """Process a markdown table."""
    table_lines = []
    i = start_idx
    while i < len(lines) and '|' in lines[i]:
        table_lines.append(lines[i])
        i += 1
    
    if len(table_lines) < 2:
        return '<p>' + ' | '.join(table_lines) + '</p>'
    
    html = ['<table>']
    for idx, tl in enumerate(table_lines):
        cells = [c.strip() for c in tl.split('|') if c.strip() != '']
        if all(re.match(r'^[-:]+$', c) for c in cells):
            continue
        tag = 'th' if idx == 0 else 'td'
        html.append('<tr>')
        for cell in cells:
            html.append(f'<{tag}>{process_inline(cell)}</{tag}>')
        html.append('</tr>')
    html.append('</table>')
    return '\n'.join(html)


def process_inline(text):
    """Process inline markdown: bold, italic, code. Does NOT process math-protected spans."""
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # Subscripts (only OUTSIDE math blocks — math blocks are already protected by placeholders)
    text = re.sub(r'_\{([^}]+)\}', r'<sub>\1</sub>', text)
    # Superscripts (same protection)
    text = re.sub(r'\^\{([^}]+)\}', r'<sup>\1</sup>', text)
    return text


def get_lesson_info(filename):
    """Extract lesson number and title from filename and first line."""
    match = re.match(r'L(\d+)_(.+)\.md', filename)
    if not match:
        return None, None, None
    num = int(match.group(1))
    slug = match.group(2)
    
    path = os.path.join(LESSONS_DIR, filename)
    try:
        with open(path, 'r') as f:
            first_line = f.readline().strip()
            title = first_line.lstrip('# ').strip()
    except:
        title = slug.replace('_', ' ').title()
    
    return num, slug, title


def generate_all_html():
    """Generate HTML for all lesson .md files."""
    md_files = sorted(
        [f for f in os.listdir(LESSONS_DIR) if f.endswith('.md') and f.startswith('L')],
        key=lambda x: int(re.match(r'L(\d+)', x).group(1))
    )
    
    lessons_info = []
    for f in md_files:
        num, slug, title = get_lesson_info(f)
        if num:
            lessons_info.append((num, slug, title, f))
    
    for idx, (num, slug, title, filename) in enumerate(lessons_info):
        md_path = os.path.join(LESSONS_DIR, filename)
        html_filename = filename.replace('.md', '.html')
        html_path = os.path.join(LESSONS_DIR, html_filename)
        
        with open(md_path, 'r') as f:
            md_content = f.read()
        
        body_html = md_to_html(md_content)
        
        prev_link = ''
        next_link = ''
        if idx > 0:
            prev_fn = lessons_info[idx-1][3].replace('.md', '.html')
            prev_link = f'<a href="{prev_fn}">← Lesson {lessons_info[idx-1][0]}</a>'
        else:
            prev_link = '<span></span>'
        
        if idx < len(lessons_info) - 1:
            next_fn = lessons_info[idx+1][3].replace('.md', '.html')
            next_link = f'<a href="{next_fn}">Lesson {lessons_info[idx+1][0]} →</a>'
        else:
            next_link = '<span></span>'
        
        html = HTML_TEMPLATE.format(
            title=f'Lesson {num}: {title} — IB Physics HL',
            content=body_html,
            prev_link=prev_link,
            next_link=next_link
        )
        
        with open(html_path, 'w') as f:
            f.write(html)
        
        print(f"  Generated: {html_filename}")
    
    return lessons_info


def generate_index(lessons_info):
    """Generate index.html with all lessons organized by chapter."""
    chapters = [
        ("A.1 Kinematics", [1]),
        ("A.2 Forces & Momentum", [2, 3, 4]),
        ("A.3 Work, Energy & Power", [5]),
        ("A.4 Rigid Body Mechanics (HL)", [6, 7, 8]),
        ("A.5 Special Relativity (HL)", [9, 11, 12, 13]),
        ("Measurement & Uncertainty", [10]),
        ("B.1 Thermal Energy Transfers", [14, 15]),
        ("B.2 Greenhouse Effect", [16, 17]),
        ("B.3 Gas Laws", [18, 19, 20]),
        ("B.4 Thermodynamics (HL)", [21, 22, 23]),
        ("B.5 Current & Circuits", [24, 25, 26, 27, 28]),
        ("C.1 Simple Harmonic Motion", [29, 30, 31, 32]),
        ("C.2 Wave Model", [33, 34, 35]),
        ("C.3 Wave Phenomena", [36, 37, 38, 39]),
        ("C.4 Standing Waves & Resonance", [40, 41, 42]),
        ("C.5 Doppler Effect", [43, 44]),
        ("D.1 Gravitational Fields", [45, 46, 47]),
        ("D.2 Electric & Magnetic Fields", [48, 49, 50, 51]),
        ("D.3 Motion in EM Fields", [52, 53]),
        ("D.4 Induction (HL)", [54, 55, 56]),
        ("E.1 Structure of the Atom", [57, 58, 59]),
        ("E.2 Quantum Physics (HL)", [60, 61, 62, 63]),
        ("E.3 Radioactive Decay", [64, 65]),
        ("E.4 Fission", [66]),
        ("E.5 Fusion & Stars", [67]),
    ]
    
    lesson_map = {num: (slug, title, fn) for num, slug, title, fn in lessons_info}
    
    rows = []
    for ch_name, lesson_nums in chapters:
        rows.append(f'<tr><th colspan="3">{ch_name}</th></tr>')
        for n in lesson_nums:
            if n in lesson_map:
                slug, title, fn = lesson_map[n]
                html_fn = fn.replace('.md', '.html')
                rows.append(
                    f'<tr>'
                    f'<td style="text-align:center;width:60px">{n}</td>'
                    f'<td><a href="{html_fn}">{title}</a></td>'
                    f'<td style="text-align:center;width:60px">🔲</td>'
                    f'</tr>'
                )
    
    index_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IB Physics HL — Lesson Index</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700&display=swap');
  
  :root {{
    --bg: #fdfcf9;
    --text: #1a1a1a;
    --accent: #2c5f2d;
    --border: #d0cec7;
    --code-bg: #f4f3ef;
  }}
  
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  
  body {{
    font-family: 'Source Serif 4', Georgia, serif;
    font-size: 17px;
    line-height: 1.7;
    color: var(--text);
    background: var(--bg);
    max-width: 820px;
    margin: 0 auto;
    padding: 2rem 1.5rem 4rem;
  }}
  
  h1 {{
    font-size: 2rem;
    font-weight: 700;
    margin: 0 0 0.5rem;
    color: var(--accent);
  }}
  
  .subtitle {{
    color: #666;
    margin-bottom: 2rem;
    font-style: italic;
  }}
  
  .stats {{
    display: flex;
    gap: 2rem;
    margin: 0 0 2rem;
    flex-wrap: wrap;
  }}
  
  .stat {{
    background: var(--code-bg);
    padding: 0.75rem 1.25rem;
    border-radius: 6px;
    text-align: center;
  }}
  
  .stat .num {{
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--accent);
  }}
  
  .stat .label {{
    font-size: 0.85rem;
    color: #666;
  }}
  
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
  }}
  
  th {{
    background: var(--accent);
    color: white;
    padding: 0.6rem 1rem;
    text-align: left;
    font-weight: 600;
  }}
  
  td {{
    padding: 0.5rem 1rem;
    border-bottom: 1px solid var(--border);
  }}
  
  tr:hover td {{
    background: #f8f7f3;
  }}
  
  a {{
    color: var(--accent);
    text-decoration: none;
    font-weight: 600;
  }}
  
  a:hover {{ text-decoration: underline; }}
  
  .legend {{
    margin: 2rem 0 1rem;
    font-size: 0.9rem;
    color: #666;
  }}
  
  .legend span {{
    margin-right: 1.5rem;
  }}
  
  @media print {{
    body {{ font-size: 12pt; max-width: 100%; }}
    a {{ color: #000; }}
    th {{ background: #ddd; color: #000; }}
    .stats {{ display: none; }}
  }}
</style>
</head>
<body>

<h1>IB Physics HL — Complete Lessons</h1>
<p class="subtitle">67 lessons covering every topic in the Pearson IB Physics HL textbook (Hamper &amp; Mitchell, 3rd Ed., 2023). Built for a 7.</p>

<div class="stats">
  <div class="stat"><div class="num">67</div><div class="label">Lessons</div></div>
  <div class="stat"><div class="num">25</div><div class="label">Chapters</div></div>
  <div class="stat"><div class="num">42</div><div class="label">Day Plan</div></div>
  <div class="stat"><div class="num">~300</div><div class="label">Practice Problems</div></div>
</div>

<p class="legend">
  <span>🔲 = Not started</span>
  <span>🔄 = In progress</span>
  <span>✅ = Mastered</span>
  <span>⚠️ = Review needed</span>
</p>

<table>
  <tr><th style="width:60px;text-align:center">#</th><th>Lesson Title</th><th style="width:60px;text-align:center">Done</th></tr>
  {''.join(rows)}
</table>

<p style="margin-top:2rem;text-align:center;color:#999;font-size:0.9rem;">
  <a href="../study_plan.md">📅 Study Plan</a> &nbsp;·&nbsp;
  <a href="../diagnosis.md">🔍 Diagnosis</a> &nbsp;·&nbsp;
  <a href="../syllabus_overview.md">✅ Syllabus Checklist</a> &nbsp;·&nbsp;
  <a href="data_booklet.html">📖 Data Booklet</a>
</p>

</body>
</html>'''
    
    with open(os.path.join(LESSONS_DIR, 'index.html'), 'w') as f:
        f.write(index_html)
    
    print(f"  Generated: index.html")


if __name__ == '__main__':
    print("Generating HTML from lesson markdown files...")
    print("(MathJax config fixed, math blocks protected from HTML injection)")
    lessons = generate_all_html()
    generate_index(lessons)
    print(f"\nDone! {len(lessons)} lessons converted to HTML.")
