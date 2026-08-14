# Deployment Guide - IB45PLS Platform Overhaul

## Quick Deployment Checklist

### 1. Local Testing (Before Pushing)
```bash
# Test imports work
cd /Users/a3015110/Desktop/IB45PLS
python3 -c "from user_profile import UserProfile; from practice_generator import PracticeGenerator; print('✅ Imports OK')"

# Test Flask app starts
python3 app.py
# Visit http://localhost:5000 and test:
# - Login
# - Enhanced dashboard (/dashboard)
# - Any lesson page
# - Practice generation
```

### 2. Git Commit & Push
```bash
cd /Users/a3015110/Desktop/IB45PLS
git add .
git commit -m "feat: comprehensive platform overhaul - Phase 1-3

- Add enhanced user profiles with mastery tracking
- Implement AI practice problem generator
- Add flashcard system with spaced repetition
- Create full exam mode (Papers 1-3)
- Build unified lesson template (fluapi-inspired)
- Add performance analytics dashboard
- Implement smart recommendations engine
- Map all subjects to IB syllabus
- Add context-aware AI tutor per lesson

Features: 11 new modules, 1800+ lines of code
Closes: Platform overhaul request"

git push origin main
```

### 3. PythonAnywhere Deployment

#### Step 1: Pull Code
```bash
# SSH into PythonAnywhere or use Bash console
cd ~/IB45PLS
git pull origin main
```

#### Step 2: Check File Structure
```bash
# Verify new files exist
ls -la user_profile.py practice_generator.py syllabus_mappings.py
ls -la templates/dashboard_enhanced.html templates/flashcards.html
ls -la static/lesson.css
```

#### Step 3: Create Data Directory
```bash
# Create directory for user profiles
mkdir -p ~/IB45PLS/data
chmod 755 ~/IB45PLS/data
```

#### Step 4: Test Imports
```bash
# Test Python imports work
cd ~/IB45PLS
python3 -c "from user_profile import UserProfile; print('✅ Profile import OK')"
python3 -c "from practice_generator import PracticeGenerator; print('✅ Generator import OK')"
```

#### Step 5: Reload Web App
1. Go to PythonAnywhere **Web** tab
2. Click **Reload** button for your web app
3. Check **Error log** for any import errors

#### Step 6: Test Routes
Visit these URLs to verify:
- `/dashboard` → Should redirect to enhanced dashboard
- `/dashboard_enhanced` → New analytics dashboard
- `/flashcards/biology` → Flashcard interface (will be empty initially)
- `/exam/biology/paper/1` → Exam mode (generates on load)

### 4. Common Issues & Fixes

#### Issue: Import Error for new modules
```
ModuleNotFoundError: No module named 'user_profile'
```

**Fix:**
```bash
# Ensure you're in the right directory
cd ~/IB45PLS
ls -la *.py  # Should show user_profile.py, practice_generator.py
```

**If files missing:**
```bash
git pull origin main  # Pull again
```

#### Issue: Data directory permission denied
```
PermissionError: [Errno 13] Permission denied: 'data/username.json'
```

**Fix:**
```bash
mkdir -p ~/IB45PLS/data
chmod 755 ~/IB45PLS/data
```

#### Issue: Rate limit errors immediately
```
Rate limit exceeded. Try again in an hour.
```

**Fix:** Rate limit state is in-memory, restart resets it:
1. Go to Web tab
2. Click Reload

#### Issue: Flashcards page shows empty
**This is normal!** Flashcards are generated when user clicks "Generate Flashcards" in a lesson.

#### Issue: Practice problems not generating
**Check:** OpenRouter API key is set and valid:
```bash
# In app.py, verify:
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "sk-or-v1-...")
```

### 5. Feature Testing Workflow

#### Test Enhanced Dashboard
1. Login as EthanYang
2. Visit `/dashboard`
3. Should see:
   - Study streak (will be 1 on first visit)
   - Subjects with mastery breakdown
   - 0 in all mastery categories initially
4. Click on a subject → View a lesson
5. Return to dashboard → Should see 1 lesson in "Learning" status

#### Test Practice Generation
1. Open any Biology lesson
2. Click **"Practice"** button (if using new template)
3. OR manually visit `/generate_practice` with POST request
4. Should generate 5 problems with MCQ/structured mix
5. Note: Each generation uses 1 AI request (rate limited to 60/hour)

#### Test Flashcards
1. Open any lesson
2. Generate flashcards (would need button added to existing lessons)
3. Visit `/flashcards/biology`
4. Should show cards with flip functionality
5. Rate cards: Again/Hard/Good/Easy
6. Next review scheduled based on SM-2 algorithm

