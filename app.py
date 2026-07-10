import os
import json
import time
import secrets
import urllib.request
import urllib.error
import re
from functools import wraps
from flask import Flask, render_template, request, jsonify, send_from_directory, abort, Response, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# ── Security config ──
app.secret_key = os.environ.get("FLASK_SECRET_KEY", secrets.token_hex(32))
app.config.update(
    SESSION_COOKIE_SECURE=False,   # Set True in production with HTTPS
    SESSION_COOKIE_HTTPONLY=True,  # Block JS access to session cookie
    SESSION_COOKIE_SAMESITE="Lax", # CSRF protection for cookies
    PERMANENT_SESSION_LIFETIME=86400,  # 24 hours
)

# OpenRouter API key
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "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")

# Gemini API key (free tier)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.0-flash"

# Free models on OpenRouter (tried in order, with fallback)
# Free models on OpenRouter — prioritized for IB tutoring quality
# Tier 1: Best for tutoring (large, instruction-tuned)
# Tier 2: Good fallbacks (solid quality)
# Tier 3: Fast/light (speed over depth)
FREE_MODELS = [
    # Tier 1: Best quality for tutoring + grading
    "meta-llama/llama-3.3-70b-instruct:free",
    "nvidia/nemotron-3-super-120b-a12b:free",
    "qwen/qwen3-next-80b-a3b-instruct:free",
    # Tier 2: Solid fallbacks
    "google/gemini-2.0-flash-001",
    "mistralai/mistral-7b-instruct",
    "tencent/hy3:free",
    "google/gemma-4-26b-a4b-it:free",
    # Tier 3: Fast & reliable
    "meta-llama/llama-3.2-3b-instruct:free",
]

# ── User store (hashed passwords, no plaintext storage) ──
# To add users later, run this in Python:
#   from werkzeug.security import generate_password_hash
#   print(generate_password_hash("the_password"))
USERS = {
    "EthanYang": {
        "password_hash": generate_password_hash("IB45", method="pbkdf2:sha256"),
        "name": "Ethan Yang",
    },
    "cynthia": {
        "password_hash": "pbkdf2:sha256:1000000$J2iCGUzR82eYLMRO$fcd5f658093594e43fec661da6c1b9b7b7a96ee51ef3f3578e8fa501d333577f",
        "name": "Cynthia",
    }
}

# ── Brute-force rate limiter (in-memory) ──
LOGIN_ATTEMPTS = {}  # {ip: [timestamp, timestamp, ...]}
MAX_ATTEMPTS = 5      # Max attempts
ATTEMPT_WINDOW = 300   # 5-minute window

# ── Chat/grading rate limiter (per user, 30 req/hour) ──
USER_REQUESTS = {}     # {username: [timestamp, timestamp, ...]}
MAX_REQUESTS_HOUR = 30  # 30 AI requests per user per hour
REQUEST_WINDOW = 3600   # 1-hour window

# Subject configuration
SUBJECTS = {
    "economics": {
        "name": "Economics SL",
        "icon": "📊",
        "color": "#2c6b4f",
        "folder": "subjects/economics",
        "index": "index.html",
        "description": "IB Economics SL — 57 lessons",
        "total_lessons": 57
    },
    "chemistry": {
        "name": "Chemistry HL",
        "icon": "🧪",
        "color": "#2c5f2d",
        "folder": "subjects/chemistry",
        "index": "index.html",
        "description": "IB Chemistry HL — 41 lessons",
        "total_lessons": 41,
        "subfolder": "lessons"
    },
    "physics": {
        "name": "Physics HL",
        "icon": "⚛️",
        "color": "#6c3483",
        "folder": "subjects/physics",
        "index": "index.html",
        "description": "IB Physics HL — 67 lessons",
        "total_lessons": 67
    },
    "math": {
        "name": "Math AA HL",
        "icon": "📐",
        "color": "#1a5276",
        "folder": "subjects/math",
        "index": "index.html",
        "description": "IB Math AA HL — 50 lessons",
        "total_lessons": 50
    },
    "chinese": {
        "name": "Chinese Lang Lit SL",
        "icon": "🇨🇳",
        "color": "#b22222",
        "folder": "subjects/chinese",
        "index": "index.html",
        "description": "IB Chinese Lang & Lit SL — Paper 1 & 2 practice",
        "total_lessons": 7
    },
    "english": {
        "name": "English Lang Lit SL",
        "icon": "🇬🇧",
        "color": "#1a5276",
        "folder": "subjects/english",
        "index": "index.html",
        "description": "IB English Lang & Lit SL — Paper 1 practice",
        "total_lessons": 3
    },
    "sat": {
        "name": "SAT Prep",
        "icon": "🎓",
        "color": "#e67e22",
        "folder": "subjects/sat",
        "index": "index.html",
        "description": "SAT — 50 lessons + 5 practice tests",
        "total_lessons": 50
    },
    "biology": {
        "name": "Biology HL",
        "icon": "🧬",
        "color": "#27ae60",
        "folder": "subjects/biology",
        "index": "index.html",
        "description": "IB Biology HL — 54 lessons",
        "total_lessons": 54
    }
}

