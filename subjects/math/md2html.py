#!/usr/bin/env python3
"""Quick markdown-to-HTML for lesson files."""
import sys, re

content = open(sys.argv[1]).read()
html_path = sys.argv[2]
title = sys.argv[3]
lesson_num = int(sys.argv[4])

lines = content.split('\n')
out = []
in_code = False
in_table = False
table_rows = []
list_buf = []

def flush_list():
    global list_buf
    if list_buf:
        out.append('<ul>' + ''.join(f'<li>{l}</li>' for l in list_buf) + '</ul>')
        list_buf = []

def render_table(rows):
    result = []
    for i, row in enumerate(rows):
        cells = [c.strip() for c in row.split('|')]
        cells = [c for c in cells if c]
        if all(re.match(r'^[:\- ]+$', c) for c in cells):
            continue
        tag = 'th' if i == 0 else 'td'
        result.append('<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in cells) + '</tr>')
    return '\n'.join(result)

def process_inline(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    return text

for line in lines:
    if in_code:
        if line.startswith('```'):
            out.append('</pre>')
            in_code = False
        else:
            out.append(line)
        continue
    
    if line.startswith('```'):
        in_code = True
        out.append('<pre>')
        continue
    
    if in_table:
        if line.startswith('|'):
            table_rows.append(line)
            continue
        else:
            out.append('<table>')
            out.append(render_table(table_rows))
            out.append('</table>')
            in_table = False
            table_rows = []
    
    if line.startswith('|'):
        in_table = True
        table_rows = [line]
        continue
    
    if line.startswith('# '):
        flush_list()
        out.append(f'<h1>{process_inline(line[2:])}</h1>')
    elif line.startswith('## '):
        flush_list()
        out.append(f'<h2>{process_inline(line[3:])}</h2>')
    elif line.startswith('### '):
        flush_list()
        out.append(f'<h3>{process_inline(line[4:])}</h3>')
    elif line.strip() == '---':
        flush_list()
        out.append('<hr>')
    elif line.strip() == '':
        flush_list()
        out.append('')
    elif line.strip().startswith('$$') and line.strip().endswith('$$'):
        flush_list()
        math = line.strip()[2:-2]
        out.append(f'<div class="math-block">$${math}$$</div>')
    elif line.startswith('- ') or line.startswith('* '):
        list_buf.append(process_inline(line[2:]))
    elif re.match(r'^\d+\.', line):
        list_buf.append(process_inline(line))
    else:
        flush_list()
        out.append(f'<p>{process_inline(line)}</p>')

flush_list()
if in_table and table_rows:
    out.append('<table>')
    out.append(render_table(table_rows))
    out.append('</table>')

body = '\n'.join(out)

html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lesson {lesson_num} — {title}</title>
<script>MathJax={{tex:{{inlineMath:[['$','$']],displayMath:[['$$','$$']]}}}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>
<style>body{{max-width:800px;margin:40px auto;font-family:'Times New Roman',Georgia,serif;font-size:17px;line-height:1.7;padding:0 20px;color:#1a1a1a;}}h1{{font-size:22px;border-bottom:2px solid #333;padding-bottom:8px;margin-top:36px;}}h2{{font-size:19px;margin-top:28px;color:#2c3e50;}}h3{{font-size:17px;margin-top:22px;color:#444;}}p{{margin:0.6em 0;}}li{{margin:0.3em 0 0.3em 20px;}}.math-block{{text-align:center;margin:1em 0;overflow-x:auto;}}b{{color:#222;}}.nav{{text-align:center;margin:30px 0;font-size:14px;}}.nav a{{margin:0 8px;color:#3498db;text-decoration:none;}}table{{border-collapse:collapse;margin:1em auto;}}th,td{{border:1px solid #999;padding:6px 14px;text-align:center;}}pre{{background:#f7f7f7;padding:10px 16px;border-left:3px solid #3498db;overflow-x:auto;font-family:'Courier New',monospace;font-size:15px;line-height:1.4;}}ul{{margin:0.5em 0;}}ul li{{list-style-type:disc;}}</style></head><body>
<div class="nav"><a href="index.html">← Back to Index</a></div>

{body}

<div class="nav"><a href="index.html">← Back to Index</a></div>
</body></html>'''

open(html_path, 'w').write(html)
