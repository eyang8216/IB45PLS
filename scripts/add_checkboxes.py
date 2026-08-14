#!/usr/bin/env python3
"""
Add completion checkbox to all lesson files (updated to handle subdirectories)
"""

import os
from pathlib import Path
from bs4 import BeautifulSoup

def add_checkbox_to_lesson(filepath):
    """Add completion checkbox to a lesson file"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has checkbox
    if 'lesson-completion' in content:
        return False

    soup = BeautifulSoup(content, 'html.parser')
    body = soup.find('body')

    if not body:
        return False

    # Add checkbox at the very top of body
    checkbox_html = '''
<div class="lesson-completion" style="margin: 0 0 2rem 0; padding: 1rem; background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border-radius: 8px; border: 2px solid #bae6fd;">
    <label class="completion-checkbox" style="display: flex; align-items: center; gap: 0.75rem; cursor: pointer;">
        <input type="checkbox" id="lesson-complete" style="width: 24px; height: 24px; cursor: pointer; accent-color: #10b981;">
        <span style="font-size: 1rem; color: #0f172a; font-weight: 600;">✓ Mark this lesson as complete</span>
    </label>
</div>
'''

    checkbox_soup = BeautifulSoup(checkbox_html, 'html.parser')

    # Insert as first child of body
    body.insert(0, checkbox_soup)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    return True


def main():
    subjects = ['biology', 'chemistry', 'physics', 'math', 'economics', 'english', 'chinese', 'sat']

    total_added = 0

    for subject in subjects:
        subject_dir = Path('subjects') / subject

        if not subject_dir.exists():
            continue

        # Check both root and lessons subdirectory
        lesson_files = []
        for pattern in ['lesson*.html', 'L*.html']:
            lesson_files.extend(subject_dir.glob(pattern))

            # Also check lessons subdirectory
            lessons_subdir = subject_dir / 'lessons'
            if lessons_subdir.exists():
                lesson_files.extend(lessons_subdir.glob(pattern))

        lesson_files = list(set(lesson_files))  # Remove duplicates
        added = 0

        for filepath in lesson_files:
            if add_checkbox_to_lesson(filepath):
                added += 1

        if added > 0:
            print(f"✅ {subject}: Added checkbox to {added} lessons")

        total_added += added

    print(f"\n✅ Total: Added checkbox to {total_added} lessons")


if __name__ == "__main__":
    main()
