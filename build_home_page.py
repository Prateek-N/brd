import json
import os

with open(r"f:\New Stem\sept14_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

# Sept new 3 candidates data
SEPT_NEW_PEOPLE = [
  {
    "name": "Sylvester Rodrigues",
    "jobTitle": "Senior Business Analyst",
    "company": "BRIDGEPOINT CAREERS LLC",
    "slug": "sylvester-rodrigues",
    "project": "E-Commerce Sales Performance & KPI Analysis",
    "projectDesc": "Analyze a public Kaggle e-commerce dataset to identify sales trends, customer segments, and business improvement opportunities. Deliver a KPI dashboard, BRD, and stakeholder presentation.",
    "tools": "Excel, Power BI Desktop, Python pandas, Kaggle dataset, GitHub",
    "responsibilities": [
      "Gather, analyze, and interpret business data to identify trends and operational insights.",
      "Develop and maintain business dashboards, reports, and performance visualizations for stakeholders.",
      "Collect, clean, and validate business data for accuracy and consistency across systems.",
      "Perform business analysis to support decision-making, risk assessment, and strategic planning.",
      "Collaborate with cross-functional teams to understand business requirements and objectives.",
      "Identify process improvement opportunities through data-driven analysis and actionable recommendations.",
      "Monitor key business indicators (KPIs) and track operational performance metrics.",
      "Conduct ad hoc analysis to address business challenges and support operational needs.",
      "Create and maintain documentation for business requirements, reports, and analytical processes.",
      "Ensure data integrity, governance, and compliance with organizational policies and standards.",
      "Present business findings and actionable recommendations to management and key stakeholders."
    ]
  },
  {
    "name": "Niyazuddin Shaik",
    "jobTitle": "Cloud Security Engineer",
    "company": "BRIDGEPOINT CAREERS LLC",
    "slug": "niyazuddin-shaik",
    "project": "Multi-Cloud Security Architecture & Threat Detection",
    "projectDesc": "Design and monitor secure cloud infrastructure across AWS/Azure, build IAM least-privilege policies, SIEM security monitoring, and DevSecOps automated compliance scanning.",
    "tools": "AWS/Azure, Terraform, Docker, Python/Bash, SIEM/WAF, GitHub Actions",
    "responsibilities": [
      "Design, implement, and manage cloud security architectures across AWS, Azure, or GCP environments.",
      "Monitor cloud environments for security threats, vulnerabilities, and compliance violations.",
      "Conduct cloud security assessments, risk analysis, and penetration testing to identify weaknesses.",
      "Implement and manage IAM policies, roles, and access controls to enforce least-privilege principles.",
      "Configure and manage security tools such as SIEM, CSPM, WAF, and cloud-native security services.",
      "Develop and enforce cloud security policies, standards, and best practices across the organization.",
      "Respond to cloud security incidents, perform root cause analysis, and implement remediation actions.",
      "Ensure compliance with regulatory frameworks such as GDPR, HIPAA, SOC 2, and ISO 27001.",
      "Collaborate with DevOps, engineering, and IT teams to embed security into CI/CD pipelines (DevSecOps).",
      "Automate cloud security tasks using scripting languages such as Python, Bash, or Terraform.",
      "Stay current with emerging cloud security threats, vulnerabilities, and evolving industry standards."
    ]
  },
  {
    "name": "Nevil Jack Denis",
    "jobTitle": "Product Manager",
    "company": "BRIDGEPOINT CAREERS LLC",
    "slug": "nevil-jack-denis",
    "project": "AI-Driven Product Roadmap & Growth Optimization",
    "projectDesc": "Define product vision, author detailed PRDs, design user journeys in Figma, and formulate A/B experimentation frameworks to maximize SaaS engagement and retention.",
    "tools": "Figma, Jira, Notion, Amplitude/Mixpanel, Google Slides, GitHub",
    "responsibilities": [
      "Define and communicate the product vision, strategy, and roadmap aligned with business goals.",
      "Gather and prioritize product requirements from customers, stakeholders, and market research.",
      "Collaborate with engineering, design, marketing, and sales teams to deliver product features.",
      "Write clear and detailed product requirements documents (PRDs), user stories, and acceptance criteria.",
      "Manage the product backlog and prioritize features using frameworks such as RICE or MoSCoW.",
      "Define and track key product metrics, KPIs, and OKRs to measure product success.",
      "Conduct competitive analysis and market research to identify opportunities and threats.",
      "Lead product discovery sessions, user interviews, and usability testing to validate assumptions.",
      "Coordinate cross-functional sprint planning, stand-ups, and retrospectives in Agile environments.",
      "Develop go-to-market strategies and support product launches with clear positioning and messaging.",
      "Analyze product usage data and feedback to inform iteration and continuous improvement decisions."
    ]
  }
]

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

html_template = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>3-Month Project Plans · Sep 14–Dec 6, 2026</title>
<link rel="stylesheet" href="styles.css" />
<style>
.tab-row {{
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: flex-end;
}}
.search-box {{
  width: 100%;
  max-width: 360px;
  padding: 10px 16px;
  border-radius: 8px;
  border: 1px solid rgba(255,255,255,0.15);
  background: rgba(15,23,42,0.6);
  color: #fff;
  font-size: 14px;
  outline: none;
  transition: border-color 0.2s;
}}
.search-box:focus {{
  border-color: #38bdf8;
}}
.filter-bar {{
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}}
.filter-btns {{
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}}
.filter-btn {{
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 700;
  cursor: pointer;
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.15);
  color: #cbd5e1;
  transition: all 0.2s;
}}
.filter-btn.active {{
  background: #0284c7;
  color: #ffffff;
  border-color: #38bdf8;
}}
.project-badge {{
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  padding: 3px 8px;
  border-radius: 4px;
  background: rgba(56,189,248,0.15);
  color: #38bdf8;
  border: 1px solid rgba(56,189,248,0.3);
  margin-bottom: 8px;
}}
@media(max-width:1100px){{.tab-row .btn{{font-size:11px;padding:10px 14px;height:38px}}}}
@media(max-width:700px){{.tab-row .btn{{font-size:10px;padding:6px 10px;height:34px}}}}
</style>
</head>
<body>
<div class="topbar">
<div class="topbar-inner">
<div class="brand">
<div class="brand-mark"></div>
<div class="brand-title">Project Plan</div>
<div class="brand-sub">Sep 14, 2026 – Dec 6, 2026</div>
</div>
<div class="tab-row" id="tabRow">
  <button class="tab-btn btn btn-primary" data-tab="all" type="button">All Projects (27)</button>
  <button class="tab-btn btn btn-outline" data-tab="ipeople" type="button">IPEOPLE (13)</button>
  <button class="tab-btn btn btn-outline" data-tab="bridgepoint" type="button">BRIDGEPOINT (14)</button>
  <button class="tab-btn btn btn-outline" data-tab="septnew" type="button" style="background:linear-gradient(135deg,#7c3aed,#4f46e5);color:#fff;border-color:transparent;">🆕 SEPT NEW (3)</button>
