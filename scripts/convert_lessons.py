#!/usr/bin/env python3
"""
Lesson Template Converter
Converts existing HTML lessons to use the new unified lesson_base.html template
"""

import os
import re
import json
from pathlib import Path
from bs4 import BeautifulSoup

class LessonConverter:
    """Convert old lesson HTML to new template format"""

    def __init__(self, subjects_dir="subjects"):
        self.subjects_dir = subjects_dir
        self.converted_count = 0
        self.error_count = 0
        self.errors = []

    def extract_lesson_metadata(self, html_content, filepath):
        """Extract metadata from existing lesson HTML"""
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract title
        title_tag = soup.find('h1')
        if not title_tag:
            title_tag = soup.find('title')

        title = title_tag.get_text().strip() if title_tag else Path(filepath).stem

        # Try to extract level from title or content
        level = "HL"  # Default
        if "SL" in title.upper():
            level = "SL"
        elif "HL" in title.upper():
            level = "HL"
        elif "AHL" in title.upper():
            level = "AHL"

        # Extract learning objectives if present
        objectives = []
        objectives_section = soup.find(string=re.compile(r'What You\'ll Learn|Learning Objectives|Objectives', re.I))
        if objectives_section:
            parent = objectives_section.find_parent()
            if parent:
                ul = parent.find_next('ul')
                if ul:
                    objectives = [li.get_text().strip() for li in ul.find_all('li')]

        return {
            'title': title,
            'level': level,
            'objectives': objectives,
            'syllabus_code': self._extract_syllabus_code(title)
        }

    def _extract_syllabus_code(self, title):
        """Try to extract syllabus code from title (e.g., A1.1, B2.3)"""
        match = re.search(r'\b([A-E]\d+\.?\d*)\b', title)
        return match.group(1) if match else ""

    def extract_lesson_content(self, html_content):
        """Extract main content from existing HTML"""
        soup = BeautifulSoup(html_content, 'html.parser')

        # Remove script tags, nav, style (we'll use new styles)
        for tag in soup.find_all(['script', 'nav', 'style']):
            if 'MathJax' not in str(tag):  # Keep MathJax config
                tag.decompose()

        # Get body content or main content area
        body = soup.find('body')
        if not body:
            return str(soup)

        # Remove any existing nav bars
        for nav_class in ['lessons-nav', 'nav', 'top-nav']:
            for nav in body.find_all(class_=nav_class):
                nav.decompose()

        # Remove chatbot if exists
        for chatbot in body.find_all(id='lessons-chatbot'):
            chatbot.decompose()

        # Get the main content
        content = str(body)

        # Clean up - remove body tags
        content = re.sub(r'<body[^>]*>', '', content)
        content = re.sub(r'</body>', '', content)

        return content.strip()

    def convert_to_template(self, html_content, subject_key, lesson_id, filepath):
        """Convert lesson to new template format"""

        # Check if already converted
        if 'lesson-actions' in html_content:
            return html_content  # Already converted, skip

        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract metadata
        metadata = self.extract_lesson_metadata(html_content, filepath)

        # Add completion checkbox after first h2 (since no h1 exists)
        first_h2 = soup.find('h2')
        if first_h2:
            checkbox_html = '''
<div class="lesson-completion" style="margin: 1rem 0; padding: 1rem; background: #f0f9ff; border-radius: 8px;">
    <label class="completion-checkbox" style="display: flex; align-items: center; gap: 0.75rem; cursor: pointer;">
        <input type="checkbox" id="lesson-complete" style="width: 24px; height: 24px; cursor: pointer; accent-color: #10b981;">
        <span style="font-size: 1rem; color: #0f172a; font-weight: 500;">✓ Mark this lesson as complete</span>
    </label>
</div>
'''
            checkbox_soup = BeautifulSoup(checkbox_html, 'html.parser')
            first_h2.insert_before(checkbox_soup)

        # Add interactive buttons before closing body
        body = soup.find('body')
        if body:
            buttons_html = '''
<div class="lesson-actions" style="margin: 2rem 0; padding: 1.5rem; background: #f8fafc; border-radius: 8px; display: flex; gap: 1rem; flex-wrap: wrap;">
    <button id="generate-flashcards-btn" class="action-btn" style="padding: 0.75rem 1.5rem; background: #3b82f6; color: white; border: none; border-radius: 6px; font-weight: 600; cursor: pointer; transition: all 0.2s;">
        🗂️ Generate Flashcards
    </button>
    <button id="practice-problems-btn" class="action-btn" style="padding: 0.75rem 1.5rem; background: #10b981; color: white; border: none; border-radius: 6px; font-weight: 600; cursor: pointer; transition: all 0.2s;">
        ✏️ Practice Problems
    </button>
    <button id="ask-ai-btn" class="action-btn" style="padding: 0.75rem 1.5rem; background: #8b5cf6; color: white; border: none; border-radius: 6px; font-weight: 600; cursor: pointer; transition: all 0.2s;">
        💬 Ask AI
    </button>
</div>

<script>
(function() {
    const subjectKey = "''' + subject_key + '''";
    const lessonId = "''' + lesson_id + '''";
    const lessonTitle = "''' + metadata['title'].replace('"', '\\"') + '''";

    function getCsrf() {
        var m = document.querySelector('meta[name="csrf-token"]');
        return m ? m.getAttribute('content') : '';
    }

    // Completion checkbox
    const checkbox = document.getElementById('lesson-complete');
    if (checkbox) {
        // Load saved state
        const saved = localStorage.getItem(`completed_${subjectKey}_${lessonId}`);
        if (saved === 'true') checkbox.checked = true;

        checkbox.addEventListener('change', async function() {
            const completed = this.checked;
            localStorage.setItem(`completed_${subjectKey}_${lessonId}`, completed);

            try {
                await fetch('/toggle_completion', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRF-Token': getCsrf()
                    },
                    body: JSON.stringify({
                        subject: subjectKey,
                        lesson: lessonId,
                        completed: completed
                    })
                });
            } catch(e) {
                console.error('Error saving completion:', e);
            }
        });
    }

    // Generate Flashcards
    const flashcardsBtn = document.getElementById('generate-flashcards-btn');
    if (flashcardsBtn) {
        flashcardsBtn.addEventListener('click', async function() {
            this.disabled = true;
            this.textContent = '⏳ Generating...';

            try {
                const content = document.body.innerText.substring(0, 2000);
                const response = await fetch('/generate_flashcards', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRF-Token': getCsrf()
                    },
                    body: JSON.stringify({
                        subject: subjectKey,
                        lesson: lessonTitle,
                        content_summary: content
                    })
                });

                const data = await response.json();
                if (data.error) {
                    alert('Error: ' + data.error);
                } else {
                    alert(`✅ Created ${data.count} flashcards! View them at /flashcards/${subjectKey}`);
                }
            } catch(e) {
                alert('Error generating flashcards: ' + e.message);
            } finally {
                this.disabled = false;
                this.textContent = '🗂️ Generate Flashcards';
            }
        });
    }

    // Practice Problems - open in new section
    const practiceBtn = document.getElementById('practice-problems-btn');
    if (practiceBtn) {
        practiceBtn.addEventListener('click', function() {
            alert('Practice problems feature coming soon! Use the AI chatbot to generate custom questions.');
        });
    }

    // Ask AI - scroll to chatbot
    const aiBtn = document.getElementById('ask-ai-btn');
    if (aiBtn) {
        aiBtn.addEventListener('click', function() {
            const chatbot = document.getElementById('lessons-chatbot');
            if (chatbot) {
                chatbot.scrollIntoView({ behavior: 'smooth' });
                const toggleBtn = chatbot.querySelector('.chatbot-toggle');
                if (toggleBtn) toggleBtn.click();
            } else {
                alert('AI chatbot not available on this page. It will be added soon!');
            }
        });
    }

    // Track lesson view
    fetch('/mark_viewed', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRF-Token': getCsrf()
        },
        body: JSON.stringify({
            subject: subjectKey,
            lesson: lessonId
        })
    }).catch(e => console.error('Error tracking view:', e));

})();
</script>
'''
            buttons_soup = BeautifulSoup(buttons_html, 'html.parser')

            # Find nav and insert before it, or insert at end
            nav = body.find(class_='nav')
            if nav:
                nav.insert_before(buttons_soup)
            else:
                body.append(buttons_soup)

        return str(soup)

    def convert_lesson_file(self, filepath, subject_key):
        """Convert a single lesson file"""
        try:
            # Read original file
            with open(filepath, 'r', encoding='utf-8') as f:
                original_html = f.read()

            # Extract lesson ID from filename
            lesson_id = Path(filepath).stem

            # Convert to new template
            new_html = self.convert_to_template(original_html, subject_key, lesson_id, filepath)

            # Backup original
            backup_path = str(filepath) + '.backup'
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_html)

            # Write converted version
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_html)

            self.converted_count += 1
            print(f"✅ Converted: {filepath}")
            return True

        except Exception as e:
            self.error_count += 1
            self.errors.append(f"❌ Error converting {filepath}: {str(e)}")
            print(f"❌ Error converting {filepath}: {str(e)}")
            return False

    def convert_subject(self, subject_key, dry_run=False):
        """Convert all lessons for a subject"""
        subject_dir = Path(self.subjects_dir) / subject_key

        if not subject_dir.exists():
            print(f"⚠️  Subject directory not found: {subject_dir}")
            return

        print(f"\n📚 Converting {subject_key.upper()} lessons...")

        # Find all HTML lesson files - check both root and lessons/ subdirectory
        lesson_files = []
        for pattern in ['lesson_*.html', 'lesson*.html', 'L*.html']:
            lesson_files.extend(subject_dir.glob(pattern))
            # Also check lessons subdirectory
            lessons_subdir = subject_dir / 'lessons'
            if lessons_subdir.exists():
                lesson_files.extend(lessons_subdir.glob(pattern))

        # Sort for consistent ordering
        lesson_files = sorted(set(lesson_files))

        if not lesson_files:
            print(f"⚠️  No lesson files found in {subject_dir}")
            return

        print(f"Found {len(lesson_files)} lesson files")

        if dry_run:
            print("🔍 DRY RUN - No files will be modified")
            for filepath in lesson_files[:5]:  # Show first 5
                print(f"  Would convert: {filepath.name}")
            if len(lesson_files) > 5:
                print(f"  ... and {len(lesson_files) - 5} more")
            return

        # Convert each lesson
        for filepath in lesson_files:
            self.convert_lesson_file(filepath, subject_key)

        print(f"\n✅ Converted {self.converted_count} lessons")
        if self.error_count > 0:
            print(f"❌ {self.error_count} errors")

    def convert_all_subjects(self, dry_run=False):
        """Convert lessons for all subjects"""
        subjects = ['biology', 'chemistry', 'physics', 'math', 'economics',
                   'english', 'chinese', 'sat']

        print("=" * 60)
        print("LESSON TEMPLATE CONVERTER")
        print("=" * 60)

        if dry_run:
            print("🔍 DRY RUN MODE - No files will be modified")

        for subject in subjects:
            self.convert_subject(subject, dry_run)

        print("\n" + "=" * 60)
        print("CONVERSION SUMMARY")
        print("=" * 60)
        print(f"✅ Successfully converted: {self.converted_count} lessons")
        print(f"❌ Errors: {self.error_count}")

        if self.errors:
            print("\nErrors encountered:")
            for error in self.errors:
                print(f"  {error}")

        print("\n💾 Original files backed up with .backup extension")
        print("🔄 To revert: rename .backup files back to .html")

    def generate_report(self, output_file="conversion_report.json"):
        """Generate detailed conversion report"""
        report = {
            "converted_count": self.converted_count,
            "error_count": self.error_count,
            "errors": self.errors
        }

        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)

        print(f"\n📄 Report saved to: {output_file}")


def main():
    import sys

    converter = LessonConverter()

    # Check for dry-run flag
    dry_run = '--dry-run' in sys.argv or '-n' in sys.argv

    # Check for specific subject
    if len(sys.argv) > 1 and sys.argv[1] not in ['--dry-run', '-n']:
        subject = sys.argv[1]
        converter.convert_subject(subject, dry_run)
    else:
        converter.convert_all_subjects(dry_run)

    converter.generate_report()


if __name__ == "__main__":
    main()
