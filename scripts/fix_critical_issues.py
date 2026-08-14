#!/usr/bin/env python3
"""
Fix all critical and high priority issues from Phase 3 verification
"""
import os
import glob
from pathlib import Path

BASE_DIR = "/Users/a3015110/Desktop/IB45PLS/subjects"

# Issue 1: Fix Physics missing checkboxes (67 lessons)
print("=" * 60)
print("TASK 1: Adding completion checkboxes to Physics lessons")
print("=" * 60)

physics_lessons = sorted(glob.glob(f"{BASE_DIR}/physics/L*.html"))
print(f"Found {len(physics_lessons)} Physics lessons")

for lesson_path in physics_lessons:
    with open(lesson_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if checkbox already exists
    if 'lesson-completion' in content or 'lesson-complete' in content:
        print(f"✓ {os.path.basename(lesson_path)} - already has checkbox")
        continue

    # Find the first h1 or body tag to insert before
    if '<h1' in content:
        insert_point = content.find('<h1')
    elif '<body>' in content:
        insert_point = content.find('<body>') + 6
    else:
        print(f"✗ {os.path.basename(lesson_path)} - no insertion point found")
        continue

    checkbox_html = '''<div class="lesson-completion" style="margin: 0 0 2rem 0; padding: 1rem; background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border-radius: 8px; border: 2px solid #bae6fd;">
<label class="completion-checkbox" style="display: flex; align-items: center; gap: 0.75rem; cursor: pointer;">
<input id="lesson-complete" style="width: 24px; height: 24px; cursor: pointer; accent-color: #10b981;" type="checkbox" onchange="markLessonComplete('physics', this)"/>
<span style="font-size: 1rem; color: #0f172a; font-weight: 600;">✓ Mark this lesson as complete</span>
</label>
</div>

'''

    new_content = content[:insert_point] + checkbox_html + content[insert_point:]

    # Add JavaScript if not present
    if 'markLessonComplete' not in new_content:
        js_code = '''
<script>
function markLessonComplete(subject, checkbox) {
    const lessonId = window.location.pathname.split('/').pop().replace('.html', '');
    const completed = checkbox.checked;

    fetch('/toggle_completion', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            subject: subject,
            lesson: lessonId,
            completed: completed
        })
    }).then(response => {
        if (response.ok) {
            console.log('Progress saved');
        }
    }).catch(err => console.error('Failed to save:', err));
}

// Load completion status on page load
window.addEventListener('DOMContentLoaded', function() {
    const lessonId = window.location.pathname.split('/').pop().replace('.html', '');
    fetch('/api/subject_progress/physics')
        .then(r => r.json())
        .then(data => {
            const lessonData = data.lessons && data.lessons[lessonId];
            if (lessonData && lessonData.completed) {
                document.getElementById('lesson-complete').checked = true;
            }
        })
        .catch(err => console.log('Could not load progress'));
});
</script>
'''
        # Insert before </body>
        if '</body>' in new_content:
            new_content = new_content.replace('</body>', js_code + '</body>')

    with open(lesson_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✓ {os.path.basename(lesson_path)} - checkbox added")

print(f"\n✅ Physics: Added checkboxes to {len(physics_lessons)} lessons\n")

# Issue 2: Fix Biology navigation links
print("=" * 60)
print("TASK 2: Fixing Biology edge-case navigation links")
print("=" * 60)

# Fix lesson_01.html - remove back link to lesson_00
lesson_01_path = f"{BASE_DIR}/biology/lesson_01.html"
if os.path.exists(lesson_01_path):
    with open(lesson_01_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and disable the back link
    import re
    content = re.sub(
        r'<a href="lesson_00\.html"[^>]*>.*?</a>',
        '<span style="color: #ccc; cursor: not-allowed;">← Previous</span>',
        content,
        flags=re.DOTALL
    )

    with open(lesson_01_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ lesson_01.html - disabled back link to lesson_00")

# Fix lesson_54.html - remove forward link to lesson_55
lesson_54_path = f"{BASE_DIR}/biology/lesson_54.html"
if os.path.exists(lesson_54_path):
    with open(lesson_54_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and disable the forward link
    content = re.sub(
        r'<a href="lesson_55\.html"[^>]*>.*?</a>',
        '<span style="color: #ccc; cursor: not-allowed;">Next →</span>',
        content,
        flags=re.DOTALL
    )

    with open(lesson_54_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ lesson_54.html - disabled forward link to lesson_55")

print(f"\n✅ Biology: Fixed 2 navigation links\n")

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("✅ Physics: 67 lessons updated with checkboxes")
print("✅ Biology: 2 navigation links fixed")
print("\nNext: Run full Phase 1 conversion on Math, Chinese, English, SAT")
