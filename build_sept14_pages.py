import json
import os
import re

with open(r"f:\New Stem\sept14_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

WEEKS_12 = [
    {"week": 1, "dateRange": "Sep 14–Sep 20, 2026"},
    {"week": 2, "dateRange": "Sep 21–Sep 27, 2026"},
    {"week": 3, "dateRange": "Sep 28–Oct 4, 2026"},
    {"week": 4, "dateRange": "Oct 5–Oct 11, 2026"},
    {"week": 5, "dateRange": "Oct 12–Oct 18, 2026"},
    {"week": 6, "dateRange": "Oct 19–Oct 25, 2026"},
    {"week": 7, "dateRange": "Oct 26–Nov 1, 2026"},
    {"week": 8, "dateRange": "Nov 2–Nov 8, 2026"},
    {"week": 9, "dateRange": "Nov 9–Nov 15, 2026"},
    {"week": 10, "dateRange": "Nov 16–Nov 22, 2026"},
    {"week": 11, "dateRange": "Nov 23–Nov 29, 2026"},
    {"week": 12, "dateRange": "Nov 30–Dec 6, 2026"},
]

def escape_html(val):
    if not val:
        return ""
    return (str(val)
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&#39;'))

def generate_profile_html(c):
    name = c["name"]
    title = c["jobTitle"]
    company = c["company"]
    project = c["project"]
    project_desc = c["projectDesc"]
    tools = c["tools"]
    resps = c["responsibilities"]
    week_tasks = c["weekTasks"]

    resp_lis = "\n".join(f"<li>{escape_html(r)}</li>" for r in resps)
    
    plan_json = {
        "name": name,
        "jobTitle": title,
        "projectName": project,
        "projectDescription": project_desc,
        "tools": tools,
        "weeks": [
            {
                "week": w["week"],
                "raw": f"W{w['week']} ({w['dateRange']}): {week_tasks[w['week']-1]}"
            }
            for w in WEEKS_12
        ]
    }

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{escape_html(name)}</title>
<link rel="stylesheet" href="../styles.css" />
</head>
<body>
<div class="topbar">
<div class="topbar-inner">
<div class="brand">
<div class="brand-mark"></div>
<a class="brand-title" href="../home.html">Back to Home</a>
</div>
<a class="btn btn-outline" href="../home.html">Home</a>
</div>
</div>
<div class="wrap">
<section class="profile-hero">
<h1>{escape_html(name)}</h1>
<p class="title">{escape_html(title)}</p>
<div class="badge"><span class="dot"></span>{escape_html(company)}</div>
</section>

<section class="content" style="margin-bottom:24px;">
<div style="background:linear-gradient(135deg,rgba(14,165,233,0.08),rgba(99,102,241,0.08));border:1px solid rgba(14,165,233,0.25);border-radius:12px;padding:20px;margin-bottom:20px;">
  <div style="font-size:11px;letter-spacing:1px;text-transform:uppercase;color:#0284c7;font-weight:800;margin-bottom:6px;">Sample 3-Month Project · Starting Sep 14, 2026</div>
  <h2 style="font-size:20px;font-weight:800;color:#0f172a;margin:0 0 8px 0;">{escape_html(project)}</h2>
  <p style="font-size:14px;color:#334155;line-height:1.6;margin:0 0 12px 0;">{escape_html(project_desc)}</p>
  <div style="font-size:13px;color:#64748b;"><strong style="color:#0f172a;">Tech Stack &amp; Tools:</strong> {escape_html(tools)}</div>
</div>

<h2>Roles &amp; Responsibilities</h2>
<ul class="list">
{resp_lis}
</ul>
</section>

<section class="section" id="weeks">
  <div class="section-head">
    <div>
      <p class="section-label">Plan · Sep 14–Dec 6, 2026</p>
      <h2 class="section-title">Week 1–Week 12 Tasks</h2>
    </div>
    <div class="section-meta">Click a week to view and copy your assignment</div>
  </div>
  <div class="week-grid" id="weekGrid" aria-label="Weekly task navigation"></div>
</section>

<dialog class="modal" id="weekDialog" aria-labelledby="weekTitle" aria-describedby="weekMeta">
  <div class="modal-inner">
    <div class="modal-header">
      <div class="modal-headings">
        <p class="modal-label" id="weekMeta"></p>
        <h2 class="modal-title" id="weekTitle"></h2>
      </div>
      <div class="modal-actions">
        <button class="btn btn-primary modal-copy" type="button" id="copyBtn" aria-label="Copy week tasks to clipboard">Copy to Clipboard</button>
        <button class="btn btn-outline modal-close" type="button" id="closeBtn" aria-label="Close modal">Close</button>
      </div>
    </div>
    <div class="modal-body" id="modalBody"></div>
    <div class="modal-status" id="modalStatus" aria-live="polite"></div>
  </div>
</dialog>

<footer class="footer">Weekly Plan</footer>
</div>

<script>
const PLAN = {json.dumps(plan_json, indent=2)};

function escapeHtml(value) {{
  return String(value ?? "").replace(/[&<>"']/g, c => ({{"&":"&amp;","<":"&lt;",">":"&gt;","\\"":"&quot;","'":"&#39;"}}[c]));
}}

