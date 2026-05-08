/* ── State ──────────────────────────────────── */
let currentProblem    = null;
let selectedChoice    = null;
let currentDifficulty = 'All';
let currentSource     = 'bank';
let selectedTopics    = new Set();
let _bankItems        = [];

/* ── DOM refs ───────────────────────────────── */
const sqlEditor          = document.getElementById('sqlEditor');
const choicesList        = document.getElementById('choicesList');
const choicesToggle      = document.getElementById('choicesToggle');
const choicesBody        = document.getElementById('choicesBody');
const submitBtn          = document.getElementById('submitBtn');
const tryAgainBtn        = document.getElementById('tryAgainBtn');
const newProblemBtn      = document.getElementById('newProblemBtn');
const hintToggle         = document.getElementById('hintToggle');
const hintBox            = document.getElementById('hintBox');
const resultsPanel       = document.getElementById('resultsPanel');
const loadingOverlay     = document.getElementById('loadingOverlay');
const loadingMsg         = document.getElementById('loadingMsg');
const questionListSelect = document.getElementById('questionListSelect');
const btnAllRandom       = document.getElementById('btnAllRandom');
const topicPickerBtn     = document.getElementById('topicPickerBtn');
const topicPanel         = document.getElementById('topicPanel');
const topicList          = document.getElementById('topicList');
const topicCount         = document.getElementById('topicCount');

/* ── Source toggle ───────────────────────────── */
document.querySelectorAll('.btn-source').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.btn-source').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentSource = btn.dataset.source;
    btnAllRandom.textContent = currentSource === 'bank' ? 'All' : 'Random';
    questionListSelect.classList.toggle('hidden', currentSource !== 'bank');
    if (currentSource === 'bank') {
      filterBankList();
    } else {
      topicCount.classList.add('hidden');
    }
  });
});

/* ── Difficulty buttons ──────────────────────── */
document.querySelectorAll('.btn-diff').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.btn-diff').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentDifficulty = btn.dataset.diff;
    if (currentSource === 'bank') {
      filterBankList();      // also calls updateTopicCount when needed
    }
  });
});

/* ── Init ────────────────────────────────────── */
(async function init() {
  await populateBankList();
  await loadProblem();
})();

/* ── Populate question list dropdown ─────────── */
async function populateBankList() {
  const result = await safeFetch('/api/bank_list');
  if (!result.ok) return;
  _bankItems = result.data;
  const diffLabel = { Easy: 'E', Medium: 'M', Hard: 'H' };
  result.data.forEach(item => {
    const opt = document.createElement('option');
    opt.value = item.index;
    opt.dataset.difficulty = item.difficulty;
    opt.dataset.category   = item.category;
    opt.textContent = `#${item.index + 1} [${diffLabel[item.difficulty] || item.difficulty}] ${item.title}`;
    questionListSelect.appendChild(opt);
  });
  buildTopicCheckboxes();
}

/* ── Filter bank dropdown by difficulty + topic ─ */
function filterBankList() {
  Array.from(questionListSelect.options).forEach(opt => {
    if (!opt.value) return;
    const diffOk  = currentDifficulty === 'All' || opt.dataset.difficulty === currentDifficulty;
    const topicOk = selectedTopics.size === 0 || selectedTopics.has(opt.dataset.category);
    opt.hidden = !diffOk || !topicOk;
  });
  const sel = questionListSelect.selectedOptions[0];
  if (sel && sel.hidden) questionListSelect.value = '';
  updateTopicCount();
}

questionListSelect.addEventListener('change', () => {
  const val = questionListSelect.value;
  if (val !== '') loadProblem(parseInt(val, 10));
});

/* ── Topic checkboxes ────────────────────────── */
function buildTopicCheckboxes() {
  const topics = [...new Set(_bankItems.map(i => i.category))].sort();
  topicList.innerHTML = '';
  topics.forEach(topic => {
    const label = document.createElement('label');
    label.className = 'topic-checkbox-label';
    const cb = document.createElement('input');
    cb.type = 'checkbox';
    cb.value = topic;
    cb.addEventListener('change', () => {
      if (cb.checked) selectedTopics.add(topic);
      else            selectedTopics.delete(topic);
      updateTopicUI();
    });
    label.appendChild(cb);
    label.appendChild(document.createTextNode(' ' + topic));
    topicList.appendChild(label);
  });
}

function updateTopicUI() {
  const n = selectedTopics.size;
  topicPickerBtn.textContent = n === 0 ? '☰ Select Topic' : `☰ Topics (${n})`;
  topicPickerBtn.classList.toggle('has-topics', n > 0);
  if (currentSource === 'bank') filterBankList();
}

