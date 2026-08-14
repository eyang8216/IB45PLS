# Phase 3: Content Verification Plan

## Objective
Verify all 327 lesson HTML files across 8 subjects for:
- Content integrity (no broken HTML)
- LaTeX/MathJax rendering
- IB syllabus alignment
- Link integrity
- Image alt text and accessibility
- Accurate scientific content

## Verification Strategy

### Approach: Parallel Subagent Verification
Spawn 8 subject-specific subagents in parallel, each verifying their subject's lessons.

### Subagent Tasks
Each subagent will:
1. Read all lesson files for their subject
2. Check for common issues:
   - Broken HTML tags
   - Missing or malformed LaTeX (`$...$`, `$$...$$`)
   - Broken internal links
   - Missing images or alt text
   - Incomplete content sections
3. Verify key IB concepts are present (using syllabus_mappings.py)
4. Return structured findings report

### Subject Distribution
- **Biology Agent**: 54 lessons (subjects/biology/lesson_*.html)
- **Chemistry Agent**: 41 lessons (subjects/chemistry/lessons/lesson_*.html)
- **Physics Agent**: 67 lessons (subjects/physics/L*.html)
- **Math Agent**: 50 lessons (subjects/math/lesson*.html)
- **Economics Agent**: 65 lessons (subjects/economics/lesson_*.html)
- **Chinese Agent**: 7 lessons (subjects/chinese/lesson_*.html)
- **English Agent**: 3 lessons (subjects/english/lesson_*.html)
- **SAT Agent**: 50 lessons (subjects/sat/lesson_*.html)

### Verification Checklist per Lesson

#### 1. HTML Structure
- [ ] Valid HTML5 structure
- [ ] All opening tags have closing tags
- [ ] No unclosed `<div>`, `<span>`, `<p>` tags
- [ ] Proper heading hierarchy (h1 → h2 → h3)

#### 2. LaTeX/MathJax
- [ ] All math expressions properly delimited (`$...$` or `$$...$$`)
- [ ] No unescaped special characters in math mode
- [ ] Complex equations use `\begin{align}...\end{align}` correctly
- [ ] Chemical formulas use `\ce{...}` (for Chemistry)

#### 3. Content Quality
- [ ] Lesson has clear learning objectives
- [ ] Content matches IB syllabus topic
- [ ] Examples are present and relevant
- [ ] Key terms are defined or explained
- [ ] No obvious factual errors

#### 4. Links & Media
- [ ] All internal links point to existing files
- [ ] External links are relevant (not broken check, just relevance)
- [ ] Images have descriptive alt text
- [ ] Image file paths are correct

#### 5. Interactive Elements (from Phase 1)
- [ ] Completion checkbox present
- [ ] Generate Flashcards button present
- [ ] Practice Problems button present
- [ ] Ask AI button present
- [ ] JavaScript event handlers attached

### Output Format

Each subagent returns JSON:
```json
{
  "subject": "biology",
  "total_lessons": 54,
  "lessons_checked": 54,
  "issues_found": 3,
  "findings": [
    {
      "lesson": "lesson_23.html",
      "severity": "medium",
      "category": "latex",
      "description": "Unclosed LaTeX delimiter in equation on line 145",
      "line": 145
    }
  ],
  "summary": {
    "html_issues": 0,
    "latex_issues": 2,
    "content_issues": 1,
    "link_issues": 0,
    "accessibility_issues": 0
  }
}
```

### Severity Levels
- **Critical**: Broken HTML, page won't render
- **High**: LaTeX errors, broken internal links, missing content
- **Medium**: Missing alt text, minor formatting issues
- **Low**: Stylistic improvements, optional enhancements

### Aggregated Report Structure

```markdown
# Content Verification Report

**Date**: 2026-08-14
**Total Lessons Verified**: 327
**Issues Found**: X
**Status**: [PASS / NEEDS FIXES]

## Summary by Subject

| Subject | Lessons | Critical | High | Medium | Low | Status |
|---------|---------|----------|------|--------|-----|--------|
| Biology | 54 | 0 | 2 | 5 | 3 | ⚠️ |
| Chemistry | 41 | 0 | 1 | 3 | 2 | ⚠️ |
| ... | ... | ... | ... | ... | ... | ... |

## Critical Issues (Immediate Action Required)

[List of critical issues if any]

## High Priority Issues

[List of high priority issues]

## Medium Priority Issues

[Summary statistics, not full list]

## Low Priority Issues

[Summary statistics, not full list]

## Detailed Findings by Subject

### Biology HL
- Total: 54 lessons
- Issues: 10 (2 high, 5 medium, 3 low)
- Files: [list of files with issues]

[Detailed list]

### Chemistry HL
...

## Recommendations

1. Fix all critical issues immediately
2. Address high-priority LaTeX errors
3. Add missing alt text (medium priority)
4. Consider stylistic improvements (low priority)

## Next Steps

1. Review this report
2. Create fix tasks for critical/high issues
3. Re-verify after fixes
4. Proceed to deployment
```

### Workflow Script

```python
#!/usr/bin/env python3
"""
Phase 3: Content Verification Workflow
Spawn 8 subagents in parallel to verify all lessons
"""

import asyncio
from workflow import Workflow

subjects = [
    ("biology", 54, "subjects/biology/lesson_*.html"),
    ("chemistry", 41, "subjects/chemistry/lessons/lesson_*.html"),
    ("physics", 67, "subjects/physics/L*.html"),
    ("math", 50, "subjects/math/lesson*.html"),
    ("economics", 65, "subjects/economics/lesson_*.html"),
    ("chinese", 7, "subjects/chinese/lesson_*.html"),
    ("english", 3, "subjects/english/lesson_*.html"),
    ("sat", 50, "subjects/sat/lesson_*.html"),
]

async def main():
    results = await asyncio.gather(*[
        verify_subject(name, count, pattern)
        for name, count, pattern in subjects
    ])
    
    # Aggregate results
    total_issues = sum(r['issues_found'] for r in results)
    
    # Generate report
    generate_report(results, total_issues)

if __name__ == "__main__":
    asyncio.run(main())
```

## Execution Plan

1. **Spawn 8 Subagents** (parallel)
   - Each agent gets: subject name, lesson count, file pattern
   - Each agent reads all lessons for their subject
   - Each agent returns findings JSON

2. **Aggregate Results**
   - Combine all JSON findings
   - Calculate total issues by severity
   - Group by subject and category

3. **Generate Report**
   - Create VERIFICATION_REPORT.md
   - Include summary tables
   - List all findings with file:line references
   - Provide recommendations

4. **User Review**
   - User reviews report
   - Decides which issues to fix
   - Prioritizes critical/high issues

5. **Fix Issues** (if needed)
   - Create fix tasks
   - Re-verify after fixes
   - Update report

6. **Proceed to Deployment**
   - If no critical issues, ready to deploy
   - If fixes made, re-test
   - Deploy to PythonAnywhere

## Estimated Time

- Subagent verification: ~10-15 minutes (parallel)
- Report generation: ~2 minutes
- User review: 5-10 minutes
- **Total: ~20-30 minutes**

## Ready to Execute

Waiting for user confirmation to proceed with Phase 3 verification.