function splitSteps(taskText) {{
  const txt = String(taskText || "").trim();
  const parts = txt.split(":");
  const body = parts.length > 1 ? parts.slice(1).join(":").trim() : txt;
  const rawSteps = body.split(/(?:;\\s*|\\.\\s+)/).map(s => s.trim()).filter(Boolean);
  if (!rawSteps.length) return [body];
  return rawSteps.map(s => s.replace(/^[•\\-–—\\s]+/, "").trim()).filter(Boolean);
}}

function getWeekHeading(raw) {{
  const m = String(raw || "").match(/^W\\d+\\s*\\(([^)]+)\\)/);
  return m ? m[1] : "";
}}

function cleanTaskBody(raw) {{
  const parts = String(raw || "").split(":");
  return parts.length > 1 ? parts.slice(1).join(":").trim() : raw;
}}

const grid = document.getElementById("weekGrid");
const dialog = document.getElementById("weekDialog");
const modalBody = document.getElementById("modalBody");
const weekTitle = document.getElementById("weekTitle");
const weekMeta = document.getElementById("weekMeta");
const modalStatus = document.getElementById("modalStatus");
const copyBtn = document.getElementById("copyBtn");
const closeBtn = document.getElementById("closeBtn");

let activeWeek = null;
let closeTimer = null;

grid.innerHTML = (PLAN.weeks || []).map(w => {{
  const dateRange = getWeekHeading(w.raw);
  const taskBody = cleanTaskBody(w.raw);
  return `
    <button class="week-btn" type="button" data-week="${{w.week}}" aria-haspopup="dialog" aria-controls="weekDialog">
      <div class="week-num">Week ${{w.week}}</div>
      <div class="week-sub">${{escapeHtml(dateRange)}}</div>
      <div class="week-title">${{escapeHtml(taskBody)}}</div>
      <div class="week-cta">Open Tasks →</div>
    </button>
  `;
}}).join("");