function updateTopicCount() {
  if (selectedTopics.size === 0 || currentSource !== 'bank') {
    topicCount.classList.add('hidden');
    return;
  }
  const n = _bankItems.filter(item => {
    const diffOk  = currentDifficulty === 'All' || item.difficulty === currentDifficulty;
    const topicOk = selectedTopics.has(item.category);
    return diffOk && topicOk;
  }).length;
  topicCount.textContent = `${n} question${n !== 1 ? 's' : ''} match`;
  topicCount.classList.remove('hidden');
}

/* ── Topic panel open / close ────────────────── */
topicPickerBtn.addEventListener('click', e => {
  e.stopPropagation();
  topicPanel.classList.toggle('hidden');
});

document.addEventListener('click', e => {
  if (!topicPickerBtn.contains(e.target) && !topicPanel.contains(e.target)) {
    topicPanel.classList.add('hidden');
  }
});

/* ── Loading helpers ─────────────────────────── */
function showLoading(msg = 'Generating question…') {
  loadingMsg.textContent = msg;
  loadingOverlay.classList.remove('hidden');
}

function hideLoading() {
  loadingOverlay.classList.add('hidden');
}

/* ── Safe JSON fetch ─────────────────────────── *
 * Always parses the response body safely.
 * Returns { ok: true, data } or { ok: false, error }.
 */
async function safeFetch(url, options) {
  let res;
  try {
    res = await fetch(url, options);
  } catch (networkErr) {
    return { ok: false, error: 'Network error — is the Flask server running? ' + networkErr.message };
  }

  let text;
  try {
    text = await res.text();
  } catch (e) {
    return { ok: false, error: 'Failed to read server response.' };
  }

  // Detect an HTML error page (Werkzeug debug page, proxy error, etc.)
  if (text.trimStart().startsWith('<')) {
    return {
      ok: false,
      error: `Server returned an HTML error page (HTTP ${res.status}). Check the Flask console for the traceback.`,
    };
  }

  let data;
  try {
    data = JSON.parse(text);
  } catch (e) {
    return { ok: false, error: `Server response is not valid JSON (HTTP ${res.status}): ${text.slice(0, 200)}` };
  }

  if (!res.ok || data.error) {
    return { ok: false, error: data.error || `HTTP ${res.status}` };
  }

  return { ok: true, data };
}

/* ── Load a problem ──────────────────────────── */
async function loadProblem(bankIndex = null) {
  const isBank = currentSource === 'bank';
  const isAll  = currentDifficulty === 'All';

  const diffDisplay = isAll ? 'random' : currentDifficulty;
  const msg = isBank
    ? `Loading ${isAll ? '' : currentDifficulty + ' '}question from bank…`
    : `Generating ${diffDisplay} question with Ollama… (20–60 s)`;
  showLoading(msg);
  submitBtn.disabled = true;

  const topicsParam = selectedTopics.size > 0
    ? `&topics=${encodeURIComponent([...selectedTopics].join(','))}`
    : '';

  let url;
  if (isBank) {
    url = bankIndex !== null
      ? `/api/bank_problem?index=${bankIndex}`
      : `/api/bank_problem?difficulty=${currentDifficulty}${topicsParam}`;
  } else {
    const aiDiff = isAll
      ? ['Easy', 'Medium', 'Hard'][Math.floor(Math.random() * 3)]
      : currentDifficulty;
    url = `/api/problem?difficulty=${aiDiff}${topicsParam}`;
  }

  const result = await safeFetch(url);

  hideLoading();

  if (!result.ok) {
    const isOllama = !isBank && (
      result.error.toLowerCase().includes('ollama') ||
      result.error.toLowerCase().includes('connect') ||
      result.error.toLowerCase().includes('generation failed')
    );
    const msg = isOllama
      ? `Ollama error — make sure Ollama is running and the model is pulled.\n\nDetails: ${result.error}`
      : `Failed to load question:\n\n${result.error}`;
    alert(msg);
    submitBtn.disabled = false;
    return;
  }

  const data = result.data;
  currentProblem = data;
  selectedChoice = null;

  // Meta
  document.getElementById('problemTitle').textContent     = data.title;
  document.getElementById('difficultyBadge').textContent  = data.difficulty;
  document.getElementById('difficultyBadge').className    = `badge ${data.difficulty}`;
  document.getElementById('categoryBadge').textContent    = data.category;

  document.getElementById('descriptionText').textContent  = data.description;
  document.getElementById('questionText').textContent     = data.question;

  // Hint
  hintBox.textContent = data.hint || 'No hint available.';
  hintBox.classList.add('hidden');
  hintToggle.textContent = 'Show Hint';

  // Tables
  renderTables(data.tables);

  // Choices
  renderChoices(data.choices);

  // Editor – clear
  sqlEditor.value = '';

  // Collapse choices on new problem
  choicesToggle.classList.remove('open');
  choicesBody.classList.add('hidden');

  // Results – hide
  hideResults();
  tryAgainBtn.classList.add('hidden');
  submitBtn.disabled = false;
  submitBtn.textContent = 'Submit Answer';
}

