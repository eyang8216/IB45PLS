# Enhanced User Profile Data Structure
# Stores detailed progress tracking beyond simple "viewed" status

import json
import os
from datetime import datetime

class UserProfile:
    """Enhanced user profile with detailed progress tracking"""

    def __init__(self, username):
        self.username = username
        self.data_file = f"data/{username}.json"
        self.data = self._load_data()

    def _load_data(self):
        """Load user data from JSON file"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return self._create_default_data()

    def _create_default_data(self):
        """Create default user profile structure"""
        return {
            "username": self.username,
            "created_at": datetime.now().isoformat(),
            "study_streak": 0,
            "last_active": None,
            "total_study_time": 0,  # minutes
            "subjects": {},
            "flashcards": {},
            "practice_history": [],
            "exam_attempts": [],
            "goals": [],
            "preferences": {
                "difficulty": "medium",
                "notifications": True
            }
        }

    def save(self):
        """Save user data to JSON file"""
        os.makedirs("data", exist_ok=True)
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def mark_lesson_viewed(self, subject, lesson_id):
        """Mark a lesson as viewed"""
        if subject not in self.data["subjects"]:
            self.data["subjects"][subject] = {
                "lessons": {},
                "mastery": {},
                "time_spent": 0
            }

        if lesson_id not in self.data["subjects"][subject]["lessons"]:
            self.data["subjects"][subject]["lessons"][lesson_id] = {
                "first_viewed": datetime.now().isoformat(),
                "view_count": 0,
                "mastery_level": "not_started"
            }

        self.data["subjects"][subject]["lessons"][lesson_id]["view_count"] += 1
        self.data["subjects"][subject]["lessons"][lesson_id]["last_viewed"] = datetime.now().isoformat()

        # Update mastery based on engagement
        if self.data["subjects"][subject]["lessons"][lesson_id]["view_count"] >= 1:
            self.data["subjects"][subject]["lessons"][lesson_id]["mastery_level"] = "learning"

        self.save()

    def update_mastery(self, subject, lesson_id, level):
        """Update mastery level for a lesson
        Levels: not_started, learning, proficient, mastery
        """
        if subject in self.data["subjects"] and lesson_id in self.data["subjects"][subject]["lessons"]:
            self.data["subjects"][subject]["lessons"][lesson_id]["mastery_level"] = level
            self.save()

    def record_practice(self, subject, lesson_id, score, total, time_spent):
        """Record practice problem attempt"""
        practice_record = {
            "subject": subject,
            "lesson_id": lesson_id,
            "score": score,
            "total": total,
            "percentage": round((score / total) * 100, 1),
            "time_spent": time_spent,
            "timestamp": datetime.now().isoformat()
        }

        self.data["practice_history"].append(practice_record)

        # Update mastery based on performance
        if practice_record["percentage"] >= 90:
            self.update_mastery(subject, lesson_id, "mastery")
        elif practice_record["percentage"] >= 75:
            self.update_mastery(subject, lesson_id, "proficient")

        self.save()

    def record_exam_attempt(self, exam_type, score, total, paper_number=None):
        """Record full exam attempt"""
        exam_record = {
            "type": exam_type,
            "paper": paper_number,
            "score": score,
            "total": total,
            "percentage": round((score / total) * 100, 1),
            "timestamp": datetime.now().isoformat()
        }

        self.data["exam_attempts"].append(exam_record)
        self.save()

    def get_subject_progress(self, subject, total_lessons):
        """Get detailed progress for a subject"""
        if subject not in self.data["subjects"]:
            return {
                "viewed": 0,
                "total": total_lessons,
                "mastery_breakdown": {
                    "not_started": total_lessons,
                    "learning": 0,
                    "proficient": 0,
                    "mastery": 0
                },
                "time_spent": 0
            }

        subject_data = self.data["subjects"][subject]
        lessons = subject_data["lessons"]

        mastery_breakdown = {
            "not_started": total_lessons - len(lessons),
            "learning": 0,
            "proficient": 0,
            "mastery": 0
        }

        for lesson_data in lessons.values():
            level = lesson_data.get("mastery_level", "not_started")
            mastery_breakdown[level] = mastery_breakdown.get(level, 0) + 1

        return {
            "viewed": len(lessons),
            "total": total_lessons,
            "mastery_breakdown": mastery_breakdown,
            "time_spent": subject_data.get("time_spent", 0)
        }

    def get_recommended_lessons(self, subject):
        """Get smart recommendations for next lessons"""
        # Simple recommendation: lessons viewed but with low mastery
        recommendations = []

        if subject in self.data["subjects"]:
            lessons = self.data["subjects"][subject]["lessons"]
            for lesson_id, lesson_data in lessons.items():
                if lesson_data["mastery_level"] in ["not_started", "learning"]:
                    recommendations.append({
                        "lesson_id": lesson_id,
                        "reason": "Continue learning",
                        "mastery": lesson_data["mastery_level"]
                    })

        return recommendations[:5]  # Top 5 recommendations

    def update_streak(self):
        """Update study streak based on activity"""
        today = datetime.now().date()
        last_active = self.data.get("last_active")

        if last_active:
            last_date = datetime.fromisoformat(last_active).date()
            days_diff = (today - last_date).days

            if days_diff == 0:
                # Same day, streak continues
                pass
            elif days_diff == 1:
                # Consecutive day, increment streak
                self.data["study_streak"] += 1
            else:
                # Streak broken
                self.data["study_streak"] = 1
        else:
            # First activity
            self.data["study_streak"] = 1

        self.data["last_active"] = datetime.now().isoformat()
        self.save()

    def add_flashcard(self, subject, lesson_id, front, back):
        """Add a flashcard for spaced repetition"""
        if subject not in self.data["flashcards"]:
            self.data["flashcards"][subject] = []

        flashcard = {
            "lesson_id": lesson_id,
            "front": front,
            "back": back,
            "created": datetime.now().isoformat(),
            "next_review": datetime.now().isoformat(),
            "interval": 1,  # days
            "ease_factor": 2.5,
            "repetitions": 0
        }

        self.data["flashcards"][subject].append(flashcard)
        self.save()

    def get_due_flashcards(self, subject):
        """Get flashcards due for review (spaced repetition)"""
        if subject not in self.data["flashcards"]:
            return []

        now = datetime.now()
        due_cards = []

        for card in self.data["flashcards"][subject]:
            next_review = datetime.fromisoformat(card["next_review"])
            if next_review <= now:
                due_cards.append(card)

        return due_cards