SYSTEM_PROMPT = """You are a friendly, encouraging IB tutor assistant. You help students learn Economics SL, Chemistry HL, Physics HL, Math AA HL, Chinese Lang Lit SL, English Lang Lit SL, and Biology HL.

Your teaching style:
- Break down complex concepts into simple explanations
- Use analogies and examples relevant to a high school student
- When asked about problems, guide the student step-by-step rather than giving the answer immediately
- Use Socratic questioning to help students discover answers themselves
- Keep responses concise but thorough (~2-4 paragraphs)
- Use LaTeX notation ($$...$$ for display, $...$ for inline) when explaining math or formulas
- Be encouraging and celebrate understanding — these are challenging IB subjects!

Subject context available:
- Economics SL: Micro, Macro, International, Development — 57 lessons
- Chemistry HL: Stoichiometry, Atomic Structure, Bonding, Energetics, Kinetics, Equilibrium, Acids/Bases, Redox, Organic — 41 lessons  
- Physics HL: Mechanics, Thermal, Waves, Electricity, Fields, Quantum, Relativity, Nuclear — 67 lessons
- Math AA HL: Algebra, Functions, Trigonometry, Calculus, Vectors, Stats, Probability — 50 lessons
- Biology HL: Water, Nucleic Acids, Cells, Evolution, Biodiversity, Carbohydrates, Lipids, Proteins, Membranes, Organelles, Respiration, Photosynthesis, Genetics, Ecology, Human Physiology — 54 lessons
- Chinese Lang Lit SL: Paper 1 & 2 guided analysis practice
- English Lang Lit SL: Paper 1 guided analysis practice

If a student asks about a topic you're unsure of, be honest about limitations and suggest they consult their textbook or teacher."""


# ── Security: Decorators & Helpers ──

