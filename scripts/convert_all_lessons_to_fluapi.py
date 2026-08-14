#!/usr/bin/env python3
"""
Convert ALL lesson HTML files to unified Fluapi design with working progress tracking
"""
import os
import re
import glob

BASE_DIR = "/Users/a3015110/Desktop/IB45PLS/subjects"

# Subject metadata for navigation
SUBJECTS = {
    "biology": {"name": "Biology HL", "icon": "🧬", "key": "biology"},
    "chemistry": {"name": "Chemistry HL", "icon": "🧪", "key": "chemistry"},
    "economics": {"name": "Economics HL", "icon": "📊", "key": "economics"},
    "math": {"name": "Math AA HL", "icon": "📐", "key": "math"},
    "physics": {"name": "Physics HL", "icon": "⚛️", "key": "physics"},
}

def extract_lesson_id(filename):
    """Extract lesson ID from filename"""
    # Remove .html extension
    return filename.replace('.html', '')

def extract_content(html):
    """Extract body content from HTML"""
    # Remove everything before <body> and after </body>
    body_match = re.search(r'<body[^>]*>(.*)</body>', html, re.DOTALL | re.IGNORECASE)
    if body_match:
        content = body_match.group(1)
    else:
        content = html

    # Remove old completion checkbox if exists
    content = re.sub(r'<div class="lesson-completion".*?</div>\s*', '', content, flags=re.DOTALL)

    # Remove old nav if exists
    content = re.sub(r'<div class="nav".*?</div>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<nav.*?</nav>\s*', '', content, flags=re.DOTALL)

    return content.strip()

def extract_title(html):
    """Extract h1 title from HTML"""
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
    if title_match:
        title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
        return title

    # Fallback: try <title> tag
    title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
    if title_match:
        title = title_match.group(1).strip()
        # Remove "— IB Biology HL" etc
        title = re.sub(r'\s*[—–-]\s*IB.*$', '', title)
        return title

    return "Lesson"

def generate_fluapi_lesson(content, title, subject_key, subject_name, lesson_id):
    """Generate Fluapi-style lesson HTML"""

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — {subject_name}</title>
<script>window.MathJax = {{ tex: {{ inlineMath: [['$','$'], ['\\\\(','\\\\)']], displayMath: [['$$','$$'], ['\\\\[','\\\\]']] }} }};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>
<link rel="stylesheet" href="/static/lesson.css">
<style>
/* Additional lesson-specific overrides if needed */
.lesson-actions {{
  display: flex;
  gap: 1rem;
  margin: 2rem 0;
  flex-wrap: wrap;
}}

.lesson-actions button {{
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}}

.lesson-actions button:hover {{
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}}
</style>
</head>
<body>

<!-- Navigation Bar -->
<nav class="lesson-nav">
  <div class="nav-left">
    <a href="/" class="nav-home">🏠 Home</a>
    <span class="nav-separator">›</span>
    <a href="/subjects/{subject_key}/" class="nav-subject">{subject_name}</a>
  </div>
  <div class="nav-right">
    <button onclick="openAI()" class="nav-btn">💬 Ask AI</button>
    <button onclick="generatePractice()" class="nav-btn">✏️ Practice</button>
    <a href="/dashboard" class="nav-btn">📊 Progress</a>
    <a href="/how-to-use" class="nav-btn">❓ How to Use</a>
  </div>
</nav>

<!-- Lesson Header with Completion -->
<header class="lesson-header">
  <div class="lesson-completion-bar">
    <label class="completion-checkbox">
      <input type="checkbox" id="lesson-complete" data-subject="{subject_key}" data-lesson="{lesson_id}">
      <span>✓ Mark as complete</span>
    </label>
    <div class="mastery-selector">
      <label>Mastery:</label>
      <select id="mastery-level" data-subject="{subject_key}" data-lesson="{lesson_id}">
        <option value="0">Not Started</option>
        <option value="1">Learning</option>
        <option value="2">Proficient</option>
        <option value="3">Mastery</option>
      </select>
    </div>
  </div>
  <h1>{title}</h1>
</header>

<!-- Main Content -->
<main class="lesson-content">
{content}

<!-- Interactive Actions -->
<div class="lesson-actions">
  <button onclick="generateFlashcards()">🃏 Generate Flashcards</button>
  <button onclick="generatePractice()">📝 Practice Problems</button>
  <button onclick="openAI()">🤖 Ask AI Tutor</button>
</div>

</main>

