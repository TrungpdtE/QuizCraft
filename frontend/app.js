const API = "/api/exercises";

const state = {
  type: "",
  file: "",
  mode: "sequential",
  sessionId: "",
  question: null,
  total: 0,
  score: { correct: 0, incorrect: 0, skipped: 0 },
  locked: false,
};

const typeMeta = {
  word_forms: { name: "Word Form", description: "Từ gốc và các dạng từ liên quan" },
  word_types: { name: "Word Type", description: "Nhận diện loại từ trong câu" },
  multiple_choice: { name: "Multiple Choice", description: "Câu hỏi trắc nghiệm nhiều lựa chọn" },
};

const $ = (selector) => document.querySelector(selector);
const typeOptions = $("#type-options");
const fileSelect = $("#file-select");
const startButton = $("#start-btn");
const setupScreen = $("#setup-screen");
const exerciseScreen = $("#exercise-screen");
const completeScreen = $("#complete-screen");
const questionArea = $("#question-area");
const feedback = $("#feedback");

document.addEventListener("DOMContentLoaded", loadTypes);
fileSelect.addEventListener("change", () => {
  state.file = fileSelect.value;
  startButton.disabled = !state.file;
});
document.querySelectorAll('input[name="mode"]').forEach((input) => {
  input.addEventListener("change", () => {
    state.mode = document.querySelector('input[name="mode"]:checked').value;
  });
});
startButton.addEventListener("click", startExercise);
$("#submit-btn").addEventListener("click", submitAnswer);
$("#skip-btn").addEventListener("click", skipQuestion);
$("#answer-btn").addEventListener("click", showAnswer);
$("#next-btn").addEventListener("click", nextQuestion);
$("#back-btn").addEventListener("click", showSetup);
$("#restart-btn").addEventListener("click", showSetup);

async function loadTypes() {
  try {
    const types = await request(`${API}/types`);
    typeOptions.innerHTML = types
      .map((type) => {
        const meta = typeMeta[type.id] || { name: type.name, description: "" };
        return `
          <button class="type-card" data-type="${escapeHtml(type.id)}">
            <strong>${escapeHtml(meta.name)}</strong>
            <small>${escapeHtml(meta.description)}</small>
          </button>`;
      })
      .join("");
    document.querySelectorAll(".type-card").forEach((button) => {
      button.addEventListener("click", () => selectType(button.dataset.type));
    });
  } catch (error) {
    showError("setup", error.message);
  }
}

async function selectType(type) {
  state.type = type;
  state.file = "";
  document.querySelectorAll(".type-card").forEach((button) => {
    button.classList.toggle("active", button.dataset.type === type);
  });
  fileSelect.disabled = true;
  fileSelect.innerHTML = '<option value="">Đang tải...</option>';
  startButton.disabled = true;
  showError("setup", "");
  try {
    const data = await request(`${API}/files?type=${encodeURIComponent(type)}`);
    fileSelect.innerHTML =
      '<option value="">Chọn một file bài học</option>' +
      data.files.map((file) => `<option value="${escapeHtml(file)}">${escapeHtml(file)}</option>`).join("");
    fileSelect.disabled = false;
  } catch (error) {
    fileSelect.innerHTML = '<option value="">Không có dữ liệu</option>';
    showError("setup", error.message);
  }
}

async function startExercise() {
  showError("setup", "");
  startButton.disabled = true;
  try {
    const params = new URLSearchParams({ type: state.type, file: state.file, mode: state.mode });
    const data = await request(`${API}/start?${params}`);
    state.sessionId = data.session_id;
    state.question = data.question;
    state.total = data.total;
    state.score = data.score;
    setupScreen.classList.add("hidden");
    completeScreen.classList.add("hidden");
    exerciseScreen.classList.remove("hidden");
    renderQuestion();
  } catch (error) {
    showError("setup", error.message);
  } finally {
    startButton.disabled = !state.file;
  }
}

function renderQuestion() {
  state.locked = false;
  feedback.className = "feedback hidden";
  feedback.textContent = "";
  showError("exercise", "");
  setActionState(false);
  updateScore();

  const question = state.question;
  if (!question) {
    showComplete();
    return;
  }
  updateProgress(question.number, state.total);
  if (state.type === "word_forms") renderWordForm(question);
  if (state.type === "word_types") renderWordTypes(question);
  if (state.type === "multiple_choice") renderMultipleChoice(question);
}

