#!/usr/bin/env python3
"""
Generate unified index pages with CORRECT actual filenames
"""
import os
import glob

BASE_DIR = "/Users/a3015110/Desktop/IB45PLS/subjects"

# Get actual lesson files and extract their info
def get_actual_lessons(subject_dir, pattern):
    """Get actual lesson files and extract titles"""
    files = sorted(glob.glob(f"{subject_dir}/{pattern}"))
    lessons = []

    for filepath in files:
        filename = os.path.basename(filepath)

        # Read first few lines to get title
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read(3000)

            # Extract title from h1 tag
            import re
            title_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
            if title_match:
                title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
                # Clean up lesson number prefix
                title = re.sub(r'^Lesson \d+[:\-—\s]+', '', title, flags=re.IGNORECASE)
            else:
                title = filename.replace('.html', '').replace('_', ' ').title()

            lessons.append({
                'filename': filename,
                'title': title,
                'number': len(lessons) + 1
            })
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            continue

    return lessons

# Economics lessons
print("Scanning Economics lessons...")
econ_lessons = get_actual_lessons(f"{BASE_DIR}/economics", "lesson_*.html")
print(f"Found {len(econ_lessons)} Economics lessons")

# Math lessons
print("Scanning Math lessons...")
math_lessons = get_actual_lessons(f"{BASE_DIR}/math", "lesson*.html")
print(f"Found {len(math_lessons)} Math lessons")

# Physics lessons
print("Scanning Physics lessons...")
physics_lessons = get_actual_lessons(f"{BASE_DIR}/physics", "L*.html")
print(f"Found {len(physics_lessons)} Physics lessons")

# Generate unified index HTML
def generate_unified_index(subject_key, subject_name, emoji, lessons, level="HL"):
    """Generate unified index HTML with actual lesson links"""

    lessons_html = ""

    # Group lessons by topic (every 10-15 lessons = 1 topic for simplicity)
    topic_size = 15
    for i in range(0, len(lessons), topic_size):
        topic_lessons = lessons[i:i+topic_size]
        topic_num = (i // topic_size) + 1

        lessons_html += f'''
<!-- Topic {topic_num} -->
<div class="topic-section" id="topic{topic_num}">
  <div class="topic-header" onclick="toggleSection(this)">
    <div>
      <h2>Topic {topic_num}</h2>
      <span class="topic-meta">{len(topic_lessons)} lessons</span>
    </div>
    <span class="collapse-icon">▼</span>
  </div>
  <div class="topic-content">
'''

        for lesson in topic_lessons:
            lesson_id = lesson['filename'].replace('.html', '')

            lessons_html += f'''    <div class="lesson-row" data-lesson-id="{lesson_id}">
      <div class="lesson-num">{lesson['number']}</div>
      <div class="lesson-info">
        <div class="lesson-title">
          <a href="{lesson['filename']}">{lesson['title']}</a>
        </div>
        <div class="lesson-code">{lesson['number']}</div>
      </div>
      <span class="mastery-badge not-started" data-level="0" onclick="cycleMastery(this, '{lesson_id}')">Not Started</span>
      <input type="checkbox" class="lesson-checkbox" data-lesson-id="{lesson_id}" onchange="toggleCompletion('{lesson_id}', this)">
    </div>
'''

        lessons_html += '''  </div>
</div>
'''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{subject_name} — Course Index</title>
<link rel="stylesheet" href="../../static/subject_index.css">
</head>
<body>

<div class="container">
  <header class="page-header">
    <h1>{emoji} {subject_name}</h1>
    <p class="subtitle">{len(lessons)} lessons · {level} · Target: Grade 7</p>
  </header>

  <div class="stats-bar">
    <div class="stat-card">
      <div class="stat-num" id="completed-count">0</div>
      <div class="stat-label">Completed</div>
    </div>
    <div class="stat-card">
      <div class="stat-num" id="remaining-count">{len(lessons)}</div>
      <div class="stat-label">Remaining</div>
    </div>
    <div class="stat-card">
      <div class="stat-num" id="progress-pct">0%</div>
      <div class="stat-label">Progress</div>
    </div>
    <div class="stat-card">
      <div class="stat-num" id="streak-days">0</div>
      <div class="stat-label">Day Streak</div>
    </div>
  </div>

  <div class="progress-bar-container">
    <div class="progress-bar" id="progress-bar-fill"></div>
  </div>

  <div class="controls">
    <input type="text" id="search-input" placeholder="Search lessons..." class="search-box">
    <div class="control-buttons">
      <button onclick="expandAll()" class="btn-secondary">Expand All</button>
      <button onclick="collapseAll()" class="btn-secondary">Collapse All</button>
      <button onclick="showMasteryFilter()" class="btn-secondary">Filter by Mastery</button>
    </div>
  </div>

  <div id="lessons-container">
{lessons_html}  </div>

  <div class="mastery-legend">
    <div class="legend-item">
      <span class="mastery-badge not-started">Not Started</span>
      <span>Haven't viewed yet</span>
    </div>
    <div class="legend-item">
      <span class="mastery-badge learning">Learning</span>
      <span>Currently studying</span>
    </div>
    <div class="legend-item">
      <span class="mastery-badge proficient">Proficient</span>
      <span>Understand the concepts</span>
    </div>
    <div class="legend-item">
      <span class="mastery-badge mastery">Mastery</span>
      <span>Can teach others</span>
    </div>
  </div>
</div>

<script>
const SUBJECT_KEY = "{subject_key}";

function cycleMastery(badge, lessonId) {{
  const currentLevel = parseInt(badge.dataset.level) || 0;
  const nextLevel = (currentLevel + 1) % 4;
  badge.dataset.level = nextLevel;
  badge.className = 'mastery-badge';
  const labels = ['Not Started', 'Learning', 'Proficient', 'Mastery'];
  const classes = ['not-started', 'learning', 'proficient', 'mastery'];
  badge.classList.add(classes[nextLevel]);
  badge.textContent = labels[nextLevel];
  updateMastery(lessonId, nextLevel);
}}

async function loadProgress() {{
  try {{
    const response = await fetch('/api/subject_progress/' + SUBJECT_KEY);
    if (!response.ok) return {{}};
    const data = await response.json();
    return data;
  }} catch (e) {{
    console.error('Failed to load progress:', e);
    return {{}};
  }}
}}

async function toggleCompletion(lessonId, checkbox) {{
  const completed = checkbox.checked;
  try {{
    const response = await fetch('/toggle_completion', {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify({{subject: SUBJECT_KEY, lesson: lessonId, completed: completed}})
    }});
    if (response.ok) {{
      const row = checkbox.closest('.lesson-row');
      if (row) row.classList.toggle('completed', completed);
      updateStats();
    }}
  }} catch (e) {{
    console.error('Failed to save completion:', e);
    checkbox.checked = !completed;
  }}
}}