/* ── Table preview ───────────────────────────── */
function renderTables(tables) {
  const container = document.getElementById('tablesPreviews');
  container.innerHTML = '';
  tables.forEach(t => {
    const colNames = t.columns.map(c => c.name);
    const rows     = (t.data || []).slice(0, 8);
    const more     = (t.data || []).length - rows.length;

    const headerRow = colNames.map(c => `<th>${esc(c)}</th>`).join('');
    const bodyRows  = rows.map(row =>
      `<tr>${colNames.map(c => `<td>${esc(row[c] ?? 'NULL')}</td>`).join('')}</tr>`
    ).join('');

    container.innerHTML += `
      <div class="table-block">
        <div class="table-name">${esc(t.name)}</div>
        <div class="data-table-wrap">
          <table class="data-table">
            <thead><tr>${headerRow}</tr></thead>
            <tbody>${bodyRows}</tbody>
          </table>
        </div>
        ${more > 0 ? `<div class="row-more">… ${more} more row${more > 1 ? 's' : ''}</div>` : ''}
      </div>`;
  });
}

/* ── Multiple choice ─────────────────────────── */
function renderChoices(choices) {
  choicesList.innerHTML = '';
  choices.forEach(c => {
    const div = document.createElement('div');
    div.className = 'choice-item';
    div.dataset.id = c.id;
    const preview = c.text.replace(/\s+/g, ' ').slice(0, 60) + '…';
    div.innerHTML = `
      <div class="choice-header">
        <span class="choice-id">${esc(c.id)}</span>
        <span class="choice-preview">${esc(preview)}</span>
      </div>
      <pre class="choice-code">${esc(c.text)}</pre>`;
    div.addEventListener('click', () => toggleChoice(div, c.id));
    choicesList.appendChild(div);
  });
}

function toggleChoice(div, id) {
  const wasExpanded = div.classList.contains('expanded');
  document.querySelectorAll('.choice-item').forEach(el => {
    el.classList.remove('expanded', 'selected');
  });
  if (!wasExpanded) div.classList.add('expanded');

  if (selectedChoice === id) {
    selectedChoice = null;
  } else {
    selectedChoice = id;
    div.classList.add('selected');
  }
}

/* ── Submit ──────────────────────────────────── */
submitBtn.addEventListener('click', submitAnswer);

sqlEditor.addEventListener('keydown', e => {
  if (e.key === 'Tab') {
    e.preventDefault();
    const s = sqlEditor.selectionStart;
    const v = sqlEditor.value;
    sqlEditor.value = v.slice(0, s) + '    ' + v.slice(s);
    sqlEditor.selectionStart = sqlEditor.selectionEnd = s + 4;
  }
  if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) submitAnswer();
});

async function submitAnswer() {
  if (!currentProblem) return;
  const query = sqlEditor.value.trim();
  if (!query && !selectedChoice) {
    alert('Write a SQL query and/or select a multiple-choice answer before submitting.');
    return;
  }

  submitBtn.disabled = true;
  submitBtn.textContent = 'Grading…';

  const result = await safeFetch('/api/submit', {
    method:  'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      problem_id: currentProblem.id,
      query:      query,
      choice:     selectedChoice,
    }),
  });

  submitBtn.disabled = false;
  submitBtn.textContent = 'Submit Answer';

  if (!result.ok) {
    alert('Submit error: ' + result.error);
    return;
  }

  renderResults(result.data, query);
  tryAgainBtn.classList.remove('hidden');
}