</div>
</div>
</div>

<div class="wrap">
<section class="hero">
<h1>3-Month Sample Projects &amp; Weekly Plans</h1>
<p>Individual 12-week project assignments starting <strong>September 14, 2026</strong>. Review project scopes, tools, weekly milestones, and email-ready task assignments for all team members.</p>
<div class="cta-row">
<a class="btn btn-primary" href="#projects-section" style="text-decoration:none;">Browse Projects</a>
<a class="btn btn-outline" href="#weeks-section" style="text-decoration:none;">Weekly Schedule (W1–W12)</a>
</div>
</section>

<!-- 27 CANDIDATES PROJECT SECTION -->
<div id="main-content">
  <section class="section" id="projects-section">
    <div class="section-head">
      <div>
        <p class="section-label">Sep 14 – Dec 6, 2026 Cohort</p>
        <h2 class="section-title">Team Members &amp; Sample Projects</h2>
      </div>
      <div class="section-meta"><span id="candidateCount">{len(candidates)}</span> Projects</div>
    </div>

    <div class="filter-bar">
      <input type="text" id="searchInput" class="search-box" placeholder="Search by name, role, or project..." aria-label="Search candidates" />
      <div class="filter-btns">
        <button class="filter-btn active" data-filter="all">All ({len(candidates)})</button>
        <button class="filter-btn" data-filter="IPEOPLE CAREER LLC">IPEOPLE ({len([c for c in candidates if c['company']=='IPEOPLE CAREER LLC'])})</button>
        <button class="filter-btn" data-filter="BRIDGEPOINT CAREERS LLC">BRIDGEPOINT ({len([c for c in candidates if c['company']=='BRIDGEPOINT CAREERS LLC'])})</button>
      </div>
    </div>

    <div class="role-grid" id="projectsGrid" aria-label="Team member project cards"></div>
  </section>

  <section class="section" id="weeks-section">
    <div class="section-head">
      <div>
        <p class="section-label">Schedule · 12-Week Milestones</p>
        <h2 class="section-title">Week 1–Week 12 Tasks</h2>
      </div>
      <div class="section-meta">Click any week to open all individual assignments</div>
    </div>
    <div class="week-grid" id="weekGrid" aria-label="Weekly tasks grid"></div>
  </section>
