# Enhanced Flask Routes for New Features
# Add these routes to app.py

from user_profile import UserProfile
from practice_generator import PracticeGenerator, SpacedRepetition

# Initialize practice generator (add after FREE_MODELS definition)
practice_gen = None  # Will be initialized with API caller

def get_practice_generator():
    """Lazy init practice generator"""
    global practice_gen
    if practice_gen is None:
        def api_caller(messages):
            """Wrapper for API calls"""
            for model in FREE_MODELS:
                try:
                    response = call_openrouter(messages, model)
                    if response:
                        return response
                except:
                    continue
            return "Unable to generate content."

        practice_gen = PracticeGenerator(api_caller)
    return practice_gen


# Enhanced dashboard route
@app.route("/dashboard")
@login_required
def dashboard_enhanced():
    """Enhanced dashboard with mastery tracking"""
    username = session.get("user", "")
    profile = UserProfile(username)

    # Update streak
    profile.update_streak()

    # Get progress for all subjects
    subjects_progress = {}
    for subject_key, subject_info in SUBJECTS.items():
        total = subject_info.get("total_lessons", 0)
        progress = profile.get_subject_progress(subject_key, total)
        subjects_progress[subject_key] = {
            **progress,
            "name": subject_info["name"],
            "icon": subject_info["icon"],
            "color": subject_info["color"]
        }

    # Get recent practice attempts
    recent_practice = profile.data.get("practice_history", [])[-5:]

    # Get exam attempts
    exam_attempts = profile.data.get("exam_attempts", [])[-5:]

    # Get recommendations
    recommendations = {}
    for subject_key in SUBJECTS.keys():
        recs = profile.get_recommended_lessons(subject_key)
        if recs:
            recommendations[subject_key] = recs[:3]

    return render_template("dashboard_enhanced.html",
        username=username,
        streak=profile.data.get("study_streak", 0),
        total_time=profile.data.get("total_study_time", 0),
        subjects=subjects_progress,
        recent_practice=recent_practice,
        exam_attempts=exam_attempts,
        recommendations=recommendations,
        csrf_token=generate_csrf_token()
    )


# Mark lesson as viewed (enhanced)
@app.route("/mark_viewed", methods=["POST"])
@login_required
def mark_viewed_enhanced():
    """Mark lesson as viewed with enhanced tracking"""
    username = session.get("user", "")
    data = request.get_json()

    subject = data.get("subject", "")
    lesson = data.get("lesson", "")

    if not subject or not lesson:
        return jsonify({"error": "Missing subject or lesson"}), 400

    profile = UserProfile(username)
    profile.mark_lesson_viewed(subject, lesson)

    return jsonify({"success": True})


# Generate practice problems
@app.route("/generate_practice", methods=["POST"])
@login_required
def generate_practice():
    """Generate AI practice problems for a lesson"""
    if check_user_rate_limit(session.get("user", "")):
        return jsonify({"error": "Rate limit exceeded. Try again in an hour."}), 429

    record_user_request(session.get("user", ""))

    data = request.get_json()
    context = data.get("context", {})

    subject = context.get("subject", "")
    lesson = context.get("lesson", "")
    syllabus = context.get("syllabus", "")
    level = context.get("level", "HL")

    gen = get_practice_generator()
    problems = gen.generate_problems(subject, lesson, syllabus, level, count=5)

    # Format as HTML
    html = '<div class="practice-problems">'
    for i, problem in enumerate(problems, 1):
        html += f'<div class="problem" data-problem-id="{i}">'
        html += f'<div class="problem-header">'
        html += f'<span class="problem-number">Problem {i}</span>'
        html += f'<span class="problem-difficulty {problem.get("difficulty", "medium")}">{problem.get("difficulty", "medium").title()}</span>'
        html += f'<span class="problem-marks">[{problem.get("marks", 0)} marks]</span>'
        html += f'</div>'
        html += f'<div class="problem-question">{problem.get("question", "")}</div>'

        if problem.get("type") == "mcq" and problem.get("options"):
            html += '<div class="problem-options">'
            for opt in problem["options"]:
                html += f'<label><input type="radio" name="problem_{i}" value="{opt[0]}"> {opt}</label>'
            html += '</div>'
        else:
            html += f'<textarea class="problem-answer" placeholder="Type your answer here..." rows="4"></textarea>'

        html += f'<button class="show-answer-btn" data-answer="{problem.get("correct_answer", "")}" data-explanation="{problem.get("explanation", "")}">Show Answer</button>'
        html += f'<div class="problem-solution" style="display: none;"></div>'
        html += '</div>'

    html += '</div>'
    html += '''
    <script>
    document.querySelectorAll('.show-answer-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const solution = this.nextElementSibling;
            if (solution.style.display === 'none') {
                solution.innerHTML = `
                    <div class="answer"><strong>Answer:</strong> ${this.dataset.answer}</div>
                    <div class="explanation"><strong>Explanation:</strong> ${this.dataset.explanation}</div>
                `;
                solution.style.display = 'block';
                this.textContent = 'Hide Answer';
            } else {
                solution.style.display = 'none';
                this.textContent = 'Show Answer';
            }
        });
    });
    </script>
    '''

    return jsonify({"html": html})