/* ── Results ─────────────────────────────────── */
function renderResults(data, userQuery) {
  resultsPanel.style.display = 'flex';

  const bannerEl = document.getElementById('resultBanner');
  const graded   = data.query_graded;

  if (!userQuery) {
    bannerEl.className   = 'result-banner';
    bannerEl.textContent = 'No SQL submitted — see choice analysis below.';
  } else if (graded && graded.error) {
    bannerEl.className   = 'result-banner error';
    bannerEl.textContent = '⚠ SQL Error: ' + graded.error;
  } else if (graded && graded.is_correct) {
    bannerEl.className   = 'result-banner correct';
    bannerEl.textContent = '✓ Correct! Your query produces the expected result.';
  } else if (graded) {
    bannerEl.className   = 'result-banner incorrect';
    bannerEl.textContent = '✗ Incorrect — your output does not match the expected result.';
  } else {
    bannerEl.className   = 'result-banner';
    bannerEl.textContent = '';
  }

  const choiceBanner = document.getElementById('choiceBanner');
  if (data.choice_selected) {
    choiceBanner.className   = data.choice_correct ? 'result-banner correct' : 'result-banner incorrect';
    choiceBanner.textContent = data.choice_correct
      ? `✓ Choice ${data.choice_selected} is correct!`
      : `✗ Choice ${data.choice_selected} is incorrect.`;
    choiceBanner.style.display = 'block';
  } else {
    choiceBanner.style.display = 'none';
  }

  const userBlock = document.getElementById('userOutputBlock');
  const expBlock  = document.getElementById('expectedOutputBlock');

  if (!userQuery || !graded) {
    userBlock.innerHTML = '<p class="no-query-msg">No SQL query submitted.</p>';
  } else if (graded.error) {
    userBlock.innerHTML = `<p class="no-query-msg" style="color:var(--red)">${esc(graded.error)}</p>`;
  } else {
    document.getElementById('userRowCount').textContent = graded.user_row_count;
    userBlock.innerHTML = buildTable(graded.user_columns, graded.user_data);
  }

  document.getElementById('expectedRowCount').textContent =
    currentProblem.expected_rows ? currentProblem.expected_rows.length : '?';
  expBlock.innerHTML = buildTable(
    currentProblem.expected_columns,
    currentProblem.expected_rows
  );

  document.getElementById('explanationBody').innerHTML =
    markdownLite(data.explanation || '');

  renderChoiceAnalysis(data.choices_graded, data.choice_selected);

  resultsPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function buildTable(columns, rows) {
  if (!columns || columns.length === 0) return '<p class="no-query-msg">No data</p>';
  const head = columns.map(c => `<th>${esc(c)}</th>`).join('');
  const body = (rows || []).map(row =>
    `<tr>${columns.map(c => {
      const v = row[c];
      return v === null || v === undefined
        ? `<td class="null-val">NULL</td>`
        : `<td>${esc(String(v))}</td>`;
    }).join('')}</tr>`
  ).join('');
  return `<div class="output-table-wrap">
    <table class="output-table">
      <thead><tr>${head}</tr></thead>
      <tbody>${body}</tbody>
    </table>
  </div>`;
}

function renderChoiceAnalysis(choices, userSelected) {
  const container = document.getElementById('choiceAnalysis');
  container.innerHTML = '';
  choices.forEach(c => {
    const isCorrect  = c.correct;
    const isSelected = c.id === userSelected;
    const div = document.createElement('div');
    div.className = `choice-result ${isCorrect ? 'correct-choice' : 'incorrect-choice'} ${isSelected ? 'user-selected' : ''}`;
    div.innerHTML = `
      <div class="choice-result-header">
        <span class="choice-result-id">${esc(c.id)}</span>
        <span>${isCorrect ? '<span class="tick">✓</span>' : '<span class="cross">✗</span>'}</span>
        ${isSelected ? '<span class="user-tag">YOUR PICK</span>' : ''}
        <span class="choice-result-expl">${esc(c.explanation)}</span>
      </div>
      <pre class="choice-result-code">${esc(c.text)}</pre>`;
    container.appendChild(div);
  });
}

/* ── Try Again / New Problem ─────────────────── */
tryAgainBtn.addEventListener('click', () => {
  hideResults();
  sqlEditor.value = '';
  selectedChoice  = null;
  document.querySelectorAll('.choice-item').forEach(el =>
    el.classList.remove('selected', 'expanded')
  );
});

newProblemBtn.addEventListener('click', () => {
  questionListSelect.value = '';
  loadProblem();
});

hintToggle.addEventListener('click', () => {
  const hidden = hintBox.classList.toggle('hidden');
  hintToggle.textContent = hidden ? 'Show Hint' : 'Hide Hint';
});

choicesToggle.addEventListener('click', () => {
  choicesToggle.classList.toggle('open');
  choicesBody.classList.toggle('hidden');
});

function hideResults() {
  resultsPanel.style.display = 'none';
}

/* ── Helpers ─────────────────────────────────── */
function esc(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function markdownLite(text) {
  text = text.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  text = text.replace(/`([^`]+)`/g, '<code style="background:var(--surface2);padding:1px 4px;border-radius:3px;font-family:monospace;font-size:0.85em">$1</code>');
  text = text.replace(/\n/g, '<br>');
  return text;
}
