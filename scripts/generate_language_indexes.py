#!/usr/bin/env python3
"""
Generate unified index pages for Chinese, English, and SAT
"""
import os

SUBJECTS = {
    "chinese": {
        "name": "Chinese Lang & Lit SL",
        "emoji": "🇨🇳",
        "total": 7,
        "subfolder": "",
        "topics": [
            {
                "title": "Paper 1: Textual Analysis",
                "lessons": [
                    (1, "Guided Textual Analysis — Structure & Approach", "P1.1", False),
                    (2, "Literary Devices & Language Features", "P1.2", False),
                    (3, "Text Types — Articles, Speeches, Advertisements", "P1.3", False),
                ]
            },
            {
                "title": "Paper 2: Comparative Essay",
                "lessons": [
                    (4, "Comparative Analysis Techniques", "P2.1", False),
                    (5, "Essay Structure & Organization", "P2.2", False),
                ]
            },
            {
                "title": "Practice & Review",
                "lessons": [
                    (6, "Past Paper Practice — Paper 1", "Practice.1", False),
                    (7, "Past Paper Practice — Paper 2", "Practice.2", False),
                ]
            }
        ]
    },
    "english": {
        "name": "English Lang & Lit SL",
        "emoji": "🇬🇧",
        "total": 3,
        "subfolder": "",
        "topics": [
            {
                "title": "Paper 1: Guided Analysis",
                "lessons": [
                    (1, "Analyzing Unseen Texts — Non-Fiction", "P1.1", False),
                    (2, "Analyzing Unseen Texts — Literary Prose", "P1.2", False),
                ]
            },
            {
                "title": "Practice",
                "lessons": [
                    (3, "Past Paper Practice — Paper 1", "Practice.1", False),
                ]
            }
        ]
    },
    "sat": {
        "name": "SAT Prep",
        "emoji": "🎓",
        "total": 50,
        "subfolder": "",
        "topics": [
            {
                "title": "SAT Reading",
                "lessons": [
                    (i, f"Reading Lesson {i} — Comprehension & Evidence", f"R.{i}", False)
                    for i in range(1, 11)
                ]
            },
            {
                "title": "SAT Writing & Language",
                "lessons": [
                    (i, f"Writing Lesson {i-10} — Grammar & Style", f"W.{i-10}", False)
                    for i in range(11, 21)
                ]
            },
            {
                "title": "SAT Math (No Calculator)",
                "lessons": [
                    (i, f"Math Lesson {i-20} — Algebra & Problem Solving", f"M1.{i-20}", False)
                    for i in range(21, 31)
                ]
            },
            {
                "title": "SAT Math (Calculator)",
                "lessons": [
                    (i, f"Math Lesson {i-30} — Advanced Topics", f"M2.{i-30}", False)
                    for i in range(31, 41)
                ]
            },
            {
                "title": "Practice Tests",
                "lessons": [
                    (i, f"Full Practice Test {i-40}", f"Test.{i-40}", False)
                    for i in range(41, 51)
                ]
            }
        ]
    }
}

def generate_subject_html(subject_key, config):
    """Generate HTML for a subject index page"""

    subject_name = config["name"]
    emoji = config["emoji"]
    total = config["total"]
    subfolder = config.get("subfolder", "")

    # Build lessons HTML
    lessons_html = ""

    for topic in config["topics"]:
        topic_title = topic["title"]
        topic_id = f"topic{len(lessons_html) // 500 + 1}"

        topic_lessons = topic["lessons"]

        lessons_html += f'''
<!-- {topic_title} -->
<div class="topic-section" id="{topic_id}">
  <div class="topic-header" onclick="toggleSection(this)">
    <div>
      <h2>{topic_title}</h2>
      <span class="topic-meta">{len(topic_lessons)} lessons</span>
    </div>
    <span class="collapse-icon">▼</span>
  </div>
  <div class="topic-content">
'''

        for lesson_data in topic_lessons:
            num, title, code, is_hl = lesson_data
            hl_badge = ' <span class="level-badge">HL</span>' if is_hl else ''

            lesson_file = f"lesson_{num:02d}.html" if subfolder == "" else f"{subfolder}/lesson_{num:02d}.html"
            lesson_id = f"lesson_{num:02d}"

            lessons_html += f'''    <div class="lesson-row" data-lesson-id="{lesson_id}">
      <div class="lesson-num">{num}</div>
      <div class="lesson-info">
        <div class="lesson-title">
          <a href="{lesson_file}">{title}{hl_badge}</a>
        </div>
        <div class="lesson-code">{code}</div>
      </div>
      <span class="mastery-badge not-started" data-level="0" onclick="cycleMastery(this, '{lesson_id}')">Not Started</span>
      <input type="checkbox" class="lesson-checkbox" data-lesson-id="{lesson_id}" onchange="toggleCompletion('{lesson_id}', this)">
    </div>
'''

        lessons_html += '''  </div>
</div>
'''

    # Determine level badge text
    level_text = "SL" if "SL" in subject_name else "Prep"

    # Build full HTML
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
    <p class="subtitle">{total} lessons · {level_text} · Target: High Score</p>
  </header>

  <div class="stats-bar">
    <div class="stat-card">
      <div class="stat-num" id="completed-count">0</div>
      <div class="stat-label">Completed</div>
    </div>
    <div class="stat-card">
      <div class="stat-num" id="remaining-count">{total}</div>
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

if __name__ == "__main__":
    base_path = "/Users/a3015110/Desktop/IB45PLS/subjects"

    for subject_key, config in SUBJECTS.items():
        html = generate_subject_html(subject_key, config)
        output_path = os.path.join(base_path, subject_key, "index_new.html")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"✅ Generated: {subject_key}/index_new.html")

    print("\n📝 To apply changes, run:")
    print("cd subjects && for dir in chinese english sat; do mv $dir/index.html $dir/index_old.html && mv $dir/index_new.html $dir/index.html; done")