function renderWordForm(question) {
  if (question.phase === "forms") {
    questionArea.innerHTML = `
      <p class="question-label">Bước 2 · Các dạng từ</p>
      <h2 class="question-title">${escapeHtml(question.english)}</h2>
      <div class="forms-grid">
        ${question.form_fields
          .map(
            (field) => `
            <div class="input-group">
              <label for="form-${field}">${escapeHtml(field)}</label>
              <input id="form-${field}" class="text-input form-input" data-field="${field}" autocomplete="off" />
            </div>`,
          )
          .join("")}
      </div>`;
    focusFirstInput();
    return;
  }
  questionArea.innerHTML = `
    <p class="word-prompt">${escapeHtml(question.prompt)}</p>
    <h2 class="vietnamese-word">${escapeHtml(question.vietnamese)}</h2>
    <input id="english-answer" class="text-input" placeholder="Nhập từ tiếng Anh..." autocomplete="off" />`;
  focusFirstInput();
}

function renderWordTypes(question) {
  questionArea.innerHTML = `
    <p class="question-label">Xác định loại từ</p>
    <h2 class="question-title">${escapeHtml(question.sentence)}</h2>
    <div class="token-list">
      ${question.tokens
        .map(
          (token, index) => `
          <label class="token">
            <span class="token-word">${escapeHtml(token.word)}</span>
            <input class="token-input" data-index="${index}" maxlength="5" aria-label="Loại từ của ${escapeHtml(token.word)}" />
          </label>`,
        )
        .join("")}
    </div>`;
  focusFirstInput();
}

function renderMultipleChoice(question) {
  const tags = question.tags?.length ? `<p class="question-label">${question.tags.map(escapeHtml).join(" · ")}</p>` : "";
  questionArea.innerHTML = `
    ${tags}
    <h2 class="question-title">${escapeHtml(question.question)}</h2>
    <div class="option-list">
      ${Object.entries(question.options)
        .map(
          ([letter, text]) => `
          <label class="option" data-option="${escapeHtml(letter)}">
            <input type="radio" name="choice" value="${escapeHtml(letter)}" />
            <span class="option-letter">${escapeHtml(letter)}</span>
            <span>${escapeHtml(text)}</span>
          </label>`,
        )
        .join("")}
    </div>`;
}

async function submitAnswer() {
  if (state.locked) return;
  const answer = collectAnswer();
  if (answer === null) {
    showError("exercise", "Vui lòng nhập hoặc chọn câu trả lời.");
    return;
  }
  showError("exercise", "");
  try {
    const result = await request(`${API}/submit`, {
      method: "POST",
      body: JSON.stringify({ session_id: state.sessionId, answer }),
    });
    state.score = result.score;
    updateScore();
    applyResults(result);

    if (state.type === "word_forms" && result.phase === "forms" && result.question && result.correct) {
      showFeedback(true, "Đúng từ gốc. Tiếp tục điền các dạng từ.");
      state.question = result.question;
      window.setTimeout(() => {
        renderWordForm(state.question);
        feedback.className = "feedback";
        feedback.textContent = "Đúng từ gốc. Tiếp tục điền các dạng từ.";
      }, 450);
      return;
    }
    state.locked = true;
    setActionState(true);
    showFeedback(result.correct, formatAnswer(result.correct_answer, result.correct));
  } catch (error) {
    showError("exercise", error.message);
  }
}

async function skipQuestion() {
  if (state.locked) return;
  try {
    const result = await request(`${API}/skip`, {
      method: "POST",
      body: JSON.stringify({ session_id: state.sessionId }),
    });
    state.score = result.score;
    state.locked = true;
    updateScore();
    setActionState(true);
    showFeedback(false, `Đã bỏ qua.\n${formatAnswer(result.answer, false)}`);
  } catch (error) {
    showError("exercise", error.message);
  }
}

async function showAnswer() {
  if (state.locked) return;
  try {
    const result = await request(`${API}/answer?session_id=${encodeURIComponent(state.sessionId)}`);
    state.locked = true;
    setActionState(true);
    markCorrectAnswer(result.answer);
    showFeedback(true, formatAnswer(result.answer, false));
  } catch (error) {
    showError("exercise", error.message);
  }
}

async function nextQuestion() {
  try {
    const data = await request(`${API}/next`, {
      method: "POST",
      body: JSON.stringify({ session_id: state.sessionId }),
    });
    state.question = data.question;
    state.score = data.score;
    if (data.completed) {
      showComplete();
    } else {
      renderQuestion();
    }
  } catch (error) {
    showError("exercise", error.message);
  }
}

