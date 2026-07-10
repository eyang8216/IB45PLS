/**
 * Lessons — AI IB Tutor Chatbot
 * Calls OpenRouter directly from the browser (works on PythonAnywhere free tier)
 */
(function() {
  const toggleBtn = document.getElementById('chatbot-toggle');
  const closeBtn = document.getElementById('chatbot-close');
  const windowEl = document.getElementById('chatbot-window');
  const messagesEl = document.getElementById('chatbot-messages');
  const inputEl = document.getElementById('chatbot-input');
  const sendBtn = document.getElementById('chatbot-send');
  const statusEl = document.getElementById('chatbot-status');

  let chatHistory = [];
  let isWaiting = false;
  let apiConfig = null;
  let configReady = false;

  // ── Load API config from server (returns a promise) ──
  const configPromise = fetch('/api-config')
    .then(r => r.json())
    .then(cfg => {
      apiConfig = cfg;
      configReady = true;
      if (!cfg.openrouter_key) {
        setStatus('⚠️ API key missing');
      } else {
        setStatus('');
      }
    })
    .catch(err => {
      setStatus('⚠️ Could not reach server');
      console.error('API config load failed:', err);
    });

  // ── OpenRouter call ──
  async function callOpenRouter(messages, modelIndex) {
    if (!apiConfig || !apiConfig.openrouter_key) {
      throw new Error('API key not loaded yet. Please wait a moment.');
    }
    const models = apiConfig.free_models || [];
    if (models.length === 0) throw new Error('No AI models available.');
    if (modelIndex >= models.length) throw new Error('All ' + models.length + ' models returned errors. Please try again later.');

    const model = models[modelIndex];
    console.log('Trying model', modelIndex + 1 + '/' + models.length + ':', model);
    
    const resp = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + apiConfig.openrouter_key,
        'HTTP-Referer': window.location.origin,
        'X-Title': 'Lessons IB Study Hub'
      },
      body: JSON.stringify({
        model: model,
        messages: messages,
        temperature: 0.7,
        max_tokens: 1024,
        stop: ["<unk>", "<|endoftext|>"]
      })
    });

    if (resp.status === 429) {
      console.log('Model', model, 'rate-limited, trying next...');
      await new Promise(r => setTimeout(r, 1500));
      return callOpenRouter(messages, modelIndex + 1);
    }
    if (!resp.ok) {
      const errText = await resp.text().catch(() => '');
      console.log('Model', model, 'failed (' + resp.status + '):', errText.substring(0, 100));
      return callOpenRouter(messages, modelIndex + 1);
    }

    const data = await resp.json();
    let reply = data.choices[0].message.content;
    // Clean garbled <unk> tokens
    reply = reply.replace(/<unk>+/gi, '').replace(/<\|endoftext\|>/gi, '');
    return { reply: reply, model: model };
  }

  // ── Toggle window ──
  toggleBtn.addEventListener('click', () => {
    windowEl.classList.toggle('hidden');
    if (!windowEl.classList.contains('hidden')) inputEl.focus();
  });
  closeBtn.addEventListener('click', () => windowEl.classList.add('hidden'));

  // ── Send message ──
  async function sendMessage() {
    const text = inputEl.value.trim();
    if (!text || isWaiting) return;

    // Wait for config if not loaded yet
    if (!configReady) {
      setStatus('Connecting to AI...');
      try { await configPromise; } catch(e) {}
      setStatus('');
    }
    if (!apiConfig || !apiConfig.openrouter_key) {
      addMessage('bot', '⚠️ AI is not connected. Please reload the page.');
      return;
    }

    addMessage('user', text);
    chatHistory.push({ role: 'user', content: text });
    inputEl.value = '';
    isWaiting = true;
    sendBtn.disabled = true;
    showTyping();
    setStatus('Thinking...');

    const systemPrompt = apiConfig.system_prompt || 'You are a helpful IB tutor.';
    const subjectCtx = getSubjectContext();
    const system = subjectCtx ? systemPrompt + '\n\n' + subjectCtx : systemPrompt;

    const messages = [{ role: 'system', content: system }];
    for (const msg of chatHistory.slice(0, -1)) {
      messages.push({
        role: msg.role === 'user' ? 'user' : 'assistant',
        content: msg.content
      });
    }
    messages.push({ role: 'user', content: text });

    try {
      const result = await callOpenRouter(messages, 0);
      removeTyping();
      addMessage('bot', result.reply);
      chatHistory.push({ role: 'model', content: result.reply });
      setStatus(result.model ? '🤖 ' + result.model.split('/').pop() : '');
    } catch (err) {
      removeTyping();
      addMessage('bot', '⚠️ ' + (err.message || 'AI models are busy. Please try again.'));
      setStatus('Error');
      console.error('Chat error:', err);
      chatHistory.pop();
    } finally {
      isWaiting = false;
      sendBtn.disabled = false;
      inputEl.focus();
    }
  }

  // ── Detect current subject from URL ──
  function getSubjectContext() {
    const path = window.location.pathname;
    const m = path.match(/\/subjects\/([a-z]+)/);
    if (!m) return '';
    const subject = m[1];
    const pageName = path.split('/').pop() || 'index';
    const subjectNames = {
      economics: 'Economics SL', chemistry: 'Chemistry HL',
      physics: 'Physics HL', math: 'Math AA HL',
      chinese: 'Chinese Lang Lit SL', english: 'English Lang Lit SL',
      sat: 'SAT Prep'
    };
    const subjName = subjectNames[subject] || subject;
    if (pageName === 'index' || pageName === 'index.html' || pageName === subject) {
      return 'The student is currently studying: ' + subjName + '. Tailor your answers to this subject.';
    }
    return 'The student is currently viewing: ' + subjName + ' — ' + pageName + '. Use this context to give more relevant answers.';
  }

  sendBtn.addEventListener('click', sendMessage);
  inputEl.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }
  });
  inputEl.addEventListener('input', () => {
    inputEl.style.height = 'auto';
    inputEl.style.height = Math.min(inputEl.scrollHeight, 100) + 'px';
  });

  // ── UI helpers ──
  function addMessage(role, text) {
    const div = document.createElement('div');
    div.className = 'message ' + role;
    const content = document.createElement('div');
    content.className = 'message-content';
    if (typeof marked !== 'undefined') {
      content.innerHTML = marked.parse(text);
    } else {
      content.innerHTML = '<p>' + escapeHtml(text) + '</p>';
    }
    div.appendChild(content);
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;
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

  function setStatus(msg) { statusEl.textContent = msg; }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Initial status
  setStatus('Connecting...');
  configPromise.then(() => {
    if (apiConfig && apiConfig.openrouter_key) setStatus('');
  });
})();