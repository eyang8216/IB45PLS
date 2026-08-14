#!/usr/bin/env python3
"""
Generate unified index pages for all remaining subjects
"""
import os
import re

# Subject configurations with lesson data
SUBJECTS = {
    "chemistry": {
        "name": "Chemistry HL",
        "emoji": "🧪",
        "total": 41,
        "subfolder": "lessons",
        "topics": [
            {
                "title": "Topic 1: Stoichiometric Relationships",
                "lessons": [(1, "Stoichiometry Review — Moles, Formulas, Yield, Gases", "1.1", False)]
            },
            {
                "title": "Topic 2: Atomic Structure",
                "lessons": [
                    (2, "Subatomic Particles, Isotopes & Mass Spectrometry", "2.1", False),
                    (3, "Electron Configuration — Orbitals, Aufbau, Hund, Pauli", "2.2", False),
                    (4, "Atomic Emission Spectra — Hydrogen Spectrum & Convergence", "2.3", False),
                    (5, "Ionisation Energy I — First IE, Periodic Trends", "2.4", False),
                    (6, "Ionisation Energy II — Successive IE, Anomalies, Group ID", "2.5", True),
                    (7, "Atomic Structure Review — IB-Style Problem Set", "2.6", False),
                ]
            },
            {
                "title": "Topic 3: Periodicity & Bonding",
                "lessons": [
                    (8, "The Periodic Table & Periodic Trends", "3.1", False),
                    (9, "Ionic & Covalent Bonding — Lewis Structures, Formal Charge", "3.2", False),
                    (10, "VSEPR Theory — Molecular Shapes & Bond Angles", "3.3", False),
                    (11, "Polarity & Intermolecular Forces", "3.4", False),
                    (12, "Metallic Bonding, Giant Covalent, σ/π Bonds, Hybridisation", "3.5", True),
                    (13, "Transition Metals — Complex Ions, Colour, Crystal Field Theory", "3.6", True),
                ]
            },
            {
                "title": "Topic 4: Energetics",
                "lessons": [
                    (14, "Enthalpy Changes — Definitions, Calorimetry, q = mcΔT", "4.1", False),
                    (15, "Hess's Law — Enthalpy Cycles, ΔHf⦵ & ΔHc⦵", "4.2", False),
                    (16, "Bond Enthalpies & Energy Profiles", "4.3", False),
                    (17, "Born-Haber Cycles & Enthalpy of Solution", "4.4", True),
                    (18, "Entropy, Gibbs Free Energy & Spontaneity", "4.5", True),
                ]
            },
            {
                "title": "Topic 5: Chemical Kinetics",
                "lessons": [
                    (19, "Rate of Reaction & Collision Theory", "5.1", False),
                    (20, "Factors Affecting Rate & Maxwell-Boltzmann Distribution", "5.2", False),
                    (21, "Rate Laws & Reaction Order", "5.3", True),
                    (22, "Activation Energy & Arrhenius Equation", "5.4", True),
                ]
            },
            {
                "title": "Topic 6: Chemical Equilibrium",
                "lessons": [
                    (23, "Reversible Reactions & Dynamic Equilibrium", "6.1", False),
                    (24, "Le Chatelier's Principle & Equilibrium Position", "6.2", False),
                    (25, "Equilibrium Constant Kc & Calculations", "6.3", True),
                ]
            },
            {
                "title": "Topic 7: Acids & Bases",
                "lessons": [
                    (26, "Brønsted-Lowry Theory & Conjugate Pairs", "7.1", False),
                    (27, "pH Calculations & Strong vs. Weak Acids", "7.2", False),
                    (28, "pH Curves & Indicators", "7.3", True),
                    (29, "Buffer Solutions & Henderson-Hasselbalch", "7.4", True),
                ]
            },
            {
                "title": "Topic 8: Redox Processes",
                "lessons": [
                    (30, "Oxidation Numbers & Redox Reactions", "8.1", False),
                    (31, "Electrochemical Cells & Standard Electrode Potentials", "8.2", False),
                    (32, "Electrolysis & Faraday's Laws", "8.3", True),
                ]
            },
            {
                "title": "Topic 9: Organic Chemistry I",
                "lessons": [
                    (33, "Nomenclature & Functional Groups", "9.1", False),
                    (34, "Alkanes, Alkenes, Alkynes — Structure & Reactions", "9.2", False),
                    (35, "Alcohols, Halogenoalkanes, Carbonyl Compounds", "9.3", False),
                    (36, "Reaction Mechanisms — SN1, SN2, E1, E2", "9.4", True),
                ]
            },
            {
                "title": "Topic 10: Organic Chemistry II (HL)",
                "lessons": [
                    (37, "Aromatic Compounds & Benzene Reactions", "10.1", True),
                    (38, "Stereoisomerism — Optical & Geometric", "10.2", True),
                    (39, "Synthesis Routes & Retrosynthesis", "10.3", True),
                    (40, "Spectroscopy — IR, NMR, Mass Spec", "10.4", True),
                    (41, "Green Chemistry & Atom Economy", "10.5", True),
                ]
            },
        ]
    },
    "physics": {
        "name": "Physics HL",
        "emoji": "⚛️",
        "total": 67,
        "subfolder": "",
        "lesson_prefix": "L",
        "topics": [
            {"title": "Topic 1: Measurements & Uncertainties", "count": 5},
            {"title": "Topic 2: Mechanics", "count": 12},
            {"title": "Topic 3: Thermal Physics", "count": 8},
            {"title": "Topic 4: Waves", "count": 10},
            {"title": "Topic 5: Electricity & Magnetism", "count": 14},
            {"title": "Topic 6: Circular Motion & Gravitation", "count": 6},
            {"title": "Topic 7: Atomic, Nuclear & Particle Physics", "count": 8},
            {"title": "Topic 8: Energy Production", "count": 4},
        ]
    },
    "math": {
        "name": "Math AA HL",
        "emoji": "📐",
        "total": 50,
        "subfolder": "",
        "topics": [
            {"title": "Topic 1: Number & Algebra", "count": 12},
            {"title": "Topic 2: Functions", "count": 10},
            {"title": "Topic 3: Geometry & Trigonometry", "count": 10},
            {"title": "Topic 4: Statistics & Probability", "count": 10},
            {"title": "Topic 5: Calculus", "count": 8},
        ]
    },
    "economics": {
        "name": "Economics HL",
        "emoji": "📊",
        "total": 67,
        "subfolder": "",
        "topics": [
            {"title": "Unit 1: Microeconomics", "count": 18},
            {"title": "Unit 2: Macroeconomics", "count": 16},
            {"title": "Unit 3: International Economics", "count": 14},
            {"title": "Unit 4: Development Economics", "count": 12},
            {"title": "HL Extensions", "count": 7},
        ]
    }
}

