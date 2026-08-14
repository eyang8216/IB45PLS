#!/usr/bin/env python3
"""
Generate unified Biology index page with backend integration
"""

# Biology lesson data organized by themes
THEMES = [
    {
        "id": "themeA",
        "icon": "🔬",
        "title": "Theme A: Unity and Diversity",
        "count": 11,
        "lessons": [
            (1, "Water — the medium for life", "A.1.1", False),
            (2, "Nucleic Acids I — DNA structure and evidence", "A.1.2", False),
            (3, "Nucleic Acids II — RNA, nucleosomes", "A.1.3", True),
            (4, "Origin of Cells — Miller-Urey, RNA World, endosymbiosis", "A.1.4", True),
            (5, "Cell Structure I — prokaryotic vs. eukaryotic cells, organelles", "A.2.1", False),
            (6, "Cell Structure II — techniques, atypical cells, cytoskeleton", "A.2.2", True),
            (7, "Diversity of Organisms — variation, species concepts", "A.3.1", True),
            (8, "Classification and Cladistics — domains, cladograms, keys", "A.3.2", True),
            (9, "Evolution and Speciation I — evidence, natural selection", "A.4.1", True),
            (10, "Evolution and Speciation II — speciation, Hardy-Weinberg", "A.4.2", True),
            (11, "Conservation of Biodiversity — threats, strategies, CITES", "A.4.3", True),
        ]
    },
    {
        "id": "themeB",
        "icon": "🧪",
        "title": "Theme B: Form and Function",
        "count": 13,
        "lessons": [
            (12, "Carbohydrates and Lipids I — monosaccharides to polysaccharides", "B.1.1", False),
            (13, "Carbohydrates and Lipids II — phospholipids, steroids", "B.1.2", True),
            (14, "Proteins I — amino acids to tertiary structure", "B.1.3", False),
            (15, "Proteins II — quaternary structure, folding", "B.1.4", True),
            (16, "Membranes and Membrane Transport — fluid mosaic model", "B.2.1", False),
            (17, "Organelles and Compartmentalization", "B.2.2", True),
            (18, "Cell Specialization — stem cells, differentiation, iPSCs", "B.2.3", False),
            (19, "Gas Exchange I — Fick's Law, human ventilation, alveoli", "B.3.1", False),
            (20, "Gas Exchange II — plants, insects, fish, O₂ curves", "B.3.2", True),
            (21, "Transport I — circulatory systems, heart, cardiac cycle", "B.3.3", False),
            (22, "Transport II — blood, lymph, plant transport, ECG", "B.3.4", True),
            (23, "Muscle and Motility — sarcomere, sliding filament", "B.4.1", True),
            (24, "Adaptation to Environment and Ecological Niches", "B.4.2", False),
        ]
    },
    {
        "id": "themeC",
        "icon": "⚡",
        "title": "Theme C: Interaction and Interdependence",
        "count": 15,
        "lessons": [
            (25, "Energy in Ecosystems — producers, consumers, trophic levels", "C.1.1", False),
            (26, "Carbon Cycling — photosynthesis, respiration, decomposition", "C.1.2", False),
            (27, "Nitrogen and Phosphorus Cycles", "C.1.3", True),
            (28, "Climate Change and Ecosystems", "C.1.4", True),
            (29, "Populations and Communities — r/K strategies, succession", "C.2.1", False),
            (30, "Population Ecology Models — logistic growth, Lotka-Volterra", "C.2.2", True),
            (31, "Nervous System I — neurons, action potentials, synapses", "C.3.1", False),
            (32, "Nervous System II — CNS, PNS, brain regions", "C.3.2", True),
            (33, "Hormones and Homeostasis I — endocrine system, feedback loops", "C.3.3", False),
            (34, "Hormones and Homeostasis II — osmoregulation, thermoregulation", "C.3.4", True),
            (35, "Reproduction I — sexual vs. asexual, gametogenesis", "C.3.5", False),
            (36, "Reproduction II — menstrual cycle, fertilization, pregnancy", "C.3.6", True),
            (37, "Immunity I — innate and adaptive immunity", "C.4.1", False),
            (38, "Immunity II — antibodies, vaccines, HIV", "C.4.2", True),
            (39, "Diseases and Epidemiology", "C.4.3", True),
        ]
    },
    {
        "id": "themeD",
        "icon": "🧬",
        "title": "Theme D: Continuity and Change",
        "count": 15,
        "lessons": [
            (40, "DNA Replication — semiconservative, enzymes, PCR", "D.1.1", False),
            (41, "Gene Expression I — transcription, translation", "D.1.2", False),
            (42, "Gene Expression II — regulation, epigenetics", "D.1.3", True),
            (43, "Mutations and Genetic Variation", "D.1.4", True),
            (44, "Inheritance I — Mendel, monohybrid and dihybrid crosses", "D.2.1", False),
            (45, "Inheritance II — linkage, chi-squared, pedigrees", "D.2.2", True),
            (46, "Genetic Engineering and Biotechnology — CRISPR, GMOs", "D.2.3", False),
            (47, "Gene Pools and Natural Selection", "D.3.1", False),
            (48, "Phylogeny and Systematics", "D.3.2", True),
            (49, "Photosynthesis I — light-dependent reactions", "D.4.1", False),
            (50, "Photosynthesis II — Calvin cycle, C4 and CAM", "D.4.2", True),
            (51, "Cellular Respiration I — glycolysis, Krebs cycle", "D.4.3", False),
            (52, "Cellular Respiration II — electron transport chain, ATP yield", "D.4.4", True),
            (53, "Neural Development and Plasticity", "D.5.1", True),
            (54, "Astrobiology and the Search for Life", "D.5.2", True),
        ]
    }
]

