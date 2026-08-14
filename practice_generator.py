# Practice Problem Generator
# AI-powered practice problem generation for each lesson

import json
from typing import List, Dict

class PracticeGenerator:
    """Generate practice problems for lessons using AI"""

    def __init__(self, api_caller):
        """Initialize with API caller function"""
        self.api_caller = api_caller

    def generate_problems(self, subject: str, lesson_title: str, syllabus_code: str = "", level: str = "HL", count: int = 5) -> List[Dict]:
        """Generate practice problems for a specific lesson"""

        prompt = f"""Generate {count} practice problems for an IB {subject} {level} lesson on "{lesson_title}".

Syllabus code: {syllabus_code if syllabus_code else 'Not specified'}

Requirements:
1. Problems should match IB exam style (Paper 1 MCQ and Paper 2 structured questions)
2. Include a mix of difficulty levels: 2 easy, 2 medium, 1 challenging
3. For each problem provide:
   - Question text (use LaTeX $...$ for inline math, $$...$$ for display math)
   - Answer/solution with explanation
   - Marks allocation (e.g., [2 marks])
   - IB command term used (e.g., "Calculate", "Explain", "Outline")

Format as JSON array:
[
  {{
    "type": "mcq" or "structured",
    "difficulty": "easy" | "medium" | "hard",
    "question": "Question text here",
    "marks": 2,
    "command_term": "Calculate",
    "options": ["A. ...", "B. ...", "C. ...", "D. ..."],  // only for MCQ
    "correct_answer": "B" or "Full answer text",
    "explanation": "Why this is correct and common mistakes"
  }}
]

Return ONLY valid JSON, no other text."""

        try:
            messages = [{"role": "user", "content": prompt}]
            response = self.api_caller(messages)

            # Parse JSON from response
            response_text = response.strip()

            # Try to extract JSON if wrapped in markdown
            if "```json" in response_text:
                start = response_text.find("```json") + 7
                end = response_text.find("```", start)
                response_text = response_text[start:end].strip()
            elif "```" in response_text:
                start = response_text.find("```") + 3
                end = response_text.find("```", start)
                response_text = response_text[start:end].strip()

            problems = json.loads(response_text)

            # Validate structure
            if not isinstance(problems, list):
                return self._fallback_problems(subject, lesson_title)

            return problems

        except Exception as e:
            print(f"Error generating problems: {e}")
            return self._fallback_problems(subject, lesson_title)

    def _fallback_problems(self, subject: str, lesson_title: str) -> List[Dict]:
        """Fallback problems if generation fails"""
        return [
            {
                "type": "structured",
                "difficulty": "medium",
                "question": f"Explain the key concepts covered in the lesson on {lesson_title}.",
                "marks": 4,
                "command_term": "Explain",
                "correct_answer": "Refer to lesson content for key concepts and their relationships.",
                "explanation": "This is a general comprehension question. Review the lesson material."
            }
        ]

    def generate_flashcards(self, subject: str, lesson_title: str, content_summary: str = "") -> List[Dict]:
        """Generate flashcards for spaced repetition"""

        prompt = f"""Generate 10 flashcards for an IB {subject} lesson on "{lesson_title}".

{f'Lesson summary: {content_summary}' if content_summary else ''}

Requirements:
1. Focus on key terms, definitions, formulas, and concepts
2. Front should be a question or term
3. Back should be a clear, concise answer
4. Use LaTeX for math: $...$ inline, $$...$$ display

Format as JSON:
[
  {{
    "front": "What is the definition of X?",
    "back": "X is defined as..."
  }}
]

Return ONLY valid JSON."""

        try:
            messages = [{"role": "user", "content": prompt}]
            response = self.api_caller(messages)

            response_text = response.strip()

            # Extract JSON
            if "```json" in response_text:
                start = response_text.find("```json") + 7
                end = response_text.find("```", start)
                response_text = response_text[start:end].strip()
            elif "```" in response_text:
                start = response_text.find("```") + 3
                end = response_text.find("```", start)
                response_text = response_text[start:end].strip()

            flashcards = json.loads(response_text)

            if not isinstance(flashcards, list):
                return []

            return flashcards

        except Exception as e:
            print(f"Error generating flashcards: {e}")
            return []

    def check_answer(self, question: str, student_answer: str, correct_answer: str, subject: str) -> Dict:
        """Grade a student's answer using AI"""

        prompt = f"""You are an IB {subject} examiner. Grade this student answer.

Question: {question}

Model Answer: {correct_answer}

Student Answer: {student_answer}

Provide:
1. Score (0-100)
2. Specific feedback on what was correct
3. What was missing or incorrect
4. How to improve

Format as JSON:
{{
  "score": 85,
  "feedback": "...",
  "strengths": ["..."],
  "improvements": ["..."]
}}

Return ONLY valid JSON."""

        try:
            messages = [{"role": "user", "content": prompt}]
            response = self.api_caller(messages)

            response_text = response.strip()

            # Extract JSON
            if "```json" in response_text:
                start = response_text.find("```json") + 7
                end = response_text.find("```", start)
                response_text = response_text[start:end].strip()
            elif "```" in response_text:
                start = response_text.find("```") + 3
                end = response_text.find("```", start)
                response_text = response_text[start:end].strip()

            feedback = json.loads(response_text)
            return feedback

        except Exception as e:
            print(f"Error checking answer: {e}")
            return {
                "score": 0,
                "feedback": "Unable to grade answer automatically.",
                "strengths": [],
                "improvements": ["Please review the model answer."]
            }

    def generate_exam_paper(self, subject: str, paper_type: int, topics: List[str], level: str = "HL") -> Dict:
        """Generate a full exam paper"""

        prompt = f"""Generate an IB {subject} {level} Paper {paper_type} exam.

Topics to cover: {', '.join(topics)}

Paper {paper_type} format:
- Paper 1: Multiple choice (40 questions, 1 mark each)
- Paper 2: Structured questions (mix of 2-4-6 mark questions, total 90 minutes)
- Paper 3: HL only, extended response (mix of short and long questions)

Generate appropriate questions for Paper {paper_type}.

Format as JSON:
{{
  "title": "Paper {paper_type} - {subject} {level}",
  "duration_minutes": 90,
  "total_marks": 75,
  "sections": [
    {{
      "name": "Section A",
      "questions": [...]
    }}
  ]
}}

Return ONLY valid JSON."""

        try:
            messages = [{"role": "user", "content": prompt}]
            response = self.api_caller(messages)

            response_text = response.strip()

            # Extract JSON
            if "```json" in response_text:
                start = response_text.find("```json") + 7
                end = response_text.find("```", start)
                response_text = response_text[start:end].strip()
            elif "```" in response_text:
                start = response_text.find("```") + 3
                end = response_text.find("```", start)
                response_text = response_text[start:end].strip()

            exam = json.loads(response_text)
            return exam

        except Exception as e:
            print(f"Error generating exam: {e}")
            return {
                "title": f"Paper {paper_type} - {subject} {level}",
                "duration_minutes": 90,
                "total_marks": 75,
                "sections": [],
                "error": "Failed to generate exam"
            }


class SpacedRepetition:
    """SM-2 algorithm for flashcard spacing"""

    @staticmethod
    def calculate_next_interval(quality: int, repetitions: int, ease_factor: float, interval: int) -> tuple:
        """
        Calculate next review interval using SM-2 algorithm

        Args:
            quality: Response quality (0-5, where 3+ is passing)
            repetitions: Number of successful repetitions
            ease_factor: Ease factor (>= 1.3)
            interval: Current interval in days

        Returns:
            (new_interval, new_repetitions, new_ease_factor)
        """

        if quality < 3:
            # Failed recall - reset
            return (1, 0, ease_factor)

        # Update ease factor
        new_ease = ease_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
        new_ease = max(1.3, new_ease)  # Minimum ease factor

        # Calculate new interval
        if repetitions == 0:
            new_interval = 1
        elif repetitions == 1:
            new_interval = 6
        else:
            new_interval = round(interval * new_ease)

        return (new_interval, repetitions + 1, new_ease)
