#!/usr/bin/env python3
"""
Add missing interactive buttons (Flashcards, Practice, AI) to lessons
"""
import os
import glob
import re
from pathlib import Path

BASE_DIR = "/Users/a3015110/Desktop/IB45PLS/subjects"

BUTTON_HTML = '''
<div class="lesson-actions" style="margin: 2rem 0; padding: 1.5rem; background: #f8fafc; border-radius: 8px; border: 1px solid #e2e8f0;">
    <h3 style="margin: 0 0 1rem 0; font-size: 1.1rem; color: #334155;">📚 Study Tools</h3>
    <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
        <button onclick="generateFlashcards()" style="flex: 1; min-width: 140px; padding: 0.75rem 1rem; background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); color: white; border: none; border-radius: 6px; font-weight: 600; cursor: pointer; transition: transform 0.2s;">
            🃏 Generate Flashcards
        </button>
        <button onclick="generatePractice()" style="flex: 1; min-width: 140px; padding: 0.75rem 1rem; background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white; border: none; border-radius: 6px; font-weight: 600; cursor: pointer; transition: transform 0.2s;">
            📝 Practice Problems
        </button>
        <button onclick="openAI()" style="flex: 1; min-width: 140px; padding: 0.75rem 1rem; background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%); color: white; border: none; border-radius: 6px; font-weight: 600; cursor: pointer; transition: transform 0.2s;">
            🤖 Ask AI Tutor
        </button>
    </div>
</div>

<script>
function generateFlashcards() {
    const lessonTitle = document.querySelector('h1').textContent;
    alert('Flashcard generation coming soon for: ' + lessonTitle);
    // TODO: Implement flashcard generation
}

function generatePractice() {
    const lessonTitle = document.querySelector('h1').textContent;
    alert('Practice problem generation coming soon for: ' + lessonTitle);
    // TODO: Implement practice generation
}

function openAI() {
    const lessonTitle = document.querySelector('h1').textContent;
    alert('AI tutor coming soon for: ' + lessonTitle);
    // TODO: Implement AI tutor
}
</script>
'''

def add_buttons_to_lesson(filepath, subject):
    """Add interactive buttons to a lesson file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if buttons already exist
    if 'lesson-actions' in content or 'generateFlashcards' in content:
        return False, "already has buttons"

    # Find insertion point (before closing </body> tag)
    if '</body>' not in content:
        return False, "no </body> tag found"

    # Insert buttons before </body>
    new_content = content.replace('</body>', BUTTON_HTML + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True, "buttons added"

# Process each subject
subjects_to_fix = [
    ('math', 'lesson*.html'),
    ('economics', 'lesson_*.html'),
    ('chinese', 'lesson_*.html'),
    ('english', 'lesson_*.html'),
    ('sat', 'lesson_*.html'),
]

total_added = 0
total_skipped = 0

for subject, pattern in subjects_to_fix:
    print("=" * 60)
    print(f"Processing {subject.upper()}")
    print("=" * 60)

    lessons = sorted(glob.glob(f"{BASE_DIR}/{subject}/{pattern}"))
    print(f"Found {len(lessons)} lessons")

    added = 0
    skipped = 0

    for lesson_path in lessons:
        success, message = add_buttons_to_lesson(lesson_path, subject)
        basename = os.path.basename(lesson_path)

        if success:
            print(f"✓ {basename} - {message}")
            added += 1
        else:
            print(f"○ {basename} - {message}")
            skipped += 1

    print(f"\n{subject.upper()}: {added} updated, {skipped} skipped\n")
    total_added += added
    total_skipped += skipped

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"✅ Total lessons updated: {total_added}")
print(f"○ Total lessons skipped: {total_skipped}")
print(f"\nAll interactive buttons added successfully!")