def generate_html():
    """Generate the unified Biology index HTML"""

    lessons_html = ""

    for theme in THEMES:
        lessons_html += f'''
<!-- {theme["title"]} -->
<div class="topic-section" id="{theme["id"]}">
  <div class="topic-header" onclick="toggleSection(this)">
    <div>
      <h2>{theme["icon"]} {theme["title"]}</h2>
      <span class="topic-meta">{theme["count"]} lessons</span>
    </div>
    <span class="collapse-icon">▼</span>
  </div>
  <div class="topic-content">
'''

        for lesson_num, title, code, is_hl in theme["lessons"]:
            hl_badge = ' <span class="level-badge">HL</span>' if is_hl else ''
            lesson_id = f"lesson_{lesson_num:02d}"

            lessons_html += f'''    <div class="lesson-row" data-lesson-id="{lesson_id}">
      <div class="lesson-num">{lesson_num}</div>
      <div class="lesson-info">
        <div class="lesson-title">
          <a href="lesson_{lesson_num:02d}.html">{title}{hl_badge}</a>
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

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Biology HL — Course Index</title>
<link rel="stylesheet" href="../../static/subject_index.css">
</head>
<body>

<div class="container">
  <header class="page-header">
    <h1>🧬 Biology HL</h1>
    <p class="subtitle">54 lessons · HL · Target: Grade 7</p>
  </header>

  <div class="stats-bar">
    <div class="stat-card">
      <div class="stat-num" id="completed-count">0</div>
      <div class="stat-label">Completed</div>
    </div>
    <div class="stat-card">
      <div class="stat-num" id="remaining-count">54</div>
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
const SUBJECT_KEY = "biology";

// Cycle through mastery levels on click
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

// Load progress from backend
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

// Update completion status
async function toggleCompletion(lessonId, checkbox) {{
  const completed = checkbox.checked;

  try {{
    const response = await fetch('/toggle_completion', {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify({{
        subject: SUBJECT_KEY,
        lesson: lessonId,
        completed: completed
      }})
    }});

    if (response.ok) {{
      const row = checkbox.closest('.lesson-row');
      if (row) {{
        row.classList.toggle('completed', completed);
      }}
      updateStats();
    }}
  }} catch (e) {{
    console.error('Failed to save completion:', e);
    checkbox.checked = !completed;
  }}
}}

// Update mastery level
async function updateMastery(lessonId, level) {{
  try {{
    const response = await fetch('/update_mastery', {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify({{
        subject: SUBJECT_KEY,
        lesson: lessonId,
        level: level
      }})
    }});

    if (response.ok) {{
      updateStats();
    }}
  }} catch (e) {{
    console.error('Failed to update mastery:', e);
  }}
}}

// Update stats bar
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

// Search functionality
document.getElementById('search-input')?.addEventListener('input', (e) => {{
  const query = e.target.value.toLowerCase();
  const rows = document.querySelectorAll('.lesson-row');

  rows.forEach(row => {{
    const text = row.textContent.toLowerCase();
    row.style.display = text.includes(query) ? '' : 'none';
  }});
}});

// Expand/collapse sections
function expandAll() {{
  document.querySelectorAll('.topic-section').forEach(section => {{
    section.classList.remove('collapsed');
  }});
}}

function collapseAll() {{
  document.querySelectorAll('.topic-section').forEach(section => {{
    section.classList.add('collapsed');
  }});
}}

// Toggle individual sections
function toggleSection(element) {{
  const section = element.closest('.topic-section');
  section.classList.toggle('collapsed');
}}

// Mastery filter
function showMasteryFilter() {{
  const filter = prompt('Filter by mastery level:\\n0 = Not Started\\n1 = Learning\\n2 = Proficient\\n3 = Mastery\\n\\nEnter level (0-3) or leave empty to show all:');

  if (filter === null) return;

  const rows = document.querySelectorAll('.lesson-row');
  rows.forEach(row => {{
    if (filter === '') {{
      row.style.display = '';
    }} else {{
      const masteryBadge = row.querySelector('.mastery-badge');
      const level = masteryBadge?.dataset.level || '0';
      row.style.display = level === filter ? '' : 'none';
    }}
  }});
}}

// Initialize on page load
async function init() {{
  const progress = await loadProgress();

  // Restore checkboxes and mastery badges
  document.querySelectorAll('.lesson-checkbox').forEach(checkbox => {{
    const lessonId = checkbox.dataset.lessonId;
    const lessonData = progress.lessons?.[lessonId];

    if (lessonData) {{
      checkbox.checked = lessonData.completed || false;

      const row = checkbox.closest('.lesson-row');
      if (row) {{
        if (checkbox.checked) {{
          row.classList.add('completed');
        }}

        // Update mastery badge
        const masteryBadge = row.querySelector('.mastery-badge');
        if (masteryBadge && lessonData.mastery_level !== undefined) {{
          const level = lessonData.mastery_level;
          masteryBadge.dataset.level = level;
          masteryBadge.className = 'mastery-badge';

          const labels = ['Not Started', 'Learning', 'Proficient', 'Mastery'];
          const classes = ['not-started', 'learning', 'proficient', 'mastery'];

          masteryBadge.classList.add(classes[level]);
          masteryBadge.textContent = labels[level];
        }}
      }}
    }}
  }});

  // Load streak
  try {{
    const streakResponse = await fetch('/api/user_streak');
    if (streakResponse.ok) {{
      const streakData = await streakResponse.json();
      document.getElementById('streak-days').textContent = streakData.streak || 0;
    }}
  }} catch (e) {{
    console.error('Failed to load streak:', e);
  }}

  updateStats();
}}

// Run on page load
document.addEventListener('DOMContentLoaded', init);
</script>

</body>
</html>'''

    return html

if __name__ == "__main__":
    html = generate_html()
    output_path = "/Users/a3015110/Desktop/IB45PLS/subjects/biology/index_new.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Generated: {output_path}")
    print("📝 Review the file, then rename it to index.html to replace the old one")