function buildModal(w) {{
  const dateRange = getWeekHeading(w.raw);
  const taskBody = cleanTaskBody(w.raw);
  const steps = splitSteps(w.raw);
  return `
    <section class="modal-section">
      <p class="section-label">Scope &amp; Tooling</p>
      <h3 class="modal-h3">${{escapeHtml(PLAN.projectName || "Project Plan")}}</h3>
      <p class="modal-p">${{escapeHtml(PLAN.projectDescription || "")}}</p>
      <div class="modal-split">
        <div>
          <p class="modal-k">Assigned Member</p>
          <p class="modal-p">${{escapeHtml(PLAN.name)}} — ${{escapeHtml(PLAN.jobTitle)}}</p>
        </div>
        <div>
          <p class="modal-k">Tech Stack &amp; Tools</p>
          <p class="modal-p">${{escapeHtml(PLAN.tools || "—")}}</p>
        </div>
      </div>
    </section>
    <section class="modal-section">
      <p class="section-label">Week ${{w.week}} Focus</p>
      <h3 class="modal-h3">${{escapeHtml(taskBody)}}</h3>
      <ul class="modal-list">
        ${{steps.map(s => `<li>${{escapeHtml(s)}}</li>`).join("")}}
      </ul>
    </section>
  `;
}}

function openModal(weekNum) {{
  const w = (PLAN.weeks || []).find(x => x.week === weekNum);
  if (!w) return;
  activeWeek = w;
  modalStatus.textContent = "";
  weekMeta.textContent = `${{escapeHtml(PLAN.name)}} · Week ${{w.week}} (${{getWeekHeading(w.raw)}})`;
  weekTitle.textContent = `Week ${{w.week}} Task Assignment`;
  modalBody.innerHTML = buildModal(w);
  if (typeof dialog.showModal === "function") {{
    if (!dialog.open) dialog.showModal();
    dialog.classList.remove("is-closing");
    dialog.classList.add("is-open");
    closeBtn.focus();
  }}
}}

function closeModal() {{
  if (!dialog.open) return;
  dialog.classList.add("is-closing");
  dialog.classList.remove("is-open");
  if (closeTimer) window.clearTimeout(closeTimer);
  closeTimer = window.setTimeout(() => {{
    dialog.close();
    dialog.classList.remove("is-closing");
  }}, 160);
}}

grid.addEventListener("click", e => {{
  const btn = e.target.closest("[data-week]");
  if (!btn) return;
  openModal(Number(btn.getAttribute("data-week")));
}});

closeBtn.addEventListener("click", closeModal);
dialog.addEventListener("cancel", e => {{ e.preventDefault(); closeModal(); }});
dialog.addEventListener("click", e => {{
  const r = dialog.getBoundingClientRect();
  const inside = r.top <= e.clientY && e.clientY <= r.bottom && r.left <= e.clientX && e.clientX <= r.right;
  if (!inside) closeModal();
}});

copyBtn.addEventListener("click", async () => {{
  if (!activeWeek) return;
  const w = activeWeek;
  const dateRange = getWeekHeading(w.raw);
  const taskBody = cleanTaskBody(w.raw);
  const text = [
    `Subject: Week ${{w.week}} Tasks — ${{PLAN.name}} (${{dateRange}})`,
    "",
    `Team Member: ${{PLAN.name}} (${{PLAN.jobTitle}})`,
    `Project: ${{PLAN.projectName}}`,
    `Week ${{w.week}}: ${{dateRange}}`,
    `Tools: ${{PLAN.tools}}`,
    "",
    "Assignment Details:",
    `- ${{taskBody}}`,
    "",
    "Regards,",
    "Project Lead",
    "mohan.gupta@ipeople-career.com"
  ].join("\\n");

  try {{
    await navigator.clipboard.writeText(text);
    modalStatus.textContent = "Copied to clipboard!";
  }} catch (err) {{
    modalStatus.textContent = "Copy failed. Please copy manually.";
  }}
}});
</script>
</body>
</html>
"""

# Write profile files to both dirs
dirs = [r"f:\New Stem\profiles", r"f:\New Stem\new_stem\profiles"]
for d in dirs:
    os.makedirs(d, exist_ok=True)
    for c in candidates:
        content = generate_profile_html(c)
        fpath = os.path.join(d, f"{c['slug']}.html")
        with open(fpath, "w", encoding="utf-8") as out:
            out.write(content)

print(f"Generated {len(candidates)} profile pages in both profiles directories.")