<!-- Footer Navigation -->
<footer class="lesson-footer">
  <a href="/subjects/{subject_key}/" class="footer-link">← Back to {subject_name} Index</a>
  <a href="/dashboard" class="footer-link">View Dashboard →</a>
</footer>

<script>
const SUBJECT = "{subject_key}";
const LESSON_ID = "{lesson_id}";

// Load saved progress on page load
async function loadProgress() {{
  try {{
    const response = await fetch(`/api/subject_progress/${{SUBJECT}}`);
    if (!response.ok) return;
    const data = await response.json();
    const lessonData = data.lessons?.[LESSON_ID];

    if (lessonData) {{
      // Set checkbox
      const checkbox = document.getElementById('lesson-complete');
      if (checkbox) checkbox.checked = lessonData.completed || false;

      // Set mastery level
      const masterySelect = document.getElementById('mastery-level');
      if (masterySelect && lessonData.mastery_level !== undefined) {{
        masterySelect.value = lessonData.mastery_level;
      }}
    }}
  }} catch (e) {{
    console.error('Failed to load progress:', e);
  }}
}}

// Save completion status
document.getElementById('lesson-complete')?.addEventListener('change', async (e) => {{
  const completed = e.target.checked;
  try {{
    const response = await fetch('/toggle_completion', {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify({{
        subject: SUBJECT,
        lesson: LESSON_ID,
        completed: completed
      }})
    }});

    if (!response.ok) {{
      console.error('Failed to save completion');
      e.target.checked = !completed; // Revert on error
    }}
  }} catch (err) {{
    console.error('Error saving completion:', err);
    e.target.checked = !completed;
  }}
}});

// Save mastery level
document.getElementById('mastery-level')?.addEventListener('change', async (e) => {{
  const level = parseInt(e.target.value);
  try {{
    const response = await fetch('/update_mastery', {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify({{
        subject: SUBJECT,
        lesson: LESSON_ID,
        level: level
      }})
    }});

    if (!response.ok) {{
      console.error('Failed to save mastery level');
    }}
  }} catch (err) {{
    console.error('Error saving mastery:', err);
  }}
}});

// Interactive button handlers
function generateFlashcards() {{
  alert('Flashcard generation coming soon!');
}}

function generatePractice() {{
  alert('Practice problem generation coming soon!');
}}

function openAI() {{
  alert('AI Tutor coming soon!');
}}

// Load progress when page loads
document.addEventListener('DOMContentLoaded', loadProgress);
</script>

</body>
</html>'''

    return html

def convert_lesson_file(filepath, subject_key, subject_name):
    """Convert a single lesson file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_html = f.read()

        # Extract components
        title = extract_title(original_html)
        content = extract_content(original_html)
        filename = os.path.basename(filepath)
        lesson_id = extract_lesson_id(filename)

        # Generate new Fluapi HTML
        new_html = generate_fluapi_lesson(content, title, subject_key, subject_name, lesson_id)

        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)

        return True
    except Exception as e:
        print(f"ERROR converting {filepath}: {e}")
        return False

# Main conversion loop
print("Starting lesson conversion to Fluapi style...\n")

total_converted = 0
total_failed = 0

for subject_key, subject_info in SUBJECTS.items():
    subject_dir = f"{BASE_DIR}/{subject_key}"
    subject_name = subject_info['name']

    print(f"Processing {subject_name}...")

    # Find all lesson HTML files
    patterns = [
        f"{subject_dir}/lesson*.html",
        f"{subject_dir}/L*.html",
        f"{subject_dir}/lessons/lesson*.html",
    ]

    lesson_files = []
    for pattern in patterns:
        lesson_files.extend(glob.glob(pattern))

    # Remove duplicates and index files
    lesson_files = list(set(lesson_files))
    lesson_files = [f for f in lesson_files if 'index' not in os.path.basename(f).lower()]

    print(f"  Found {len(lesson_files)} lesson files")

    converted = 0
    failed = 0

    for filepath in lesson_files:
        if convert_lesson_file(filepath, subject_key, subject_name):
            converted += 1
        else:
            failed += 1

    print(f"  ✓ Converted: {converted}")
    if failed > 0:
        print(f"  ✗ Failed: {failed}")

    total_converted += converted
    total_failed += failed
    print()

print("="*60)
print(f"CONVERSION COMPLETE")
print(f"Total converted: {total_converted}")
print(f"Total failed: {total_failed}")
print("="*60)