</div>

<!-- SEPT NEW STARTERS SECTION -->
<div id="septnew-content" hidden>
  <section class="section" id="roles-septnew">
    <div class="section-head">
      <div>
        <p class="section-label">Team · September 2026 Starters</p>
        <h2 class="section-title">Roles &amp; Responsibilities</h2>
      </div>
      <div class="section-meta">3 team members</div>
    </div>
    <div class="role-grid" id="rolesGridSeptNew" aria-label="September new starter team members"></div>
  </section>
</div>

<footer class="footer">Generated from the Stem Task Sheet. Plan duration: Sep 14, 2026 – Dec 6, 2026.</footer>
</div>

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

<script>
const CANDIDATES = {json.dumps(candidates, indent=2)};
const SEPT_NEW_PEOPLE = {json.dumps(SEPT_NEW_PEOPLE, indent=2)};
const WEEKS_12 = {json.dumps(WEEKS_12, indent=2)};

let currentCompanyFilter = 'all';
let currentSearchQuery = '';
let activeWeekNum = null;

function escapeHtml(value) {{
  return String(value ?? "").replace(/[&<>"']/g, c => ({{"&":"&amp;","<":"&lt;",">":"&gt;","\\"":"&quot;","'":"&#39;"}}[c]));
}}

function renderProjects() {{
  const grid = document.getElementById('projectsGrid');
  const countEl = document.getElementById('candidateCount');
  
  const filtered = CANDIDATES.filter(c => {{
    const matchesComp = currentCompanyFilter === 'all' || c.company === currentCompanyFilter;
    const q = currentSearchQuery.toLowerCase().trim();
    const matchesSearch = !q || c.name.toLowerCase().includes(q) || c.jobTitle.toLowerCase().includes(q) || c.project.toLowerCase().includes(q);
    return matchesComp && matchesSearch;
  }});

  countEl.textContent = String(filtered.length);

  grid.innerHTML = filtered.map(c => `
    <article class="role-card">
      <div class="role-head">
        <div class="role-main">
          <div class="project-badge">${{escapeHtml(c.company)}}</div>
          <h3 class="role-name">${{escapeHtml(c.name)}}</h3>
          <p class="role-title">${{escapeHtml(c.jobTitle)}}</p>
        </div>
        <div class="role-side">
          <a class="btn btn-primary role-link" href="profiles/${{c.slug}}.html" style="text-decoration:none;">Open Profile →</a>
        </div>
      </div>
      <div style="margin: 12px 0 6px 0;">
        <div style="font-size:13px;font-weight:700;color:#38bdf8;margin-bottom:4px;">${{escapeHtml(c.project)}}</div>
        <p style="font-size:13px;color:#cbd5e1;line-height:1.5;margin:0 0 8px 0;">${{escapeHtml(c.projectDesc)}}</p>
      </div>
      <details class="role-details">
        <summary class="role-summary">View Tech Stack &amp; Key Duties</summary>
        <div style="font-size:12px;color:#94a3b8;margin:8px 0 10px 0;"><strong style="color:#e2e8f0;">Tools:</strong> ${{escapeHtml(c.tools)}}</div>
        <ul class="list">
          ${{c.responsibilities.map(r => `<li>${{escapeHtml(r)}}</li>`).join('')}}
        </ul>
      </details>
    </article>
  `).join('');
}}

function renderWeeks() {{
  const grid = document.getElementById('weekGrid');
  grid.innerHTML = WEEKS_12.map(w => `
    <button class="week-btn" type="button" data-week="${{w.week}}" aria-haspopup="dialog" aria-controls="weekDialog">
      <div class="week-num">Week ${{w.week}}</div>
      <div class="week-tag">Sep 14–Dec 6 Cohort</div>
      <div class="week-sub">${{escapeHtml(w.dateRange)}}</div>
      <div class="week-project">27 Individual Project Tasks</div>
      <div class="week-cta">View All Member Assignments →</div>
    </button>
  `).join('');
}}