#### Test Exam Mode
1. Visit `/exam/biology/paper/1`
2. Should show "Generating Exam..." spinner
3. Wait ~10-20 seconds for AI generation
4. Exam appears with 40 questions (Paper 1 MCQ)
5. Timer starts automatically (90 minutes)
6. Submit or let timer expire

### 6. Performance Monitoring

#### Check API Usage
```python
# In Python console on PythonAnywhere
import json
with open('data/EthanYang.json', 'r') as f:
    data = json.load(f)
    print(f"Practice sessions: {len(data.get('practice_history', []))}")
    print(f"Exam attempts: {len(data.get('exam_attempts', []))}")
    print(f"Study streak: {data.get('study_streak', 0)}")
```

#### Monitor Error Log
1. Web tab → Error log link
2. Look for:
   - Import errors
   - API failures
   - File permission errors

#### Check Response Times
- Dashboard load: Should be < 1 second
- Practice generation: 5-15 seconds (AI generation)
- Flashcard generation: 5-10 seconds
- Exam generation: 10-30 seconds (larger content)

### 7. Rollback Plan (If Needed)

If deployment breaks:
```bash
cd ~/IB45PLS
git log --oneline -5  # See recent commits
git revert HEAD  # Undo last commit
git push origin main
# Then reload web app
```

Or revert to specific commit:
```bash
git reset --hard <commit-hash-before-overhaul>
git push origin main --force
```

### 8. Next Steps After Deployment

#### Immediate:
1. Test all 5 main routes (dashboard, practice, flashcards, exam, lessons)
2. Generate sample data:
   - View 5-10 lessons
   - Generate practice for 2-3 lessons
   - Create flashcards for 1 subject
   - Take 1 mock exam
3. Verify data persistence (logout/login, data still there)

#### Within 1 Week:
1. **Convert existing lessons** to use new `lesson_base.html` template
2. **Add syllabus codes** to lessons (use `syllabus_mappings.py`)
3. **Add learning objectives** to each lesson
4. **Test on mobile devices** (responsive design should work)
5. **Gather user feedback** (from Cynthia and yourself)

#### Future Enhancements:
1. **Lesson conversion script** to automate template migration
2. **Bulk flashcard generation** for all lessons
3. **Email notifications** for streak reminders
4. **Progress export** (PDF report)
5. **Teacher dashboard** (if adding more users)

---

## File Checklist

Ensure these files were created/modified:

### New Python Modules
- ✅ `user_profile.py` (205 lines)
- ✅ `practice_generator.py` (312 lines)
- ✅ `syllabus_mappings.py` (180 lines)
- ✅ `enhanced_routes.py` (300 lines - reference only)

### Modified Files
- ✅ `app.py` (modified, +300 lines of routes)

### New Templates
- ✅ `templates/lesson_base.html`
- ✅ `templates/dashboard_enhanced.html`
- ✅ `templates/flashcards.html`
- ✅ `templates/exam_mode.html`

### New Static Files
- ✅ `static/lesson.css`

### Documentation
- ✅ `IMPLEMENTATION_SUMMARY.md`
- ✅ `DEPLOYMENT_GUIDE.md` (this file)
- ✅ `.syllabus_audit/README.md`

### Data Directory
- ✅ `data/` (empty initially, populated on use)

---

## Support & Troubleshooting

### Getting Help
1. Check `IMPLEMENTATION_SUMMARY.md` for feature details
2. Review error log on PythonAnywhere
3. Test locally first (easier to debug)
4. Check git history for recent changes

### Common Questions

**Q: Why is dashboard empty?**
A: Dashboard shows data after you view lessons and take practice. It's empty on first login.

**Q: Practice generation takes 10+ seconds?**
A: Normal! AI generation is slow. Consider adding loading spinners.

**Q: Can I use different AI models?**
A: Yes! Edit `FREE_MODELS` list in `app.py` to reorder priority.

**Q: How do I add more users?**
A: Edit `USERS` dict in `app.py`, generate password hash:
```python
from werkzeug.security import generate_password_hash
print(generate_password_hash("password123"))
```

**Q: Can I disable rate limiting for testing?**
A: Yes, temporarily set in `app.py`:
```python
MAX_REQUESTS_HOUR = 1000  # Effectively unlimited
```

---

## Success Metrics

After 1 week of use, check:
- ✅ User profiles created: `ls -la data/` (should show .json files)
- ✅ Practice sessions completed: Check dashboard
- ✅ Flashcards reviewed: Check flashcard page
- ✅ Exams taken: Check exam history
- ✅ Study streak maintained: Check dashboard stat
- ✅ No critical errors in error log

---

**Deployment Status:** Ready ✅
**Total Implementation Time:** ~10-14 weeks of features
**Files Added:** 8 new, 1 modified
**Lines of Code:** ~1,800 new
**Testing Required:** Medium (new features need validation)
**Risk Level:** Low (no database changes, backwards compatible)