# Submit practice answers
@app.route("/submit_practice", methods=["POST"])
@login_required
def submit_practice():
    """Submit and grade practice answers"""
    if check_user_rate_limit(session.get("user", "")):
        return jsonify({"error": "Rate limit exceeded"}), 429

    record_user_request(session.get("user", ""))

    username = session.get("user", "")
    data = request.get_json()

    subject = data.get("subject", "")
    lesson_id = data.get("lesson_id", "")
    answers = data.get("answers", [])
    time_spent = data.get("time_spent", 0)

    gen = get_practice_generator()

    # Grade each answer
    results = []
    total_score = 0
    max_score = 0

    for answer in answers:
        question = answer.get("question", "")
        student_answer = answer.get("student_answer", "")
        correct_answer = answer.get("correct_answer", "")
        marks = answer.get("marks", 0)

        feedback = gen.check_answer(question, student_answer, correct_answer, subject)

        # Scale score to marks
        earned = round((feedback.get("score", 0) / 100) * marks, 1)
        total_score += earned
        max_score += marks

        results.append({
            "question": question,
            "earned": earned,
            "max": marks,
            "feedback": feedback
        })

    # Record practice attempt
    profile = UserProfile(username)
    profile.record_practice(subject, lesson_id, total_score, max_score, time_spent)

    return jsonify({
        "total_score": total_score,
        "max_score": max_score,
        "percentage": round((total_score / max_score) * 100, 1) if max_score > 0 else 0,
        "results": results
    })


# Generate flashcards
@app.route("/generate_flashcards", methods=["POST"])
@login_required
def generate_flashcards():
    """Generate flashcards for a lesson"""
    if check_user_rate_limit(session.get("user", "")):
        return jsonify({"error": "Rate limit exceeded"}), 429

    record_user_request(session.get("user", ""))

    data = request.get_json()
    subject = data.get("subject", "")
    lesson = data.get("lesson", "")
    content = data.get("content_summary", "")

    gen = get_practice_generator()
    flashcards = gen.generate_flashcards(subject, lesson, content)

    # Save to user profile
    username = session.get("user", "")
    profile = UserProfile(username)

    for card in flashcards:
        profile.add_flashcard(subject, lesson, card["front"], card["back"])

    return jsonify({
        "success": True,
        "count": len(flashcards),
        "flashcards": flashcards
    })


# Flashcard review
@app.route("/flashcards/<subject>")
@login_required
def flashcard_review(subject):
    """Flashcard review interface"""
    username = session.get("user", "")
    profile = UserProfile(username)

    due_cards = profile.get_due_flashcards(subject)

    return render_template("flashcards.html",
        subject=subject,
        cards=due_cards,
        total_due=len(due_cards),
        csrf_token=generate_csrf_token()
    )


# Update flashcard (after review)
@app.route("/review_flashcard", methods=["POST"])
@login_required
def review_flashcard():
    """Update flashcard after review"""
    username = session.get("user", "")
    data = request.get_json()

    subject = data.get("subject", "")
    card_index = data.get("card_index", 0)
    quality = data.get("quality", 0)  # 0-5

    profile = UserProfile(username)

    if subject in profile.data["flashcards"] and card_index < len(profile.data["flashcards"][subject]):
        card = profile.data["flashcards"][subject][card_index]

        # Calculate next interval using SM-2
        new_interval, new_reps, new_ease = SpacedRepetition.calculate_next_interval(
            quality,
            card.get("repetitions", 0),
            card.get("ease_factor", 2.5),
            card.get("interval", 1)
        )

        # Update card
        from datetime import datetime, timedelta
        card["interval"] = new_interval
        card["repetitions"] = new_reps
        card["ease_factor"] = new_ease
        card["next_review"] = (datetime.now() + timedelta(days=new_interval)).isoformat()
        card["last_reviewed"] = datetime.now().isoformat()

        profile.save()

        return jsonify({"success": True, "next_review_days": new_interval})

    return jsonify({"error": "Card not found"}), 404


# Exam mode
@app.route("/exam/<subject>/paper/<int:paper_num>")
@login_required
def exam_mode(subject, paper_num):
    """Full exam mode"""
    if subject not in SUBJECTS:
        abort(404)

    return render_template("exam_mode.html",
        subject=subject,
        subject_name=SUBJECTS[subject]["name"],
        paper_num=paper_num,
        csrf_token=generate_csrf_token()
    )


# Generate exam paper
@app.route("/generate_exam", methods=["POST"])
@login_required
def generate_exam():
    """Generate full exam paper"""
    if check_user_rate_limit(session.get("user", "")):
        return jsonify({"error": "Rate limit exceeded"}), 429

    record_user_request(session.get("user", ""))

    data = request.get_json()
    subject = data.get("subject", "")
    paper_type = data.get("paper", 1)
    topics = data.get("topics", [])
    level = data.get("level", "HL")

    gen = get_practice_generator()
    exam = gen.generate_exam_paper(subject, paper_type, topics, level)

    return jsonify(exam)


# Submit exam
@app.route("/submit_exam", methods=["POST"])
@login_required
def submit_exam():
    """Submit and grade exam"""
    username = session.get("user", "")
    data = request.get_json()

    exam_type = data.get("exam_type", "")
    paper_num = data.get("paper", 1)
    score = data.get("score", 0)
    total = data.get("total", 0)

    profile = UserProfile(username)
    profile.record_exam_attempt(exam_type, score, total, paper_num)

    return jsonify({"success": True})