def generate_subject_html(subject_key, config):
    """Generate HTML for a subject index page"""

    subject_name = config["name"]
    emoji = config["emoji"]
    total = config["total"]
    subfolder = config.get("subfolder", "")
    lesson_prefix = config.get("lesson_prefix", "lesson_")

    # Build lessons HTML
    lessons_html = ""
    lesson_num = 1

    for topic in config["topics"]:
        topic_title = topic["title"]
        topic_id = f"topic{len(lessons_html) // 500 + 1}"  # Simple ID generation

        # Get lessons for this topic
        if "lessons" in topic:
            topic_lessons = topic["lessons"]
        else:
            # Generate placeholder lessons for topics without detailed data
            count = topic.get("count", 5)
            topic_lessons = [(lesson_num + i, f"Lesson {lesson_num + i}", f"{lesson_num + i}", False)
                           for i in range(count)]

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

            # Build lesson filename
            if subfolder:
                lesson_file = f"{subfolder}/{lesson_prefix}{num:02d}.html"
            else:
                if lesson_prefix == "L":
                    lesson_file = f"L{num}.html"
                else:
                    lesson_file = f"{lesson_prefix}{num:02d}.html"

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
            lesson_num = num + 1

        lessons_html += '''  </div>
</div>
'''

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
    <p class="subtitle">{total} lessons · HL · Target: Grade 7</p>
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

    print("\n📝 Review the files, then run:")
    print("cd subjects && for dir in chemistry physics math economics; do mv $dir/index.html $dir/index_old.html && mv $dir/index_new.html $dir/index.html; done")
