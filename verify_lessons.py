#!/usr/bin/env python3
"""Verify economics lessons for content quality."""

import re
import json
from pathlib import Path
from html.parser import HTMLParser
from collections import defaultdict

class LessonValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.issues = []
        self.tag_stack = []
        self.headings = []
        self.has_learning_objectives = False
        self.has_examples = False
        self.has_completion_checkbox = False
        self.has_flashcards_button = False
        self.has_practice_button = False
        self.has_ai_button = False
        self.images = []
        self.links = []
        self.current_line = 1
        self.line_map = {}

    def feed(self, data):
        # Create a line map for error reporting
        lines = data.split('\n')
        pos = 0
        for i, line in enumerate(lines, 1):
            self.line_map[pos] = i
            pos += len(line) + 1
        super().feed(data)

    def get_line_number(self, pos):
        """Approximate line number from character position."""
        for start_pos, line_num in sorted(self.line_map.items(), reverse=True):
            if pos >= start_pos:
                return line_num
        return 1

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append((tag, self.getpos()[0]))
        attrs_dict = dict(attrs)

        # Check headings
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(tag[1])
            self.headings.append(level)

        # Check for learning objectives
        if 'class' in attrs_dict and 'learning-objective' in attrs_dict.get('class', ''):
            self.has_learning_objectives = True

        # Check for example sections
        if 'class' in attrs_dict and 'example' in attrs_dict.get('class', '').lower():
            self.has_examples = True

        # Check for interactive elements
        if tag == 'input' and attrs_dict.get('type') == 'checkbox' and 'lesson-complete' in attrs_dict.get('id', ''):
            self.has_completion_checkbox = True

        # Check for buttons
        if tag == 'button' or (tag == 'a' and 'btn' in attrs_dict.get('class', '')):
            text_indicators = ['flashcard', 'practice', 'ai']
            # We'll check text content in handle_data

        # Check images
        if tag == 'img':
            src = attrs_dict.get('src', '')
            alt = attrs_dict.get('alt', '')
            if not alt:
                self.issues.append({
                    'line': self.getpos()[0],
                    'severity': 'medium',
                    'category': 'accessibility',
                    'description': f'Image missing alt text: {src}'
                })
            self.images.append({'src': src, 'alt': alt, 'line': self.getpos()[0]})

        # Check links
        if tag == 'a':
            href = attrs_dict.get('href', '')
            self.links.append({'href': href, 'line': self.getpos()[0]})

    def handle_endtag(self, tag):
        if self.tag_stack and self.tag_stack[-1][0] == tag:
            self.tag_stack.pop()
        else:
            # Mismatched tag
            self.issues.append({
                'line': self.getpos()[0],
                'severity': 'critical',
                'category': 'html',
                'description': f'Mismatched closing tag: </{tag}>'
            })

    def handle_data(self, data):
        data_lower = data.lower()
        if 'flashcard' in data_lower:
            self.has_flashcards_button = True
        if 'practice' in data_lower:
            self.has_practice_button = True
        if 'ai' in data_lower or 'tutor' in data_lower:
            self.has_ai_button = True

    def check_unclosed_tags(self):
        """Check for unclosed tags at end of document."""
        for tag, line in self.tag_stack:
            if tag not in ['br', 'hr', 'img', 'input', 'meta', 'link']:
                self.issues.append({
                    'line': line,
                    'severity': 'critical',
                    'category': 'html',
                    'description': f'Unclosed tag: <{tag}>'
                })

    def check_heading_hierarchy(self):
        """Check that headings follow proper hierarchy."""
        if not self.headings:
            return

        prev_level = 0
        for i, level in enumerate(self.headings):
            if prev_level > 0 and level > prev_level + 1:
                self.issues.append({
                    'line': None,
                    'severity': 'medium',
                    'category': 'html',
                    'description': f'Heading hierarchy skip: h{prev_level} to h{level}'
                })
            prev_level = level

def check_latex(content, filepath):
    """Check LaTeX/MathJax syntax."""
    issues = []
    lines = content.split('\n')

    # Check for proper delimiters
    inline_math = re.finditer(r'\$([^\$]+)\$', content, re.DOTALL)
    display_math = re.finditer(r'\$\$([^\$]+)\$\$', content, re.DOTALL)

    # Find line numbers for math expressions
    for match in inline_math:
        math_content = match.group(1)
        start_pos = match.start()
        line_num = content[:start_pos].count('\n') + 1

        # Check for common LaTeX errors
        if '\\frac{' in math_content and math_content.count('{') != math_content.count('}'):
            issues.append({
                'line': line_num,
                'severity': 'high',
                'category': 'latex',
                'description': f'Unbalanced braces in LaTeX: {match.group(0)[:50]}...'
            })

        # Check for unescaped special characters
        if '&' in math_content and '\\&' not in math_content and 'align' not in math_content:
            issues.append({
                'line': line_num,
                'severity': 'medium',
                'category': 'latex',
                'description': f'Unescaped ampersand in math mode'
            })

    for match in display_math:
        math_content = match.group(1)
        start_pos = match.start()
        line_num = content[:start_pos].count('\n') + 1

        if '\\frac{' in math_content and math_content.count('{') != math_content.count('}'):
            issues.append({
                'line': line_num,
                'severity': 'high',
                'category': 'latex',
                'description': f'Unbalanced braces in display math'
            })

    # Check for naked math (not properly delimited)
    # Look for backslash commands outside of $ delimiters
    math_pattern = re.compile(r'(?<!\$)\\(?:frac|sqrt|sum|int|theta|alpha|beta|gamma|delta|epsilon|Delta|times|cdot|pm|infty)\{', re.IGNORECASE)
    for match in math_pattern.finditer(content):
        # Check if this is inside a $ delimiter
        start_pos = match.start()
        before = content[:start_pos]

        # Count dollars before this position
        dollars_before = before.count('$') - before.count('\\$')

        # If even number of dollars, we're outside math mode
        if dollars_before % 2 == 0:
            line_num = before.count('\n') + 1
            issues.append({
                'line': line_num,
                'severity': 'high',
                'category': 'latex',
                'description': f'LaTeX command outside math delimiters: {match.group(0)}'
            })

    return issues

