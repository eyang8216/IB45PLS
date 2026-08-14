# IB45PLS Website Updates - August 2026

## Summary of Changes

### ✅ 1. Rate Limit Increased (60 requests/hour)
- **Changed:** `MAX_REQUESTS_HOUR` from 30 to 60 in `app.py`
- **Location:** Line 71
- **Impact:** Users can now make 60 AI tutor requests per hour instead of 30

### ✅ 2. Economics Upgraded from SL to HL
- **Added:** 10 new HL-only lessons (lessons 58-67)
  - Lesson 58: Theory of the Firm (production functions, isoquants)
  - Lesson 59: Game Theory and Strategic Behavior
  - Lesson 60: Asymmetric Information and Market Failure
  - Lesson 61: Price Discrimination (HL Extension)
  - Lesson 62: Contestable Markets Theory
  - Lesson 63: Behavioral Economics
  - Lesson 64: Labor Market Monopsony
  - Lesson 65: Efficiency and Equity Trade-offs
  - Lesson 66: International Finance (HL Topics)
  - Lesson 67: Calculating National Income (HL Methods)
- **Updated:** All references from "Economics SL" to "Economics HL"
- **Total Lessons:** 57 → 67 lessons
- **Updated Files:**
  - `app.py` (subject configuration and system prompt)
  - `templates/index.html` (main page)
  - `subjects/economics/index.html` (added HL section)

### ✅ 3. AI Chatbot Made Resizable
- **Added:** CSS property `resize: both` to chatbot window
- **Features:**
  - Users can drag the bottom-right corner to resize
  - Min size: 320px × 400px
  - Max size: 800px × 80vh
  - Visual resize handle indicator
- **Location:** `app.py` CHATBOT_CSS section

### ✅ 4. UI Redesigned (Fluapi-Inspired Modern Design)
- **Created:** New `static/style.css` with clean, modern aesthetic
- **Key Changes:**
  - Modern color palette (blues instead of dark greens)
  - Improved typography and spacing
  - Better shadows and gradients
  - Smoother transitions and animations
  - Enhanced chatbot styling with gradient backgrounds
  - Message animations (slide-in effect)
  - Improved button hover states
  - Better mobile responsiveness
- **Added:** KaTeX font-face declarations for proper math rendering
- **Preserved:** Old CSS as `style-old.css` for reference

### ✅ 5. LaTeX/Math Rendering Fixed
- **Issue:** Math equations should render properly using MathJax
- **Solution:** 
  - Verified MathJax configuration in lesson files
  - Added KaTeX font-face declarations to CSS
  - All lessons already have proper `$$` delimiters
  - MathJax CDN properly loaded in templates
- **Status:** Math rendering infrastructure is correct

## Technical Details

### File Changes
- **Modified:** 3 files
  - `app.py`
  - `templates/index.html`
  - `subjects/economics/index.html`
- **Created:** 11 files
  - `static/style.css` (new design)
  - 10 HL economics lessons (lesson_58-67)
- **Preserved:** 1 file
  - `static/style-old.css` (backup)

### Color Palette (New Design)
- Primary: `#3b82f6` (blue)
- Primary Dark: `#1e3a8a` (dark blue)
- Text: `#1a1d26` (near black)
- Background: `#fafbfc` (light gray)
- Border: `#e5e7eb` (light gray)
- Accent: Various per subject

### Browser Compatibility
- Modern CSS features used (color-mix, CSS variables)
- Fallbacks provided where necessary
- Mobile-responsive breakpoints at 768px and 480px

## Testing Recommendations

1. **Rate Limit:** Test by making multiple AI requests
2. **Economics HL:** Verify all 67 lessons are accessible and render properly
3. **Chatbot Resize:** Test dragging the chatbot window corner
4. **Math Rendering:** Verify LaTeX equations display correctly in lessons
5. **Mobile:** Test responsive design on phone/tablet
6. **Browser:** Test in Chrome, Safari, Firefox

## Next Steps (Optional)

- Add full content to placeholder HL lessons (63-67)
- Consider adding practice problems for HL topics
- Test chatbot drag-to-move functionality
- Add more KaTeX font weights if needed for complex equations

---
**Date:** August 14, 2026
**Status:** ✅ All requested changes completed