function collectAnswer() {
  if (state.type === "word_forms") {
    if (state.question.phase === "forms") {
      const values = {};
      document.querySelectorAll(".form-input").forEach((input) => {
        values[input.dataset.field] = input.value;
      });
      return Object.values(values).some((value) => value.trim()) ? values : null;
    }
    const value = $("#english-answer")?.value.trim();
    return value ? { english: value } : null;
  }
  if (state.type === "word_types") {
    const values = [...document.querySelectorAll(".token-input")].map((input) => input.value.trim());
    return values.some(Boolean) ? values : null;
  }
  const selected = document.querySelector('input[name="choice"]:checked');
  return selected ? { option: selected.value } : null;
}

function applyResults(result) {
  if (state.type === "word_forms") {
    Object.entries(result.field_results || {}).forEach(([field, correct]) => {
      const input = field === "english" ? $("#english-answer") : $(`[data-field="${field}"]`);
      input?.classList.add(correct ? "is-correct" : "is-wrong");
    });
  }
  if (state.type === "word_types") {
    Object.entries(result.field_results || {}).forEach(([index, correct]) => {
      $(`.token-input[data-index="${index}"]`)?.classList.add(correct ? "is-correct" : "is-wrong");
    });
  }
  if (state.type === "multiple_choice") {
    const selected = document.querySelector('input[name="choice"]:checked')?.value;
    if (selected) $(`.option[data-option="${selected}"]`)?.classList.add(result.correct ? "is-correct" : "is-wrong");
    markCorrectAnswer(result.correct_answer);
  }
}

function markCorrectAnswer(answer) {
  if (state.type === "multiple_choice" && answer?.option) {
    $(`.option[data-option="${answer.option}"]`)?.classList.add("is-correct");
  }
}

function formatAnswer(answer, wasCorrect) {
  const prefix = wasCorrect ? "Chính xác." : "Đáp án đúng:";
  if (state.type === "word_forms") {
    if (typeof answer === "string") return `${prefix} ${answer}`;
    const lines = [`${prefix} ${answer.english || ""}`];
    Object.entries(answer.forms || answer)
      .filter(([key]) => key !== "english")
      .forEach(([key, value]) => lines.push(`${capitalize(key)}: ${value}`));
    return lines.join("\n");
  }
  if (state.type === "word_types") {
    return `${prefix}\n${state.question.tokens.map((token, index) => `${token.word}: ${answer[index]}`).join(" · ")}`;
  }
  return `${prefix} ${answer.option}. ${answer.text}`;
}

function setActionState(done) {
  $("#submit-btn").classList.toggle("hidden", done);
  $("#skip-btn").classList.toggle("hidden", done);
  $("#answer-btn").classList.toggle("hidden", done);
  $("#next-btn").classList.toggle("hidden", !done);
  questionArea.querySelectorAll("input").forEach((input) => {
    input.disabled = done;
  });
}

function showFeedback(correct, message) {
  feedback.textContent = message;
  feedback.className = `feedback${correct ? "" : " wrong"}`;
}

function updateScore() {
  $("#score-correct").textContent = state.score.correct;
  $("#score-incorrect").textContent = state.score.incorrect;
  $("#score-skipped").textContent = state.score.skipped;
}

function updateProgress(current, total) {
  $("#progress-current").textContent = current;
  $("#progress-total").textContent = total;
  $("#progress-bar").style.width = `${total ? (current / total) * 100 : 0}%`;
}

function showComplete() {
  exerciseScreen.classList.add("hidden");
  completeScreen.classList.remove("hidden");
  $("#final-score").textContent =
    `${state.score.correct} đúng · ${state.score.incorrect} sai · ${state.score.skipped} bỏ qua`;
}

function showSetup() {
  state.sessionId = "";
  state.question = null;
  exerciseScreen.classList.add("hidden");
  completeScreen.classList.add("hidden");
  setupScreen.classList.remove("hidden");
}

function showError(screen, message) {
  $(`#${screen}-error`).textContent = message;
}

function focusFirstInput() {
  window.setTimeout(() => questionArea.querySelector("input")?.focus(), 0);
}

async function request(url, options = {}) {
  const response = await fetch(url, {
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options,
  });
  const data = await response.json().catch(() => ({}));
  if (!response.ok) throw new Error(data.detail || "Không thể kết nối đến máy chủ.");
  return data;
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function capitalize(value) {
  return value.charAt(0).toUpperCase() + value.slice(1);
}