function renderSeptNewRoles() {{
  const grid = document.getElementById('rolesGridSeptNew');
  grid.innerHTML = SEPT_NEW_PEOPLE.map(p => `
    <div class="role-card">
      <div class="role-card-header">
        <div class="role-avatar">${{p.name.split(' ').map(w=>w[0]).join('').slice(0,2)}}</div>
        <div>
          <div class="role-name">${{escapeHtml(p.name)}}</div>
          <div class="role-title">${{escapeHtml(p.jobTitle)}}</div>
          <div class="role-company" style="font-size:10px;opacity:.7;margin-top:2px;">Bridgepoint Careers LLC · Sept 2026</div>
        </div>
      </div>
      <div style="margin: 12px 0 8px 0;">
        <div style="font-size:13px;font-weight:700;color:#c084fc;">${{escapeHtml(p.project)}}</div>
        <p style="font-size:12px;color:#cbd5e1;margin:4px 0 8px 0;">${{escapeHtml(p.projectDesc)}}</p>
      </div>
      <ul class="role-list">
        ${{p.responsibilities.map(r => `<li>${{escapeHtml(r)}}</li>`).join('')}}
      </ul>
      <div class="role-footer" style="margin-top:14px;">
        <a class="btn btn-primary btn-sm" href="profiles/${{p.slug}}.html" style="text-decoration:none;display:inline-block;">Open Profile →</a>
      </div>
    </div>
  `).join('');
}}

// ── MODAL LOGIC ─────────────────────────────────────────────────────────────
const dialog = document.getElementById("weekDialog");
const modalBody = document.getElementById("modalBody");
const weekTitle = document.getElementById("weekTitle");
const weekMeta = document.getElementById("weekMeta");
const modalStatus = document.getElementById("modalStatus");
const copyBtn = document.getElementById("copyBtn");
const closeBtn = document.getElementById("closeBtn");
let closeTimer = null;

function buildModalContent(weekNum) {{
  const wInfo = WEEKS_12.find(w => w.week === weekNum);
  const peopleBlocks = CANDIDATES.map(c => {{
    const task = c.weekTasks[weekNum - 1] || "No task configured.";
    return `
      <section class="modal-card">
        <div class="modal-card-head">
          <div>
            <h3 class="modal-card-title">${{escapeHtml(c.name)}}</h3>
            <p class="modal-card-sub">${{escapeHtml(c.jobTitle)}} · ${{escapeHtml(c.company)}}</p>
          </div>
          <a class="btn btn-outline btn-sm" href="profiles/${{c.slug}}.html" style="font-size:11px;padding:4px 10px;text-decoration:none;">Profile →</a>
        </div>
        <p class="modal-k" style="margin:0 0 4px;">Project</p>
        <p class="modal-p" style="margin:0 0 10px;font-weight:700;color:#0284c7;">${{escapeHtml(c.project)}}</p>
        <p class="modal-k" style="margin:0 0 4px;">Week ${{weekNum}} Task</p>
        <ul class="modal-list"><li>${{escapeHtml(task)}}</li></ul>
      </section>
    `;
  }}).join('');

  return `
    <section class="modal-section">
      <p class="section-label">Cohort Schedule</p>
      <h3 class="modal-h3">Week ${{weekNum}} Tasks · ${{escapeHtml(wInfo.dateRange)}}</h3>
      <p class="modal-p">27 Individual Project Assignments (IPEOPLE CAREER LLC &amp; BRIDGEPOINT CAREERS LLC)</p>
    </section>
    <section class="modal-section">
      <p class="section-label">Individual Assignments</p>
      ${{peopleBlocks}}
    </section>
  `;
}}

function openWeek(weekNum) {{
  activeWeekNum = weekNum;
  const wInfo = WEEKS_12.find(w => w.week === weekNum);
  modalStatus.textContent = "";
  weekMeta.textContent = `Cohort Plan · ${{wInfo.dateRange}}`;
  weekTitle.textContent = `Week ${{weekNum}} Individual Tasks`;
  modalBody.innerHTML = buildModalContent(weekNum);
  if (typeof dialog.showModal === "function") {{
    if (!dialog.open) dialog.showModal();
    dialog.classList.remove("is-closing");
    dialog.classList.add("is-open");
    closeBtn.focus();
  }}
}}

