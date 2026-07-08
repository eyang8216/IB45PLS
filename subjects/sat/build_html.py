#!/usr/bin/env python3
"""Build all HTML files from markdown lesson files."""
import subprocess
import os
import sys

LESSONS_DIR = os.path.dirname(os.path.abspath(__file__))

# Get all .md lesson files
md_files = sorted([f for f in os.listdir(LESSONS_DIR) if f.startswith('lesson') and f.endswith('.md')])

for md_file in md_files:
    num = md_file.replace('lesson', '').replace('.md', '')
    html_file = f'lesson{num}.html'
    md_path = os.path.join(LESSONS_DIR, md_file)
    html_path = os.path.join(LESSONS_DIR, html_file)
    
    # Read title from md
    with open(md_path, 'r') as f:
        first_line = f.readline().strip()
    title = first_line.replace('# ', '') if first_line.startswith('# ') else f'Lesson {num}'
    
    cmd = ['python3', os.path.join(LESSONS_DIR, 'md2html.py'), md_path, html_path, title]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f'✅ {md_file} → {html_file}')
    else:
        print(f'❌ {md_file}: {result.stderr.strip()}')

print(f'\nDone! Built {len(md_files)} HTML files.')