def check_content_quality(content, filepath):
    """Check content quality."""
    issues = []

    # Check for learning objectives
    if 'learning objective' not in content.lower():
        issues.append({
            'line': None,
            'severity': 'high',
            'category': 'content',
            'description': 'Missing learning objectives section'
        })

    # Check for examples
    if 'example' not in content.lower():
        issues.append({
            'line': None,
            'severity': 'medium',
            'category': 'content',
            'description': 'No examples found in lesson'
        })

    # Check for IB-specific content markers
    ib_markers = ['ib', 'syllabus', 'assessment']
    has_ib_content = any(marker in content.lower() for marker in ib_markers)

    return issues

def verify_lesson(filepath):
    """Verify a single lesson file."""
    print(f"Verifying: {filepath.name}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    all_issues = []

    # HTML validation
    validator = LessonValidator()
    try:
        validator.feed(content)
        validator.check_unclosed_tags()
        validator.check_heading_hierarchy()
        all_issues.extend(validator.issues)
    except Exception as e:
        all_issues.append({
            'line': None,
            'severity': 'critical',
            'category': 'html',
            'description': f'HTML parsing error: {str(e)}'
        })

    # LaTeX validation
    latex_issues = check_latex(content, filepath)
    all_issues.extend(latex_issues)

    # Content quality
    content_issues = check_content_quality(content, filepath)
    all_issues.extend(content_issues)

    # Check interactive elements
    if not validator.has_completion_checkbox:
        all_issues.append({
            'line': None,
            'severity': 'high',
            'category': 'interactive',
            'description': 'Missing completion checkbox'
        })

    if not validator.has_flashcards_button:
        all_issues.append({
            'line': None,
            'severity': 'medium',
            'category': 'interactive',
            'description': 'Missing Flashcards button'
        })

    if not validator.has_practice_button:
        all_issues.append({
            'line': None,
            'severity': 'medium',
            'category': 'interactive',
            'description': 'Missing Practice button'
        })

    if not validator.has_ai_button:
        all_issues.append({
            'line': None,
            'severity': 'medium',
            'category': 'interactive',
            'description': 'Missing AI/Tutor button'
        })

    # Check internal links
    for link in validator.links:
        href = link['href']
        if href.startswith('/') or href.startswith('../'):
            # Internal link - check if it exists
            if href.startswith('/'):
                link_path = Path('/Users/a3015110/Desktop/IB45PLS') / href.lstrip('/')
            else:
                link_path = filepath.parent / href

            if not link_path.exists():
                all_issues.append({
                    'line': link['line'],
                    'severity': 'high',
                    'category': 'links',
                    'description': f'Broken internal link: {href}'
                })

    return {
        'lesson': filepath.name,
        'path': str(filepath),
        'issues': all_issues,
        'stats': {
            'has_learning_objectives': validator.has_learning_objectives,
            'has_examples': validator.has_examples,
            'has_completion_checkbox': validator.has_completion_checkbox,
            'has_flashcards_button': validator.has_flashcards_button,
            'has_practice_button': validator.has_practice_button,
            'has_ai_button': validator.has_ai_button,
            'image_count': len(validator.images),
            'link_count': len(validator.links)
        }
    }

def main():
    lessons_dir = Path('/Users/a3015110/Desktop/IB45PLS/subjects/economics')
    lesson_files = sorted(lessons_dir.glob('lesson_*.html'))

    print(f"Found {len(lesson_files)} economics lessons to verify\n")

    all_results = []
    total_issues = 0

    for lesson_file in lesson_files:
        result = verify_lesson(lesson_file)
        all_results.append(result)
        total_issues += len(result['issues'])

        if result['issues']:
            print(f"  ⚠️  {len(result['issues'])} issue(s) found")
        else:
            print(f"  ✓ No issues")

    # Generate summary
    print(f"\n{'='*60}")
    print(f"VERIFICATION COMPLETE")
    print(f"{'='*60}")
    print(f"Total lessons checked: {len(lesson_files)}")
    print(f"Total issues found: {total_issues}")

    # Group by severity
    severity_counts = defaultdict(int)
    category_counts = defaultdict(int)

    for result in all_results:
        for issue in result['issues']:
            severity_counts[issue['severity']] += 1
            category_counts[issue['category']] += 1

    print(f"\nBy Severity:")
    for severity in ['critical', 'high', 'medium', 'low']:
        if severity in severity_counts:
            print(f"  {severity}: {severity_counts[severity]}")

    print(f"\nBy Category:")
    for category, count in sorted(category_counts.items()):
        print(f"  {category}: {count}")

    # Save detailed results
    output_file = Path('/Users/a3015110/Desktop/IB45PLS/verification_results.json')
    with open(output_file, 'w') as f:
        json.dump(all_results, f, indent=2)

    print(f"\nDetailed results saved to: {output_file}")

    return all_results

if __name__ == '__main__':
    main()