function closeWeek() {{
  if (!dialog.open) return;
  dialog.classList.add("is-closing");
  dialog.classList.remove("is-open");
  if (closeTimer) window.clearTimeout(closeTimer);
  closeTimer = window.setTimeout(() => {{
    dialog.close();
    dialog.classList.remove("is-closing");
  }}, 160);
}}

document.getElementById("weekGrid").addEventListener("click", e => {{
  const btn = e.target.closest("[data-week]");
  if (!btn) return;
  openWeek(Number(btn.getAttribute("data-week")));
}});

closeBtn.addEventListener("click", closeWeek);
dialog.addEventListener("cancel", e => {{ e.preventDefault(); closeWeek(); }});
dialog.addEventListener("click", e => {{
  const r = dialog.getBoundingClientRect();
  const inside = r.top <= e.clientY && e.clientY <= r.bottom && r.left <= e.clientX && e.clientX <= r.right;
  if (!inside) closeWeek();
}});

copyBtn.addEventListener("click", async () => {{
  if (!activeWeekNum) return;
  const wInfo = WEEKS_12.find(w => w.week === activeWeekNum);
  const lines = [];
  lines.push(`Subject: Week ${{activeWeekNum}} Tasks — 12-Week Sample Projects (${{wInfo.dateRange}})`);
  lines.push("");
  lines.push(`Week ${{activeWeekNum}}: ${{wInfo.dateRange}}`);
  lines.push("Cohort: IPEOPLE CAREER LLC & BRIDGEPOINT CAREERS LLC");
  lines.push("");
  lines.push("Individual Tasks (by team member):");
  CANDIDATES.forEach(c => {{
    lines.push("");
    lines.push(`${{c.name}} — ${{c.jobTitle}} (${{c.company}})`);
    lines.push(`Project: ${{c.project}}`);
    lines.push(`Task: ${{c.weekTasks[activeWeekNum - 1] || "No task defined."}}`);
  }});
  lines.push("");
  lines.push("Regards,");
  lines.push("Project Lead");
  lines.push("mohan.gupta@ipeople-career.com");

  try {{
    await navigator.clipboard.writeText(lines.join("\\n"));
    modalStatus.textContent = "Copied all assignments to clipboard!";
  }} catch (err) {{
    modalStatus.textContent = "Copy failed. Please copy manually.";
  }}
}});

// ── TAB SWITCHING ────────────────────────────────────────────────────────────
function switchTab(tab) {{
  document.querySelectorAll('.tab-btn').forEach(btn => {{
    const isActive = btn.dataset.tab === tab;
    btn.classList.toggle('btn-primary', isActive);
    btn.classList.toggle('btn-outline', !isActive);
  }});

  const mainContent = document.getElementById('main-content');
  const septnewContent = document.getElementById('septnew-content');

  if (tab === 'septnew') {{
    mainContent.hidden = true;
    septnewContent.hidden = false;
    renderSeptNewRoles();
  }} else {{
    mainContent.hidden = false;
    septnewContent.hidden = true;
    if (tab === 'ipeople') {{
      currentCompanyFilter = 'IPEOPLE CAREER LLC';
    }} else if (tab === 'bridgepoint') {{
      currentCompanyFilter = 'BRIDGEPOINT CAREERS LLC';
    }} else {{
      currentCompanyFilter = 'all';
    }}
    document.querySelectorAll('.filter-btn').forEach(fb => {{
      fb.classList.toggle('active', fb.dataset.filter === currentCompanyFilter);
    }});
    renderProjects();
    renderWeeks();
  }}
}}

document.querySelectorAll('.tab-btn').forEach(btn => {{
  btn.addEventListener('click', () => switchTab(btn.dataset.tab));
}});

document.querySelectorAll('.filter-btn').forEach(btn => {{
  btn.addEventListener('click', () => {{
    currentCompanyFilter = btn.dataset.filter;
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    renderProjects();
  }});
}});

document.getElementById('searchInput').addEventListener('input', e => {{
  currentSearchQuery = e.target.value;
  renderProjects();
}});

// ── INITIALIZE ────────────────────────────────────────────────────────────────
renderProjects();
renderWeeks();
renderSeptNewRoles();
</script>
</body>
</html>
"""

# Write to both home.html and new_stem/home.html
with open(r"f:\New Stem\home.html", "w", encoding="utf-8") as f:
    f.write(html_template)

with open(r"f:\New Stem\new_stem\home.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Updated home.html and new_stem/home.html successfully.")