async function updateMastery(lessonId, level) {{
  try {{
    await fetch('/update_mastery', {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify({{subject: SUBJECT_KEY, lesson: lessonId, level: level}})
    }});
    updateStats();
  }} catch (e) {{
    console.error('Failed to update mastery:', e);
  }}
}}

function updateStats() {{
  const checkboxes = document.querySelectorAll('.lesson-checkbox');
  const total = checkboxes.length;
  const completed = Array.from(checkboxes).filter(cb => cb.checked).length;
  const remaining = total - completed;
  const pct = total > 0 ? Math.round((completed / total) * 100) : 0;
  document.getElementById('completed-count').textContent = completed;
  document.getElementById('remaining-count').textContent = remaining;
  document.getElementById('progress-pct').textContent = pct + '%';
  document.getElementById('progress-bar-fill').style.width = pct + '%';
}}

document.getElementById('search-input')?.addEventListener('input', (e) => {{
  const query = e.target.value.toLowerCase();
  document.querySelectorAll('.lesson-row').forEach(row => {{
    row.style.display = row.textContent.toLowerCase().includes(query) ? '' : 'none';
  }});
}});

function expandAll() {{
  document.querySelectorAll('.topic-section').forEach(s => s.classList.remove('collapsed'));
}}

function collapseAll() {{
  document.querySelectorAll('.topic-section').forEach(s => s.classList.add('collapsed'));
}}

function toggleSection(element) {{
  element.closest('.topic-section').classList.toggle('collapsed');
}}

function showMasteryFilter() {{
  const filter = prompt('Filter by mastery level:\\n0 = Not Started\\n1 = Learning\\n2 = Proficient\\n3 = Mastery\\n\\nEnter level (0-3) or leave empty to show all:');
  if (filter === null) return;
  document.querySelectorAll('.lesson-row').forEach(row => {{
    if (filter === '') {{
      row.style.display = '';
    }} else {{
      const badge = row.querySelector('.mastery-badge');
      const level = badge?.dataset.level || '0';
      row.style.display = level === filter ? '' : 'none';
    }}
  }});
}}

async function init() {{
  const progress = await loadProgress();
  document.querySelectorAll('.lesson-checkbox').forEach(checkbox => {{
    const lessonId = checkbox.dataset.lessonId;
    const lessonData = progress.lessons?.[lessonId];
    if (lessonData) {{
      checkbox.checked = lessonData.completed || false;
      const row = checkbox.closest('.lesson-row');
      if (row && checkbox.checked) row.classList.add('completed');
      const badge = row?.querySelector('.mastery-badge');
      if (badge && lessonData.mastery_level !== undefined) {{
        const level = lessonData.mastery_level;
        badge.dataset.level = level;
        badge.className = 'mastery-badge';
        const labels = ['Not Started', 'Learning', 'Proficient', 'Mastery'];
        const classes = ['not-started', 'learning', 'proficient', 'mastery'];
        badge.classList.add(classes[level]);
        badge.textContent = labels[level];
      }}
    }}
  }});
  try {{
    const streakResponse = await fetch('/api/user_streak');
    if (streakResponse.ok) {{
      const streakData = await streakResponse.json();
      document.getElementById('streak-days').textContent = streakData.streak || 0;
    }}
  }} catch (e) {{}}
  updateStats();
}}

document.addEventListener('DOMContentLoaded', init);
</script>

</body>
</html>'''

    return html

# Generate and save
print("\nGenerating unified indexes with correct filenames...")

# Economics
econ_html = generate_unified_index("economics", "Economics HL", "📊", econ_lessons)
with open(f"{BASE_DIR}/economics/index.html", 'w', encoding='utf-8') as f:
    f.write(econ_html)
print("✓ Economics index.html")

# Math
math_html = generate_unified_index("math", "Math AA HL", "📐", math_lessons)
with open(f"{BASE_DIR}/math/index.html", 'w', encoding='utf-8') as f:
    f.write(math_html)
print("✓ Math index.html")

# Physics
physics_html = generate_unified_index("physics", "Physics HL", "⚛️", physics_lessons)
with open(f"{BASE_DIR}/physics/index.html", 'w', encoding='utf-8') as f:
    f.write(physics_html)
print("✓ Physics index.html")

print("\n✅ All unified index pages regenerated with correct filenames!")
