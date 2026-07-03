const API_URL = "/api/research";

const topicInput = document.getElementById("topic");
const dispatchBtn = document.getElementById("dispatchBtn");
const errorMsg = document.getElementById("errorMsg");
const stageList = document.getElementById("stageList");
const emptyState = document.getElementById("emptyState");
const findings = document.getElementById("findings");

const reportTopic = document.getElementById("reportTopic");
const reportBody = document.getElementById("reportBody");
const critiqueBody = document.getElementById("critiqueBody");
const searchBody = document.getElementById("searchBody");
const scrapeBody = document.getElementById("scrapeBody");

const STAGE_ORDER = ["search", "read", "write", "critique"];
// Rough pacing so the log feels alive even though the real work happens
// as one blocking call on the backend. The final stage waits on the
// actual response rather than a fixed timer.
const STAGE_PACE_MS = [1800, 2600, 2600];

const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

function setStage(name, status) {
  const el = stageList.querySelector(`[data-stage="${name}"]`);
  if (!el) return;
  el.classList.remove("is-active", "is-done");
  if (status) el.classList.add(status);
}

function resetStages() {
  STAGE_ORDER.forEach((name) => setStage(name, null));
}

async function animateStagesUntil(resultPromise) {
  for (let i = 0; i < STAGE_ORDER.length - 1; i++) {
    setStage(STAGE_ORDER[i], "is-active");
    await delay(STAGE_PACE_MS[i]);
    setStage(STAGE_ORDER[i], "is-done");
  }
  const lastStage = STAGE_ORDER[STAGE_ORDER.length - 1];
  setStage(lastStage, "is-active");
  // Wait for the real response (with a small floor so it doesn't flash).
  const [result] = await Promise.all([resultPromise, delay(900)]);
  setStage(lastStage, "is-done");
  return result;
}

function renderResults(data) {
  reportTopic.textContent = data.topic;
  reportBody.textContent = data.report;
  critiqueBody.textContent = data.feedback;
  searchBody.textContent = data.search_results;
  scrapeBody.textContent = data.scraped_content;

  emptyState.hidden = true;
  findings.hidden = false;
  findings.style.animation = "none";
  // restart the rise-in animation
  void findings.offsetWidth;
  findings.style.animation = "";
}

function setBusy(isBusy) {
  dispatchBtn.disabled = isBusy;
  dispatchBtn.querySelector(".btn-dispatch__label").textContent = isBusy
    ? "Agents working…"
    : "Dispatch Agents";
}

async function dispatch() {
  const topic = topicInput.value.trim();
  errorMsg.hidden = true;

  if (!topic) {
    errorMsg.textContent = "Give the desk a topic before dispatching the agents.";
    errorMsg.hidden = false;
    topicInput.focus();
    return;
  }

  setBusy(true);
  resetStages();
  findings.hidden = true;
  emptyState.hidden = true;

  const resultPromise = fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ topic }),
  }).then(async (res) => {
    if (!res.ok) {
      const body = await res.json().catch(() => ({}));
      throw new Error(body.detail || `Request failed with status ${res.status}`);
    }
    return res.json();
  });

  try {
    const data = await animateStagesUntil(resultPromise);
    renderResults(data);
  } catch (err) {
    resetStages();
    emptyState.hidden = false;
    errorMsg.textContent = `The desk hit a snag: ${err.message}`;
    errorMsg.hidden = false;
  } finally {
    setBusy(false);
  }
}

dispatchBtn.addEventListener("click", dispatch);

topicInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) {
    dispatch();
  }
});
