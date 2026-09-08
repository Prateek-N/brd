// ── HELPERS ───────────────────────────────────────────────────────────────────
function esc(v) {
  return String(v ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
}

// ── RENDER ROLES ──────────────────────────────────────────────────────────────
function renderRoles() {
  const grid = document.getElementById("rolesGrid");
  const sorted = [...BATCH_PEOPLE].sort((a, b) => a.name.localeCompare(b.name));
  grid.innerHTML = sorted.map(p => {
    const preview = (p.responsibilities || []).slice(0, 4).map(r => `<li>${esc(r)}</li>`).join("");
    const moreCount = (p.responsibilities || []).length - 4;
    return `
      <article class="role-card">
        <div class="role-head">
          <div class="role-main">
            <h3 class="role-name">${esc(p.name)}</h3>
            <p class="role-title">${esc(p.jobTitle)}</p>
          </div>
          <div class="role-side">
            <div class="badge"><span class="dot"></span>${esc(p.company)}</div>
            <a class="btn btn-outline role-link" href="profiles/${esc(p.slug)}.html">Open Profile</a>
          </div>
        </div>
        <details class="role-details">
          <summary class="role-summary">View responsibilities (showing 4 of ${(p.responsibilities||[]).length})</summary>
          <ul class="list">${preview}${moreCount > 0 ? `<li class="muted">&hellip; and ${moreCount} more on the profile page</li>` : ""}</ul>
        </details>
        <div style="margin-top:14px;padding-top:14px;border-top:1px solid var(--hairline)">
          <p class="modal-k" style="margin:0 0 4px">Project</p>
          <p style="margin:0;font-size:14px;color:var(--ink);font-weight:500">${esc(p.project)}</p>
          <p style="margin:6px 0 0;font-size:12px;color:var(--muted)">${esc((p.projectDesc||"").slice(0,130))}&hellip;</p>
        </div>
      </article>
    `;
  }).join("");
}

// ── RENDER WEEKS ─────────────────────────────────────────────────────────────
function renderWeeks() {
  const grid = document.getElementById("weekGrid");
  grid.innerHTML = BATCH_WEEK_DATES.map(w => {
    const phase = w.week <= 3 ? "Setup & Foundation" : w.week <= 6 ? "Build & Develop" : w.week <= 9 ? "Iterate & Improve" : "Refine & Deliver";
    return `
      <div class="week-card">
        <button class="week-btn" type="button" data-aug-week="${w.week}" aria-haspopup="dialog" aria-controls="weekDialog">
          <div class="week-num">Week ${w.week}</div>
          <div class="week-tag">Bridgepoint &middot; Aug 2026 Batch</div>
          <div class="week-sub">${esc(w.dateRange)}</div>
          <div class="week-project">${esc(phase)}</div>
        </button>
      </div>
    `;
  }).join("");
}

// ── MODAL CONTENT ─────────────────────────────────────────────────────────────
function buildModalContent(weekNum) {
  const weekInfo = BATCH_WEEK_DATES.find(w => w.week === weekNum);
  const peopleCards = BATCH_PEOPLE.map(p => {
    const task = (p.weekTasks || [])[weekNum - 1] || "No task defined for this week.";
    return `
      <section class="modal-card">
        <div class="modal-card-head">
          <div>
            <h3 class="modal-card-title">${esc(p.name)}</h3>
            <p class="modal-card-sub">${esc(p.jobTitle)} &middot; ${esc(p.company)}</p>
          </div>
          <a class="btn btn-outline modal-card-link" href="profiles/${esc(p.slug)}.html">Profile</a>
        </div>
        <p class="modal-k" style="margin:0 0 4px">Project</p>
        <p class="modal-p" style="margin:0 0 12px;font-weight:500;color:var(--ink)">${esc(p.project)}</p>
        <p class="modal-k" style="margin:0 0 6px">Week ${weekNum} Task</p>
        <ul class="modal-list"><li>${esc(task)}</li></ul>
      </section>
    `;
  }).join("");

  return `
    <section class="modal-section">
      <p class="section-label">Cohort</p>
      <h3 class="modal-h3">Bridgepoint Careers LLC &mdash; Aug 2026 Batch</h3>
      <p class="modal-p">Individual 12-week project plans &middot; Starting Aug 10, 2026</p>
      <div class="modal-split">
        <div><p class="modal-k">Date Range</p><p class="modal-p">${esc(weekInfo ? weekInfo.dateRange : "")}</p></div>
        <div><p class="modal-k">Team Members</p><p class="modal-p">${BATCH_PEOPLE.length} members &middot; individual projects</p></div>
      </div>
    </section>
    <section class="modal-section">
      <p class="section-label">Individual Tasks &mdash; Week ${weekNum}</p>
      ${peopleCards}
    </section>
  `;
}

// ── EMAIL TEXT ─────────────────────────────────────────────────────────────────
function buildEmailText(weekNum) {
  const weekInfo = BATCH_WEEK_DATES.find(w => w.week === weekNum);
  const lines = [];
  lines.push(`Subject: Week ${weekNum} Tasks \u2014 Bridgepoint Careers LLC Aug 2026 Batch (${weekInfo ? weekInfo.dateRange : ""})`);
  lines.push("");
  lines.push(`Week ${weekNum}: ${weekInfo ? weekInfo.dateRange : ""}`);
  lines.push("Cohort: Bridgepoint Careers LLC \u2014 Aug 2026 Batch");
  lines.push("");
  lines.push("Individual Assignments (by team member):");
  BATCH_PEOPLE.forEach(p => {
    lines.push("");
    lines.push(`${p.name} \u2014 ${p.jobTitle}`);
    lines.push(`Project: ${p.project}`);
    lines.push(`Week ${weekNum} Task: ${(p.weekTasks || [])[weekNum - 1] || "No task defined."}`);
    lines.push(`Tools: ${p.tools}`);
  });
  lines.push("");
  lines.push("Standard Weekly Deliverables (all members):");
  lines.push("- A short weekly update (5\u201310 lines): what you completed, what you discovered, what you will do next");
  lines.push("- Work artifacts: links/files (repo, notebook, screenshots) and any data sources used");
  lines.push("- Risks/blockers: what is blocked and what support you need");
  lines.push("");
  lines.push("Signature:");
  lines.push("- Rajeev Gupta");
  lines.push("- Project Lead");
  lines.push("- rajeev.gupta@bridgepointcareers.com");
  return lines.join("\n");
}

// ── EMAIL HTML ─────────────────────────────────────────────────────────────────
function buildEmailHtml(weekNum) {
  const weekInfo = BATCH_WEEK_DATES.find(w => w.week === weekNum);
  const subject = `Week ${weekNum} Tasks \u2014 Bridgepoint Careers LLC Aug 2026 Batch (${weekInfo ? weekInfo.dateRange : ""})`;
  const signature = { name: "Rajeev Gupta", title: "Project Lead", email: "rajeev.gupta@bridgepointcareers.com" };

  function bullet(items) {
    if (!items || !items.length) return "";
    const rows = items.map(item => `<tr><td width="18" valign="top" style="padding:2px 0;color:#05ba46;font-weight:800;">&bull;</td><td valign="top" style="padding:2px 0;color:#334155;font-size:14px;">${esc(item)}</td></tr>`).join("");
    return `<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-top:8px;">${rows}</table>`;
  }

  const personRows = BATCH_PEOPLE.map(p => {
    const task = (p.weekTasks || [])[weekNum - 1] || "No task defined.";
    return `<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="border:1px solid #d1d5db;margin-top:10px;"><tr><td width="6" style="background:#046bd2;font-size:0;line-height:0;">&nbsp;</td><td style="padding:12px 14px;"><div style="font-size:15px;font-weight:800;color:#111111;">${esc(p.name)}</div><div style="font-size:13px;color:#64748b;margin-top:2px;">${esc(p.jobTitle)}</div><div style="font-size:13px;color:#046bd2;margin-top:4px;font-weight:600;">${esc(p.project)}</div>${bullet([`Week ${weekNum} Task: ${task}`])}<div style="font-size:12px;color:#94a3b8;margin-top:8px;">Tools: ${esc(p.tools)}</div></td></tr></table>`;
  }).join("");

  const deliverableRows = bullet([
    "A short weekly update (5\u201310 lines): what you completed, what you discovered, what you will do next",
    "Work artifacts: links/files (repo, notebook, screenshots) and any data sources used",
    "Risks/blockers: what is blocked and what support you need"
  ]);

  const signatureBlock = `<div style="margin-top:18px;"><div style="font-size:13px;color:#64748b;margin:0 0 8px;">Regards,</div><div style="font-size:14px;font-weight:800;color:#111111;">${esc(signature.name)}</div><div style="font-size:13px;color:#64748b;margin-top:2px;">${esc(signature.title)}</div><div style="margin-top:6px;"><a href="mailto:${esc(signature.email)}" style="color:#046bd2;text-decoration:underline;font-size:13px;">${esc(signature.email)}</a></div></div>`;

  return `<div style="font-family:Segoe UI,Arial,sans-serif;line-height:1.45;color:#111111;"><table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#f0f5fa;padding:18px;"><tr><td align="left"><table role="presentation" align="left" cellpadding="0" cellspacing="0" border="0" width="640" style="max-width:640px;width:100%;margin:0;background:#ffffff;border:1px solid #d1d5db;"><tr><td style="background:#046bd2;color:#ffffff;padding:18px 18px 16px;"><div style="font-size:12px;letter-spacing:1px;text-transform:uppercase;opacity:.92;">Bridgepoint Careers LLC &mdash; Aug 2026 Batch</div><div style="font-size:22px;font-weight:800;margin-top:6px;">${esc(subject)}</div><div style="font-size:13px;opacity:.92;margin-top:8px;">${esc(weekInfo ? weekInfo.dateRange : "")} &middot; Individual Project Plans</div></td></tr><tr><td style="padding:18px;"><div style="font-size:12px;letter-spacing:1px;text-transform:uppercase;color:#046bd2;font-weight:800;">Individual Assignments &mdash; Week ${weekNum}</div>${personRows}<div style="margin-top:14px;"><div style="font-size:12px;letter-spacing:1px;text-transform:uppercase;color:#046bd2;font-weight:800;margin-bottom:4px;">Standard Weekly Deliverables (All Members)</div>${deliverableRows}</div>${signatureBlock}</td></tr></table></td></tr></table></div>`;
}

// ── CLIPBOARD ─────────────────────────────────────────────────────────────────
async function copyRich({ text, html }) {
  const plain = String(text || "");
  const rich = String(html || "");
  if (navigator.clipboard && typeof navigator.clipboard.write === "function" && window.ClipboardItem && rich) {
    const item = new ClipboardItem({
      "text/plain": new Blob([plain], { type: "text/plain" }),
      "text/html": new Blob([rich], { type: "text/html" })
    });
    await navigator.clipboard.write([item]);
    return;
  }
  if (navigator.clipboard && typeof navigator.clipboard.writeText === "function") {
    await navigator.clipboard.writeText(plain);
    return;
  }
  const ta = document.createElement("textarea");
  ta.value = plain;
  ta.setAttribute("readonly", "");
  ta.style.cssText = "position:fixed;top:0;left:0;width:1px;height:1px;opacity:0";
  document.body.appendChild(ta);
  ta.focus(); ta.select();
  const ok = document.execCommand("copy");
  document.body.removeChild(ta);
  if (!ok) throw new Error("Copy failed");
}

// ── MODAL STATE ───────────────────────────────────────────────────────────────
const dialog = document.getElementById("weekDialog");
const modalBody = document.getElementById("modalBody");
const weekTitle = document.getElementById("weekTitle");
const weekMeta = document.getElementById("weekMeta");
const modalStatus = document.getElementById("modalStatus");
const copyBtn = document.getElementById("copyBtn");
const closeBtn = document.getElementById("closeBtn");
let activeWeekNum = null;
let closeTimer = null;

function openWeek(weekNum) {
  activeWeekNum = weekNum;
  const weekInfo = BATCH_WEEK_DATES.find(w => w.week === weekNum);
  if (!weekInfo) return;
  modalStatus.textContent = "";
  weekMeta.textContent = `Bridgepoint Careers LLC \u00b7 ${weekInfo.dateRange}`;
  weekTitle.textContent = `Week ${weekNum} Tasks`;
  modalBody.innerHTML = buildModalContent(weekNum);
  if (typeof dialog.showModal === "function") {
    if (!dialog.open) dialog.showModal();
    dialog.classList.remove("is-closing");
    dialog.classList.add("is-open");
    closeBtn.focus();
  } else {
    modalStatus.textContent = "Your browser does not support modals. Please use a modern browser.";
  }
}

function closeWeek() {
  if (!dialog.open) return;
  dialog.classList.add("is-closing");
  dialog.classList.remove("is-open");
  if (closeTimer) window.clearTimeout(closeTimer);
  closeTimer = window.setTimeout(() => {
    dialog.close();
    dialog.classList.remove("is-closing");
  }, 160);
}

document.getElementById("weekGrid").addEventListener("click", (e) => {
  const btn = e.target.closest("[data-aug-week]");
  if (!btn) return;
  openWeek(Number(btn.getAttribute("data-aug-week")));
});

closeBtn.addEventListener("click", closeWeek);
dialog.addEventListener("cancel", (e) => { e.preventDefault(); closeWeek(); });
dialog.addEventListener("click", (e) => {
  const rect = dialog.getBoundingClientRect();
  const inside = rect.top <= e.clientY && e.clientY <= rect.bottom && rect.left <= e.clientX && e.clientX <= rect.right;
  if (!inside) closeWeek();
});

copyBtn.addEventListener("click", async () => {
  if (activeWeekNum === null) return;
  try {
    await copyRich({ text: buildEmailText(activeWeekNum), html: buildEmailHtml(activeWeekNum) });
    modalStatus.textContent = "Copied to clipboard.";
  } catch (err) {
    modalStatus.textContent = "Copy failed. Try selecting the text and copying manually.";
  }
});

document.getElementById("heroWeeksBtn").addEventListener("click", () => {
  const el = document.getElementById("weeks");
  if (el) el.scrollIntoView({ behavior: "smooth" });
});
document.getElementById("heroRolesBtn").addEventListener("click", () => {
  const el = document.getElementById("roles");
  if (el) el.scrollIntoView({ behavior: "smooth" });
});

// ── INIT ──────────────────────────────────────────────────────────────────────
renderRoles();
renderWeeks();
