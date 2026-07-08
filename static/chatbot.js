/**
 * Lessons — AI IB Tutor Chatbot
 * Connects to Flask backend which proxies Google Gemini API
 */

(function() {
  const chatbot = document.getElementById('chatbot');
  const toggleBtn = document.getElementById('chatbot-toggle');
  const closeBtn = document.getElementById('chatbot-close');
  const windowEl = document.getElementById('chatbot-window');
  const messagesEl = document.getElementById('chatbot-messages');
  const inputEl = document.getElementById('chatbot-input');
  const sendBtn = document.getElementById('chatbot-send');
  const statusEl = document.getElementById('chatbot-status');

  let chatHistory = [];
  let isWaiting = false;

  // ── CSRF token helper ──
  function getCsrfToken() {
    const meta = document.querySelector('meta[name="csrf-token"]');
    return meta ? meta.getAttribute('content') : '';
  }

  // ── Toggle window ──
  toggleBtn.addEventListener('click', () => {
    windowEl.classList.toggle('hidden');
    if (!windowEl.classList.contains('hidden')) {
      inputEl.focus();
    }
  });

  closeBtn.addEventListener('click', () => {
    windowEl.classList.add('hidden');
  });

  // ── Send message ──
  function sendMessage() {
    const text = inputEl.value.trim();
    if (!text || isWaiting) return;

    addMessage('user', text);
    chatHistory.push({ role: 'user', content: text });
    inputEl.value = '';
    isWaiting = true;
    sendBtn.disabled = true;
    showTyping();

    fetch('/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRF-Token': getCsrfToken()
      },
      body: JSON.stringify({
        message: text,
        history: chatHistory.slice(0, -1)  // exclude the just-added message
      })
    })
    .then(res => res.json())
    .then(data => {
      removeTyping();
      if (data.error) {
        addMessage('bot', '⚠️ ' + data.error);
        setStatus('Error — check API key configuration');
      } else {
        addMessage('bot', data.response);
        chatHistory.push({ role: 'model', content: data.response });
        setStatus('');
      }
    })
    .catch(err => {
      removeTyping();
      addMessage('bot', '⚠️ Connection error. Make sure the server is running.');
      setStatus('Connection error');
    })
    .finally(() => {
      isWaiting = false;
      sendBtn.disabled = false;
      inputEl.focus();
    });
  }

  sendBtn.addEventListener('click', sendMessage);
  inputEl.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });

  // Auto-resize textarea
  inputEl.addEventListener('input', () => {
    inputEl.style.height = 'auto';
    inputEl.style.height = Math.min(inputEl.scrollHeight, 100) + 'px';
  });

  // ── Add message to chat ──
  function addMessage(role, text) {
    const div = document.createElement('div');
    div.className = 'message ' + role;
    const content = document.createElement('div');
    content.className = 'message-content';
    // Split on newlines and wrap in <p>
    const paragraphs = text.split('\n').filter(p => p.trim() !== '');
    if (paragraphs.length === 0) {
      content.innerHTML = '<p>' + escapeHtml(text) + '</p>';
    } else {
      content.innerHTML = paragraphs.map(p => '<p>' + escapeHtml(p) + '</p>').join('');
    }
    div.appendChild(content);
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;

    // Re-render MathJax if available
    if (window.MathJax && window.MathJax.typesetPromise) {
      window.MathJax.typesetPromise([content]);
    }
  }

  function showTyping() {
    const div = document.createElement('div');
    div.className = 'message bot';
    div.id = 'typing-message';
    div.innerHTML = '<div class="message-content"><div class="typing-indicator"><span></span><span></span><span></span></div></div>';
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;
  }

  function removeTyping() {
    const el = document.getElementById('typing-message');
    if (el) el.remove();
  }

  function setStatus(msg) {
    statusEl.textContent = msg;
  }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // ── Check API config on load ──
  fetch('/config')
    .then(r => r.json())
    .then(data => {
      if (!data.api_configured) {
        setStatus('⚠️ API key not set — chat unavailable');
      }
    })
    .catch(() => {});
})();