def login_required(f):
    """Decorator: redirect to login if not authenticated."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated


def check_rate_limit(ip):
    """Return True if IP is rate-limited."""
    now = time.time()
    attempts = LOGIN_ATTEMPTS.get(ip, [])
    # Purge old attempts
    attempts = [t for t in attempts if now - t < ATTEMPT_WINDOW]
    LOGIN_ATTEMPTS[ip] = attempts
    return len(attempts) >= MAX_ATTEMPTS


def record_attempt(ip):
    """Record a failed login attempt."""
    now = time.time()
    if ip not in LOGIN_ATTEMPTS:
        LOGIN_ATTEMPTS[ip] = []
    LOGIN_ATTEMPTS[ip].append(now)


def check_user_rate_limit(username):
    """Return True if user has exceeded AI request quota (30/hour)."""
    now = time.time()
    requests = USER_REQUESTS.get(username, [])
    requests = [t for t in requests if now - t < REQUEST_WINDOW]
    USER_REQUESTS[username] = requests
    return len(requests) >= MAX_REQUESTS_HOUR


def record_user_request(username):
    """Record an AI request for rate limiting."""
    now = time.time()
    if username not in USER_REQUESTS:
        USER_REQUESTS[username] = []
    USER_REQUESTS[username].append(now)
    # Keep max 50 entries to bound memory
    if len(USER_REQUESTS[username]) > 50:
        USER_REQUESTS[username] = USER_REQUESTS[username][-50:]


def generate_csrf_token():
    """Generate and store CSRF token in session."""
    if "_csrf_token" not in session:
        session["_csrf_token"] = secrets.token_hex(32)
    return session["_csrf_token"]


@app.before_request
def csrf_protect():
    """Validate CSRF token on all POST requests (except login which validates inline)."""
    if request.method == "POST":
        # Skip CSRF for login (handled in the login route itself)
        if request.path == "/login":
            return
        token = session.get("_csrf_token", "")
        submitted = request.headers.get("X-CSRF-Token", "")
        if not token or not submitted or not secrets.compare_digest(token, submitted):
            return jsonify({"error": "Invalid CSRF token"}), 403


@app.after_request
def security_headers(response):
    """Add security headers to every response."""
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "0"  # Deprecated, but belts-and-suspenders
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Cache-Control"] = "no-store, max-age=0"
    # CSP: allow our own scripts, MathJax CDN, and inline styles (needed for injected content)
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; "
        "style-src 'self' 'unsafe-inline'; "
        "img-src 'self' data:; "
        "font-src 'self' data:; "
        "connect-src 'self' https://openrouter.ai; "
        "frame-ancestors 'none'; "
        "form-action 'self'"
    )
    return response


# ── NAV + CHATBOT INJECTION SNIPPETS ──

NAV_CSS = """
/* ── Lessons Nav Bar ── */
.lessons-nav {
  background: linear-gradient(135deg, #1a1a2e, #16213e);
  color: white;
  padding: 0.6rem 1.2rem;
  margin: -2rem -1.5rem 1.5rem -1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-size: 0.9rem;
  flex-wrap: wrap;
}
.lessons-nav a {
  color: white;
  text-decoration: none;
  opacity: 0.85;
  transition: opacity 0.15s;
}
.lessons-nav a:hover { opacity: 1; }
.lessons-nav .nav-home { font-weight: 600; opacity: 1; }
.lessons-nav .nav-separator { opacity: 0.4; }
.lessons-nav .nav-current { opacity: 0.6; font-style: italic; }
"""

CHATBOT_CSS = """
/* ── Chatbot Widget ── */
#lessons-chatbot { position: fixed; bottom: 1.5rem; right: 1.5rem; z-index: 9999; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
#lessons-chatbot .chatbot-toggle { display: flex; align-items: center; gap: 0.5rem; padding: 0.7rem 1.3rem; background: #1a1a2e; color: white; border: none; border-radius: 50px; font-size: 0.95rem; cursor: pointer; box-shadow: 0 4px 15px rgba(0,0,0,0.25); transition: all 0.2s; }
#lessons-chatbot .chatbot-toggle:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,0.35); background: #16213e; }
#lessons-chatbot .chatbot-icon { font-size: 1.4rem; margin-right: 0.1rem; }
#lessons-chatbot .chatbot-window { position: absolute; bottom: 70px; right: 0; width: 420px; max-height: 600px; background: white; border-radius: 16px; box-shadow: 0 10px 40px rgba(0,0,0,0.25); display: flex; flex-direction: column; overflow: hidden; border: 1px solid #ddd; }
#lessons-chatbot .chatbot-window.hidden { display: none; }
#lessons-chatbot .chatbot-header { background: linear-gradient(135deg, #1a1a2e, #16213e); color: white; padding: 0.8rem 1rem; position: relative; }
#lessons-chatbot .chatbot-header h3 { font-size: 1rem; font-weight: 600; margin: 0 0 0.1rem; color: white; }
#lessons-chatbot .chatbot-header p { font-size: 0.75rem; opacity: 0.8; margin: 0; }
#lessons-chatbot .chatbot-close { position: absolute; top: 0.5rem; right: 0.7rem; background: none; border: none; color: white; font-size: 1.1rem; cursor: pointer; opacity: 0.7; }
#lessons-chatbot .chatbot-close:hover { opacity: 1; }
#lessons-chatbot .chatbot-messages { flex: 1; overflow-y: auto; padding: 0.8rem; display: flex; flex-direction: column; gap: 0.6rem; max-height: 420px; background: #fafaf8; }
#lessons-chatbot .chatbot-messages .msg { display: flex; }
#lessons-chatbot .chatbot-messages .msg.user { justify-content: flex-end; }
#lessons-chatbot .chatbot-messages .msg-content { max-width: 85%; padding: 0.6rem 0.9rem; border-radius: 16px; font-size: 0.85rem; line-height: 1.5; }
#lessons-chatbot .chatbot-messages .msg.user .msg-content { background: #1a1a2e; color: white; border-bottom-right-radius: 4px; }
#lessons-chatbot .chatbot-messages .msg.bot .msg-content { background: white; border: 1px solid #e0e0e0; border-bottom-left-radius: 4px; }
#lessons-chatbot .chatbot-messages .msg-content p { margin: 0 0 0.3rem; }
#lessons-chatbot .chatbot-messages .msg-content p:last-child { margin-bottom: 0; }
#lessons-chatbot .chatbot-input-area { display: flex; gap: 0.3rem; padding: 0.6rem 0.7rem; border-top: 1px solid #e0e0e0; background: white; }
#lessons-chatbot .chatbot-input-area textarea { flex: 1; border: 1px solid #ddd; border-radius: 18px; padding: 0.5rem 0.9rem; font-size: 0.85rem; font-family: inherit; resize: none; outline: none; max-height: 90px; }
#lessons-chatbot .chatbot-input-area textarea:focus { border-color: #1a1a2e; }
#lessons-chatbot .chatbot-input-area button { width: 36px; height: 36px; border-radius: 50%; border: none; background: #1a1a2e; color: white; font-size: 1rem; cursor: pointer; flex-shrink: 0; }
#lessons-chatbot .chatbot-input-area button:disabled { background: #ccc; }
#lessons-chatbot .chatbot-status { text-align: center; font-size: 0.7rem; color: #999; padding: 0.2rem; min-height: 20px; }
#lessons-chatbot .typing { display: flex; gap: 4px; padding: 0.4rem 0; }
#lessons-chatbot .typing span { width: 7px; height: 7px; border-radius: 50%; background: #aaa; animation: lcb 1.4s ease-in-out infinite; }
#lessons-chatbot .typing span:nth-child(2) { animation-delay: 0.2s; }
#lessons-chatbot .typing span:nth-child(3) { animation-delay: 0.4s; }
@keyframes lcb { 0%,60%,100%{transform:translateY(0);opacity:0.4} 30%{transform:translateY(-5px);opacity:1} }
@media (max-width: 420px) { #lessons-chatbot .chatbot-window { width: calc(100vw - 1.5rem); right: -0.2rem; } }
"""

CHATBOT_HTML = """
<div id="lessons-chatbot">
  <button class="chatbot-toggle" onclick="this.nextElementSibling.classList.toggle('hidden')">
    <span class="chatbot-icon">\U0001F916</span> Ask AI Tutor
  </button>
  <div class="chatbot-window hidden">
    <div class="chatbot-header">
      <h3>\U0001F916 AI IB Tutor</h3>
      <p class="chatbot-context-label">Ask anything about your current subject</p>
      <button class="chatbot-close" onclick="this.closest('.chatbot-window').classList.add('hidden')">\u2715</button>
    </div>
    <div class="chatbot-messages">
      <div class="msg bot"><div class="msg-content"><p>Hi! I'm your IB tutor. I can see you're studying <strong class="chatbot-context-display">IB</strong>. What would you like help with?</p></div></div>
    </div>
    <div class="chatbot-input-area">
      <textarea placeholder="Ask a question..." rows="1"></textarea>
      <button onclick="lessonsChatbotSend()">\u27A4</button>
    </div>
    <div class="chatbot-status"></div>
  </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
"""

CHATBOT_JS = """
<script>
(function() {
  var win = document.querySelector('#lessons-chatbot .chatbot-window');
  var msgs = win.querySelector('.chatbot-messages');
  var input = win.querySelector('textarea');
  var btn = win.querySelector('.chatbot-input-area button');
  var status = win.querySelector('.chatbot-status');
  var history = [];
  var waiting = false;

  // Extract page context
  var path = window.location.pathname;
  var subjectKey = '';
  var subjectName = '';
  var matches = path.match(/\\/subjects\\/([^\\/]+)/);
  if (matches) {
    subjectKey = matches[1];
    var names = {economics:'Economics SL',chemistry:'Chemistry HL',physics:'Physics HL',math:'Math AA HL'};
    subjectName = names[subjectKey] || subjectKey;
  }
  var pageTitle = document.title || '';
  pageTitle = pageTitle.replace(/\\s*[-–—|].*IB.*/,'').trim();

  var greeting = win.querySelector('.chatbot-context-display');
  if (greeting && subjectName) {
    greeting.textContent = subjectName;
    if (pageTitle) greeting.textContent += ' — ' + pageTitle;
  }
  var ctxLabel = win.querySelector('.chatbot-context-label');
  if (ctxLabel && pageTitle) {
    ctxLabel.textContent = 'Currently viewing: ' + pageTitle;
  }

  window.lessonsChatbotSend = function() {
    var text = input.value.trim();
    if (!text || waiting) return;

    addMsg('user', text);
    history.push({role:'user',content:text});
    input.value = '';
    waiting = true;
    btn.disabled = true;
    showTyping();

    var ctx = {subject: subjectKey, subject_name: subjectName, lesson: pageTitle};

    fetch('/chat', {
      method:'POST',
      headers:{'Content-Type':'application/json', 'X-CSRF-Token': getCsrf()},
      body: JSON.stringify({message:text, history:history.slice(0,-1), context:ctx})
    })
    .then(function(r){return r.json();})
    .then(function(data){
      removeTyping();
      if (data.error) { addMsg('bot','\\u26A0\\uFE0F '+data.error); }
      else { addMsg('bot', data.response); history.push({role:'assistant',content:data.response}); }
    })
    .catch(function(){
      removeTyping(); addMsg('bot','\\u26A0\\uFE0F Connection error.');
    })
    .finally(function(){
      waiting=false; btn.disabled=false; input.focus();
    });
  };

  input.addEventListener('keydown', function(e) {
    if (e.key==='Enter' && !e.shiftKey) { e.preventDefault(); lessonsChatbotSend(); }
  });
  input.addEventListener('input', function() {
    this.style.height='auto'; this.style.height=Math.min(this.scrollHeight,90)+'px';
  });

  function addMsg(role, text) {
    var d = document.createElement('div'); d.className='msg '+role;
    var c = document.createElement('div'); c.className='msg-content';
    var ps = text.split('\\n').filter(function(p){return p.trim();});
    if (ps.length===0) ps=[text];
    c.innerHTML = typeof marked !== 'undefined' ? marked.parse(text) : ps.map(function(p){return '<p>'+esc(p)+'</p>';}).join('');
    d.appendChild(c); msgs.appendChild(d); msgs.scrollTop=msgs.scrollHeight;
    if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([c]);
  }

  function showTyping() {
    var d = document.createElement('div'); d.className='msg bot'; d.id='ltyping';
    d.innerHTML='<div class=\"msg-content\"><div class=\"typing\"><span></span><span></span><span></span></div></div>';
    msgs.appendChild(d); msgs.scrollTop=msgs.scrollHeight;
  }
  function removeTyping() { var e=document.getElementById('ltyping'); if(e)e.remove(); }
  function esc(s) { var d=document.createElement('div'); d.textContent=s; return d.innerHTML; }

  // Read CSRF token from meta tag
  function getCsrf() {
    var m = document.querySelector('meta[name=\"csrf-token\"]');
    return m ? m.getAttribute('content') : '';
  }
})();
</script>
"""


def inject_into_html(html_content, subject_key):
    """Inject nav bar + chatbot + CSRF meta tag into an HTML lesson page."""
    subject = SUBJECTS.get(subject_key, {})
    subj_name = subject.get("name", subject_key)
    subj_color = subject.get("color", "#1a1a2e")
    subj_icon = subject.get("icon", "📚")

    # Build nav bar
    nav = f'<nav class="lessons-nav" style="background:linear-gradient(135deg,{subj_color},#1a1a2e)">'
    nav += f'<a href="/" class="nav-home">📚 Lessons</a>'
    nav += f'<span class="nav-separator">›</span>'
    nav += f'<a href="/subjects/{subject_key}/">{subj_icon} {subj_name}</a>'
    nav += f'</nav>'

    # CSRF meta tag for JS to read
    csrf_token = generate_csrf_token()
    csrf_meta = f'<meta name="csrf-token" content="{csrf_token}">'

    # Inject CSRF meta into head
    html_content = html_content.replace('</head>', csrf_meta + '\n</head>')

    # Inject nav CSS
    if '<style>' in html_content:
        html_content = html_content.replace('<style>', '<style>\n' + NAV_CSS, 1)
    else:
        html_content = html_content.replace('</head>', '<style>' + NAV_CSS + '</style>\n</head>')

    # Inject chatbot CSS
    html_content = html_content.replace('</style>', CHATBOT_CSS + '\n</style>', 1)

    # Remove any existing <nav> and inject ours after <body>
    html_content = re.sub(r'<nav>.*?</nav>', '', html_content, flags=re.DOTALL)
    html_content = html_content.replace('<body>', '<body>\n' + nav)

    # Inject chatbot HTML + JS before </body>
    html_content = html_content.replace('</body>', CHATBOT_HTML + CHATBOT_JS + '\n</body>')

    return html_content


# ── ROUTES ──

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        client_ip = request.remote_addr

        # Rate limit check
        if check_rate_limit(client_ip):
            error = "Too many login attempts. Please wait 5 minutes."
            return render_template("login.html", error=error, csrf_token=generate_csrf_token()), 429

        # CSRF check for login form
        token = session.get("_csrf_token", "")
        submitted = request.form.get("_csrf_token", "")
        if not token or not secrets.compare_digest(token, submitted):
            record_attempt(client_ip)
            error = "Invalid form submission. Please try again."
            return render_template("login.html", error=error, csrf_token=generate_csrf_token()), 403

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        # Validate input
        if not username or not password:
            error = "Username and password are required."
        elif len(username) > 50 or len(password) > 128:
            error = "Invalid input length."
        elif username not in USERS:
            record_attempt(client_ip)
            error = "Invalid username or password."
        elif not check_password_hash(USERS[username]["password_hash"], password):
            record_attempt(client_ip)
            error = "Invalid username or password."
        else:
            # Success — clear attempts and set session
            LOGIN_ATTEMPTS.pop(client_ip, None)
            session.clear()
            session["user"] = username
            session["user_name"] = USERS[username]["name"]
            session["_csrf_token"] = secrets.token_hex(32)  # regenerate after login
            session.permanent = True
            return redirect(url_for("home"))

        return render_template("login.html", error=error, csrf_token=generate_csrf_token())

    return render_template("login.html", error=error, csrf_token=generate_csrf_token())


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/")
@login_required
def home():
    return render_template("index.html", csrf_token=generate_csrf_token())


# SAT ROUTES
# ═══════════════════════════════════════════════════════════

@app.route("/subjects/sat/")
@login_required
def sat_index():
    track_lesson_view(session.get("user",""), "sat", "index")
    sat_dir = os.path.join(os.path.dirname(__file__), "subjects", "sat")
    # Serve the lessons index if it exists
    index_path = os.path.join(sat_dir, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()
        content = inject_into_html(content, "sat")
        return content, 200, {"Content-Type": "text/html; charset=utf-8"}
    abort(404)

@app.route("/subjects/sat/<path:filename>")
@login_required
def sat_lesson(filename):
    track_lesson_view(session.get("user",""), "sat", filename)
    sat_dir = os.path.join(os.path.dirname(__file__), "subjects", "sat")
    filepath = os.path.join(sat_dir, filename)
    if not os.path.exists(filepath):
        abort(404)
    if filename.endswith(".html"):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        content = inject_into_html(content, "sat")
        return content, 200, {"Content-Type": "text/html; charset=utf-8"}
    return send_from_directory(sat_dir, filename)

@app.route("/subjects/sat/practice")
@login_required
def sat_practice():
    tests = load_sat_tests()
    return render_template("sat_practice.html",
        tests=tests,
        csrf_token=generate_csrf_token())

@app.route("/subjects/<subject>/")
@app.route("/subjects/<subject>/<path:filename>")
@login_required
def serve_subject(subject, filename="index.html"):
    if subject not in SUBJECTS:
        abort(404)

    # Track lesson view for dashboard
    track_lesson_view(session.get("user", ""), subject, filename)

    subj = SUBJECTS[subject]
    folder = os.path.join(os.path.dirname(__file__), subj["folder"])
    index_file = subj.get("index", "index.html")

    if filename == index_file or filename == "":
        filepath = os.path.join(folder, filename) if filename else os.path.join(folder, index_file)
        if os.path.exists(filepath) and filepath.endswith('.html'):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            content = inject_into_html(content, subject)
            return content, 200, {'Content-Type': 'text/html; charset=utf-8'}
        abort(404)

    filepath = os.path.join(folder, filename)
    if not os.path.exists(filepath):
        abort(404)

    if filename.endswith('.html'):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        content = inject_into_html(content, subject)
        return content, 200, {'Content-Type': 'text/html; charset=utf-8'}

    return send_from_directory(folder, filename)


def call_openrouter(messages, model):
    """Call OpenRouter API with a specific model."""
    body = json.dumps({
        "model": model,
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 1024,
        "stop": ["<unk>", "<|endoftext|>"],
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=body,
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:5050",
            "X-Title": "Lessons IB Study Hub",
        }
    )

    resp = urllib.request.urlopen(req, timeout=30)
    data = json.loads(resp.read().decode("utf-8"))
    reply = data["choices"][0]["message"]["content"]
    # Clean garbled <unk> tokens from unstable models
    reply = re.sub(r'<unk>+', '', reply)
    reply = re.sub(r'<\|endoftext\|>', '', reply)
    return reply


def call_gemini(messages):
    """Call Gemini API (free tier — works on PythonAnywhere free plan)."""
    # Convert OpenAI-format messages to Gemini format
    contents = []
    system_instruction = None
    
    for msg in messages:
        role = msg["role"]
        text = msg["content"]
        if role == "system":
            system_instruction = {"parts": [{"text": text}]}
        elif role == "user":
            contents.append({"role": "user", "parts": [{"text": text}]})
        elif role == "assistant":
            contents.append({"role": "model", "parts": [{"text": text}]})
    
    body = {
        "contents": contents,
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 1024,
        }
    }
    if system_instruction:
        body["systemInstruction"] = system_instruction
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"
    
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    
    resp = urllib.request.urlopen(req, timeout=30)
    data = json.loads(resp.read().decode("utf-8"))
    return data["candidates"][0]["content"]["parts"][0]["text"]


def call_ai(messages):
    """Try free OpenRouter models with retry on rate limits, fall back to Gemini."""
    tried_models = []
    for model in FREE_MODELS:
        for attempt in range(2):  # up to 2 tries per model
            try:
                reply = call_openrouter(messages, model)
                return reply, model
            except urllib.error.HTTPError as e:
                tried_models.append(f"{model}:{e.code}")
                if e.code == 429:  # Rate limited — quick back off
                    time.sleep(0.8 * (attempt + 1))
                    continue
                elif e.code in (404, 403, 401):
                    break  # Skip this model
                else:
                    break
            except Exception as e:
                tried_models.append(f"{model}:{str(e)[:40]}")
                break
        # If we exhausted retries or the model is bad, move to next
    
    # Fallback to Gemini
    if GEMINI_API_KEY:
        try:
            reply = call_gemini(messages)
            return reply, GEMINI_MODEL
        except Exception as e:
            raise Exception(f"All models failed (tried: {', '.join(tried_models)}). Gemini: {e}")
    
    raise Exception(f"All models failed: {', '.join(tried_models)}")


@app.route("/chat", methods=["POST"])
@login_required
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message'."}), 400

    # Rate limit check
    username = session.get("user", "anonymous")
    if check_user_rate_limit(username):
        return jsonify({"error": "Rate limit reached. You can send 30 AI requests per hour. Please wait a bit."}), 429
    record_user_request(username)

    user_message = data["message"]
    history = data.get("history", [])
    context = data.get("context", {})

    system = SYSTEM_PROMPT
    if context:
        subj = context.get("subject_name", "")
        lesson = context.get("lesson", "")
        if subj and lesson:
            system += f"\n\nThe student is currently viewing: {subj} — {lesson}. "
            system += "Use this context to give more relevant and specific answers. "
            system += "Reference specific topics from this lesson when helpful."
        elif subj:
            system += f"\n\nThe student is currently studying: {subj}. "
            system += "Tailor your answers to this subject."

    messages = [{"role": "system", "content": system}]
    for msg in history:
        role = "user" if msg["role"] == "user" else "assistant"
        messages.append({"role": role, "content": msg["content"]})
    messages.append({"role": "user", "content": user_message})

    try:
        reply, model = call_ai(messages)
        return jsonify({"response": reply, "model": model})
    except Exception as e:
        return jsonify({"error": f"All AI APIs unavailable: {e}"}), 500


@app.route("/config")
@login_required
def config():
    return jsonify({"api_configured": bool(OPENROUTER_API_KEY or GEMINI_API_KEY)})


@app.route("/api-config")
@login_required
def api_config():
    """Return API key and prompts to the browser for client-side AI calls."""
    return jsonify({
        "openrouter_key": OPENROUTER_API_KEY,
        "system_prompt": SYSTEM_PROMPT,
        "grading_rubric": IB_LANG_LIT_RUBRIC,
        "free_models": FREE_MODELS,
    })


"""
New routes added for Phase 1-3: Chinese/English paper practice, dashboard, SAT
Inserted before `if __name__ == "__main__":` in app.py
"""
# ═══════════════════════════════════════════════════════════
# PRACTICE CONTENT LOADER
# ═══════════════════════════════════════════════════════════
PRACTICE_DATA = {}
try:
    with open(os.path.join(os.path.dirname(__file__), "practice_content.json"), "r", encoding="utf-8") as f:
        PRACTICE_DATA = json.load(f)
except Exception:
    pass

# ═══════════════════════════════════════════════════════════
# IB LANG LIT A SL RUBRIC (used in system prompt for grading)
# ═══════════════════════════════════════════════════════════
IB_LANG_LIT_RUBRIC = """You are a STRICT IB examiner. Grade this essay against the IB Language A: Language and Literature SL rubric.

IMPORTANT GRADING PHILOSOPHY:
- It is BETTER TO UNDERMARK than to overmark. Be brutally honest.
- Most student essays score 2-3 per criterion, not 4-5. Only award top marks for truly exceptional work.
- A score of 3 means "solid, meets expectations for SL." Not "average."
- A score of 4 means "well above expectations." 
- A score of 5 means "near-perfect, rarely awarded." Do NOT give 5s easily.
- If the essay lacks textual references, cap Criterion A at 2.
- If the essay is purely descriptive with no analysis of authorial choices, cap Criterion B at 2.
- If the essay has no clear thesis or structure, cap Criterion C at 2.
- Grammar errors or informal register should pull Criterion D down to 2-3.
- For every point deducted, explain EXACTLY what the student must do to improve.
- Give 2-3 specific, actionable improvements in every criterion comment.

CRITERION A: Understanding and Interpretation (0-5)
- 0-1: No understanding shown or completely off-topic
- 2: Surface-level understanding, few or no textual references, relies on summary
- 3: Adequate understanding with some references, basic interpretation
- 4: Strong understanding with well-chosen references and meaningful interpretation
- 5: Exceptional insight, nuanced interpretation, references are integral to argument

CRITERION B: Analysis and Evaluation (0-5)
- 0-1: No analysis or completely irrelevant
- 2: Mostly descriptive, identifies features but doesn't analyze their effects
- 3: Analyzes some authorial choices and their effects on the reader
- 4: Strong analysis that evaluates how specific features create meaning
- 5: Sophisticated evaluation of how authorial choices work together to produce complex effects

CRITERION C: Focus and Organization (0-5)
- 0-1: No discernible organization
- 2: Some structure but meanders, lacks clear thesis or topic sentences
- 3: Clear introduction-body-conclusion, mostly stays on topic
- 4: Well-organized with logical flow, each paragraph serves a purpose
- 5: Flawless organization, seamless transitions, sustained analytical focus

CRITERION D: Language (0-5)
- 0-1: Language errors significantly obscure meaning
- 2: Frequent errors, informal or inappropriate register for academic writing
- 3: Generally clear and accurate, appropriate register with some lapses
- 4: Clear, precise, effective academic register with stylistic awareness
- 5: Masterful control of language, sophisticated vocabulary, flawless academic style

Provide your response in this exact JSON format:
{
  "criterion_a": {"score": X, "comment": "What worked + 2-3 specific improvements needed"},
  "criterion_b": {"score": X, "comment": "What worked + 2-3 specific improvements needed"},
  "criterion_c": {"score": X, "comment": "What worked + 2-3 specific improvements needed"},
  "criterion_d": {"score": X, "comment": "What worked + 2-3 specific improvements needed"},
  "total": X,
  "overall_feedback": "Start with the biggest weakness. Then give 1 strength. End with the #1 priority for improvement. Be direct - no sugarcoating."
}

Reference specific parts of the student's essay. Do not be encouraging for the sake of being nice — accuracy and honesty come first."""

# ═══════════════════════════════════════════════════════════
# DASHBOARD DATA HELPERS
# ═══════════════════════════════════════════════════════════
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def get_user_data(username):
    """Load user data from JSON file."""
    if not username:
        return {}
    filepath = os.path.join(DATA_DIR, f"{username}.json")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "lesson_views": {},
        "mock_attempts": [],
        "sat_attempts": []
    }

def save_user_data(username, data):
    """Save user data to JSON file."""
    os.makedirs(DATA_DIR, exist_ok=True)
    filepath = os.path.join(DATA_DIR, f"{username}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)

def track_lesson_view(username, subject, lesson):
    """Record that a user viewed a lesson."""
    data = get_user_data(username)
    if "lesson_views" not in data:
        data["lesson_views"] = {}
    if subject not in data["lesson_views"]:
        data["lesson_views"][subject] = []
    if lesson not in data["lesson_views"][subject]:
        data["lesson_views"][subject].append(lesson)
    save_user_data(username, data)

# ═══════════════════════════════════════════════════════════
# SAT PRACTICE TEST LOADER
# ═══════════════════════════════════════════════════════════
def load_sat_tests():
    """Load all SAT practice tests from the SAT folder."""
    sat_dir = os.path.join(os.path.dirname(__file__), "subjects", "sat", "practice_tests")
    tests = {}
    if not os.path.exists(sat_dir):
        return tests
    for test_name in sorted(os.listdir(sat_dir)):
        test_path = os.path.join(sat_dir, test_name)
        if os.path.isdir(test_path):
            modules = {}
            for mod_file in sorted(os.listdir(test_path)):
                if mod_file.endswith(".md") and mod_file != "answer_key.md":
                    with open(os.path.join(test_path, mod_file), "r", encoding="utf-8") as f:
                        modules[mod_file.replace(".md", "")] = f.read()
            if modules:
                tests[test_name] = modules
    return tests

# ═══════════════════════════════════════════════════════════
# ROUTES: CHINESE & ENGLISH PAPER PRACTICE
# ═══════════════════════════════════════════════════════════

@app.route("/subjects/chinese/")
@login_required
def chinese_index():
    track_lesson_view(session.get("user",""), "chinese", "index")
    folder = os.path.join(os.path.dirname(__file__), "subjects", "chinese")
    return send_from_directory(folder, "index.html")

@app.route("/subjects/english/")
@login_required
def english_index():
    track_lesson_view(session.get("user",""), "english", "index")
    folder = os.path.join(os.path.dirname(__file__), "subjects", "english")
    return send_from_directory(folder, "index.html")

@app.route("/subjects/chinese/paper1/<prompt_id>")
@login_required
def chinese_paper1(prompt_id):
    prompts = PRACTICE_DATA.get("chinese", {}).get("paper1_prompts", [])
    prompt = next((p for p in prompts if p["id"] == prompt_id), None)
    if not prompt:
        abort(404)
    track_lesson_view(session.get("user",""), "chinese", f"paper1_{prompt_id}")
    return render_template("practice.html",
        subject="chinese", subject_name="Chinese Lang & Lit SL",
        paper="Paper 1", prompt=prompt, mode="paper1",
        csrf_token=generate_csrf_token())

@app.route("/subjects/chinese/paper2/<prompt_id>")
@login_required
def chinese_paper2(prompt_id):
    prompts = PRACTICE_DATA.get("chinese", {}).get("paper2_prompts", [])
    prompt = next((p for p in prompts if p["id"] == prompt_id), None)
    if not prompt:
        abort(404)
    track_lesson_view(session.get("user",""), "chinese", f"paper2_{prompt_id}")
    return render_template("practice.html",
        subject="chinese", subject_name="Chinese Lang & Lit SL",
        paper="Paper 2", prompt=prompt, mode="paper2",
        csrf_token=generate_csrf_token())

@app.route("/subjects/english/paper1/<prompt_id>")
@login_required
def english_paper1(prompt_id):
    prompts = PRACTICE_DATA.get("english", {}).get("paper1_prompts", [])
    prompt = next((p for p in prompts if p["id"] == prompt_id), None)
    if not prompt:
        abort(404)
    track_lesson_view(session.get("user",""), "english", f"paper1_{prompt_id}")
    return render_template("practice.html",
        subject="english", subject_name="English Lang & Lit SL",
        paper="Paper 1", prompt=prompt, mode="paper1",
        csrf_token=generate_csrf_token())

# ═══════════════════════════════════════════════════════════
# ROUTE: AI GRADING ENDPOINT
# ═══════════════════════════════════════════════════════════

@app.route("/grade", methods=["POST"])
@login_required
def grade_essay():
    # Rate limit check
    username = session.get("user", "anonymous")
    if check_user_rate_limit(username):
        return jsonify({"error": "Rate limit reached (30 AI requests/hour). Please wait."}), 429
    record_user_request(username)

    data = request.get_json()
    essay = (data.get("essay", "") or "").strip()
    prompt_text = (data.get("prompt", "") or "").strip()
    passage = (data.get("passage", "") or "").strip()
    subject = data.get("subject", "")
    mode = data.get("mode", "paper1")

    if not essay or len(essay) < 50:
        return jsonify({"error": "Please write at least 50 characters."}), 400

    # Build grading prompt
    grading_prompt = f"""You are an IB examiner for Language A: Language and Literature SL.

The student was given this task:

PASSAGE/TEXT:
{passage}

PROMPT:
{prompt_text}

The student wrote this response:
---
{essay}
---

{IB_LANG_LIT_RUBRIC}

IMPORTANT: Return ONLY valid JSON, no other text."""

    messages = [
        {"role": "system", "content": "You are a strict but fair IB examiner. Return only valid JSON."},
        {"role": "user", "content": grading_prompt}
    ]

    try:
        reply, model = call_ai(messages)
        # Try to parse JSON from reply
        reply_clean = reply.strip()
        if reply_clean.startswith("```"):
            reply_clean = re.sub(r'^```\w*\n?', '', reply_clean)
            reply_clean = re.sub(r'\n?```$', '', reply_clean)
        result = json.loads(reply_clean)

        # Save attempt to dashboard
        username = session.get("user", "")
        user_data = get_user_data(username)
        user_data.setdefault("mock_attempts", []).append({
            "date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "subject": subject,
            "mode": mode,
            "prompt_id": data.get("prompt_id", ""),
            "prompt_title": data.get("prompt_title", ""),
            "essay_preview": essay[:300],
            "scores": result
        })
        save_user_data(username, user_data)

        return jsonify(result)
    except (json.JSONDecodeError, ValueError) as e:
        return jsonify({"error": f"AI response could not be parsed as JSON. Try again. {e}"}), 500
    except Exception as e:
        return jsonify({"error": f"Grading failed: {e}"}), 500

# ═══════════════════════════════════════════════════════════
# ROUTE: SAVE GRADING RESULT (client-side AI → server storage)
# ═══════════════════════════════════════════════════════════

@app.route("/save-result", methods=["POST"])
@login_required
def save_result():
    """Save a grading result from client-side AI to user's history."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided."}), 400

    username = session.get("user", "")
    user_data = get_user_data(username)

    result_type = data.get("type", "mock")  # "mock" or "sat"

    if result_type == "mock":
        user_data.setdefault("mock_attempts", []).append({
            "date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "subject": data.get("subject", ""),
            "mode": data.get("mode", ""),
            "prompt_id": data.get("prompt_id", ""),
            "prompt_title": data.get("prompt_title", ""),
            "essay_preview": (data.get("essay_preview", "") or "")[:300],
            "scores": data.get("scores", {})
        })
    elif result_type == "sat":
        user_data.setdefault("sat_attempts", []).append({
            "date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "module": data.get("module", ""),
            "feedback": (data.get("feedback", "") or "")[:2000]
        })

    save_user_data(username, user_data)
    return jsonify({"ok": True})

@app.route("/track", methods=["POST"])
@login_required
def track_view():
    data = request.get_json() or {}
    subject = data.get("subject", "")
    lesson = data.get("lesson", "")
    if subject and lesson:
        track_lesson_view(session.get("user", ""), subject, lesson)
    return jsonify({"ok": True})

# ═══════════════════════════════════════════════════════════
# ROUTE: USER DASHBOARD
# ═══════════════════════════════════════════════════════════

@app.route("/dashboard")
@login_required
def dashboard():
    username = session.get("user", "")
    user_data = get_user_data(username)
    user_name = session.get("user_name", username)

    mock_attempts = user_data.get("mock_attempts", [])
    sat_attempts = user_data.get("sat_attempts", [])
    lesson_views = user_data.get("lesson_views", {})

    # Subject progress tracking
    subject_progress = {}
    for key, subj in SUBJECTS.items():
        if key == "sat":
            continue  # SAT tracked separately
        total = subj.get("total_lessons", 0)
        viewed = len(lesson_views.get(key, []))
        if total > 0:
            subject_progress[key] = {
                "name": subj["name"],
                "icon": subj["icon"],
                "viewed": viewed,
                "total": total,
                "pct": round(viewed / total * 100)
            }

    return render_template("dashboard.html",
        user_name=user_name,
        mock_attempts=mock_attempts[-30:],
        sat_attempts=sat_attempts[-30:],
        subject_progress=subject_progress,
        csrf_token=generate_csrf_token())

# ═══════════════════════════════════════════════════════════

@app.route("/sat/grade", methods=["POST"])
@login_required
def grade_sat():
    # Rate limit check
    username = session.get("user", "anonymous")
    if check_user_rate_limit(username):
        return jsonify({"error": "Rate limit reached (30 AI requests/hour). Please wait."}), 429
    record_user_request(username)

    data = request.get_json()
    answers = data.get("answers", "")
    questions = data.get("questions", "")
    module_name = data.get("module", "")

    if not answers or len(answers) < 10:
        return jsonify({"error": "Please provide your answers."}), 400

    grading_prompt = f"""You are an SAT tutor grading a practice test.

Here are the questions:
{questions[:3000]}

Student's answers:
{answers[:2000]}

Grade the student's work. Tell them which questions they got right/wrong. 
For wrong answers, provide a brief explanation of the correct approach.
Give an estimated score and areas to improve.

Be encouraging but honest."""

    messages = [
        {"role": "system", "content": "You are an experienced SAT tutor. Be specific and helpful."},
        {"role": "user", "content": grading_prompt}
    ]

    try:
        reply, model = call_ai(messages)
        # Save to dashboard
        username = session.get("user", "")
        user_data = get_user_data(username)
        user_data.setdefault("sat_attempts", []).append({
            "date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "module": module_name,
            "answers_preview": answers[:300],
            "feedback": reply
        })
        save_user_data(username, user_data)

        return jsonify({"response": reply, "model": model})
    except Exception as e:
        return jsonify({"error": f"Grading failed: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=False, port=5050)
