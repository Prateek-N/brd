import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "sept14_candidates.json"), "r", encoding="utf-8") as f:
    candidates = json.load(f)

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
    ],
    "weekTasks": [
      "Define project scope, download Kaggle e-commerce dataset, understand data schema and business context.",
      "Clean and validate data — fix nulls, standardize product categories, remove duplicate records.",
      "Perform exploratory data analysis — identify top products, sales by region, monthly revenue trends.",
      "Build KPI dashboard in Excel or Power BI — revenue, order volume, average order value.",
      "Conduct customer segmentation analysis — high-value vs. low-value customers by spend and frequency.",
      "Analyze process gaps — identify bottlenecks in the sales pipeline and order fulfillment.",
      "Build variance analysis report — actual vs. target performance with written commentary.",
      "Write a business requirements document (BRD) for one proposed process improvement.",
      "Create stakeholder presentation with charts and data-backed recommendations.",
      "Validate all findings — run data quality checks across all reports and the dashboard.",
      "Finalize dashboard, write analytical report with executive summary.",
      "Package all deliverables, record a walkthrough video, upload everything to GitHub."
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
    ],
    "weekTasks": [
      "Define cloud security baseline, review AWS/Azure CIS benchmarks, map architecture.",
      "Set up sandbox cloud environment with Terraform, configure least-privilege IAM policies.",
      "Implement VPC network security groups, firewalls, and bastion host jump boxes.",
      "Configure cloud logging and SIEM integration (CloudTrail, GuardDuty, CloudWatch).",
      "Conduct vulnerability assessment and automated penetration test scans.",
      "Deploy WAF rules and TLS/SSL certificate management to protect public endpoints.",
      "Integrate DevSecOps security scanning (SonarQube, Trivy, tfsec) into CI/CD pipelines.",
      "Build interactive Cloud Security KPI dashboard tracking open vulnerabilities and MTTR.",
      "Author Cloud Incident Response Runbook and compliance policy documentation (SOC 2 / ISO 27001).",
      "Conduct incident simulation drill: detect simulated unauthorized access and execute response SOP.",
      "Perform end-to-end security compliance audit and compile remediation reports.",
      "Finalize security architecture blueprints, publish Terraform modules and documentation to GitHub."
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
    ],
    "weekTasks": [
      "Define product vision, customer personas, strategic goals, and target OKRs.",
      "Conduct competitor benchmarking and customer discovery interviews to identify feature gaps.",
      "Author comprehensive Product Requirements Document (PRD) with user stories and acceptance criteria.",
      "Design interactive user journey maps and UI wireframes in Figma.",
      "Prioritize feature backlog using RICE scoring framework and align with engineering sprint capacity.",
      "Formulate A/B testing growth experimentation plan for core onboarding funnel.",
      "Define telemetry instrumentation specs and build product KPI dashboard (Mixpanel / Amplitude).",
      "Facilitate cross-functional sprint planning and lead backlog refinement sessions.",
      "Run user usability testing sessions on interactive prototypes, synthesize feedback.",
      "Analyze A/B test results and calculate statistical significance and conversion impact.",
      "Develop Go-To-Market (GTM) launch plan, release notes, and sales enablement documentation.",
      "Finalize executive presentation deck, record product demo video, and publish artifacts to GitHub."
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
        "company": company,
        "projectName": project,
        "projectDescription": project_desc,
        "tools": tools,
        "weeks": [
            {
                "week": w["week"],
                "dateRange": w["dateRange"],
                "task": week_tasks[w["week"]-1]
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
<style>
.week-card-box {{
  grid-column: span 3;
  background: var(--canvas-elevated);
  border: 1px solid var(--hairline);
  padding: 16px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border-radius: 8px;
  transition: transform 0.15s, border-color 0.15s;
}}
.week-card-box:hover {{
  border-color: rgba(56,189,248,0.4);
}}
@media (max-width:1100px){{.week-card-box{{grid-column:span 4}}}}
@media (max-width:800px){{.week-card-box{{grid-column:span 6}}}}
@media (max-width:520px){{.week-card-box{{grid-column:span 12}}}}
.btn-copy-direct {{
  background: #0284c7;
  color: #ffffff;
  border: 1px solid #38bdf8;
  padding: 8px 14px;
  font-size: 12px;
  font-weight: 700;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  width: 100%;
  margin-top: 12px;
  transition: all 0.2s;
}}
.btn-copy-direct:hover {{
  background: #0369a1;
}}
.btn-view-details {{
  background: transparent;
  color: #94a3b8;
  border: none;
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  cursor: pointer;
  padding: 6px 0 0 0;
  text-align: center;
  width: 100%;
}}
.btn-view-details:hover {{
  color: #f8fafc;
  text-decoration: underline;
}}
</style>
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
<div style="background:linear-gradient(135deg,rgba(14,165,233,0.12),rgba(99,102,241,0.10));border:1px solid rgba(56,189,248,0.35);border-radius:12px;padding:24px;margin-bottom:24px;box-shadow:0 4px 20px rgba(0,0,0,0.35);">
  <div style="font-size:11px;letter-spacing:1.2px;text-transform:uppercase;color:#38bdf8;font-weight:800;margin-bottom:8px;display:flex;align-items:center;gap:6px;">
    <span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:#38bdf8;"></span>
    Sample 3-Month Project · Starting Sep 14, 2026
  </div>
  <h2 style="font-size:22px;font-weight:700;color:#ffffff;margin:0 0 10px 0;line-height:1.3;">{escape_html(project)}</h2>
  <p style="font-size:14px;color:#e2e8f0;line-height:1.6;margin:0 0 16px 0;">{escape_html(project_desc)}</p>
  <div style="font-size:13px;color:#94a3b8;padding-top:14px;border-top:1px solid rgba(255,255,255,0.1);">
    <strong style="color:#38bdf8;font-weight:700;">Tech Stack &amp; Tools:</strong> <span style="color:#f8fafc;font-weight:500;">{escape_html(tools)}</span>
  </div>
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
    <div class="section-meta">Click <strong>'📋 Copy Email'</strong> to copy any week's assignment to clipboard</div>
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
        <button class="btn btn-primary modal-copy" type="button" id="copyBtn" aria-label="Copy week tasks to clipboard">📋 Copy Email to Clipboard</button>
        <button class="btn btn-outline modal-close" type="button" id="closeBtn" aria-label="Close modal">Close</button>
      </div>
    </div>
    <div class="modal-body" id="modalBody"></div>
    <div class="modal-status" id="modalStatus" aria-live="polite"></div>
  </div>
</dialog>

<footer class="footer">Weekly Plan · {escape_html(name)}</footer>
</div>

<script>
const PLAN = {json.dumps(plan_json, indent=2)};

function escapeHtml(value) {{
  return String(value ?? "").replace(/[&<>"']/g, c => ({{"&":"&amp;","<":"&lt;",">":"&gt;","\\"":"&quot;","'":"&#39;"}}[c]));
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

grid.innerHTML = (PLAN.weeks || []).map(w => `
  <div class="week-card-box">
    <div>
      <div class="week-num" style="color:#38bdf8;">Week ${{w.week}}</div>
      <div class="week-sub" style="font-size:12px;color:#94a3b8;margin:4px 0 8px 0;">${{escapeHtml(w.dateRange)}}</div>
      <div style="font-size:13px;color:#e2e8f0;line-height:1.4;">${{escapeHtml(w.task)}}</div>
    </div>
    <div>
      <button class="btn-copy-direct" type="button" data-week-copy="${{w.week}}">
        📋 Copy Week ${{w.week}} Email
      </button>
      <button class="btn-view-details" type="button" data-week-open="${{w.week}}">
        View Details &amp; Scope →
      </button>
    </div>
  </div>
`).join("");

async function copyEmailForWeek(weekNum, btnElement) {{
  const w = (PLAN.weeks || []).find(x => x.week === weekNum);
  if (!w) return;
  const text = [
    `Subject: Week ${{w.week}} Task Assignment — ${{PLAN.name}} (${{w.dateRange}})`,
    "",
    `Team Member: ${{PLAN.name}} (${{PLAN.jobTitle}})`,
    `Company: ${{PLAN.company}}`,
    `Project: ${{PLAN.projectName}}`,
    `Schedule: Week ${{w.week}} (${{w.dateRange}})`,
    `Tech Stack & Tools: ${{PLAN.tools}}`,
    "",
    "Assigned Task:",
    `- ${{w.task}}`,
    "",
    "Project Context:",
    `${{PLAN.projectDescription}}`,
    "",
    "Regards,",
    "Project Lead",
    "mohan.gupta@ipeople-career.com"
  ].join("\\n");

  try {{
    await navigator.clipboard.writeText(text);
    if (btnElement) {{
      const originalText = btnElement.innerHTML;
      btnElement.innerHTML = "✅ Copied to Clipboard!";
      btnElement.style.background = "#059669";
      btnElement.style.borderColor = "#10b981";
      setTimeout(() => {{
        btnElement.innerHTML = originalText;
        btnElement.style.background = "";
        btnElement.style.borderColor = "";
      }}, 2000);
    }}
    if (modalStatus) modalStatus.textContent = `✅ Copied Week ${{w.week}} email to clipboard!`;
  }} catch (err) {{
    if (modalStatus) modalStatus.textContent = "Copy failed. Please copy manually.";
  }}
}}

function buildModal(w) {{
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
      <p class="section-label">Week ${{w.week}} Focus (${{escapeHtml(w.dateRange)}})</p>
      <h3 class="modal-h3">${{escapeHtml(w.task)}}</h3>
      <p class="modal-p" style="margin-top:8px;">Click the top <strong>'📋 Copy Email to Clipboard'</strong> button to copy this week's email template.</p>
    </section>
  `;
}}

function openModal(weekNum) {{
  const w = (PLAN.weeks || []).find(x => x.week === weekNum);
  if (!w) return;
  activeWeek = w;
  modalStatus.textContent = "";
  weekMeta.textContent = `${{escapeHtml(PLAN.name)}} · Week ${{w.week}} (${{escapeHtml(w.dateRange)}})`;
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
  const copyBtnEl = e.target.closest("[data-week-copy]");
  if (copyBtnEl) {{
    const wNum = Number(copyBtnEl.getAttribute("data-week-copy"));
    copyEmailForWeek(wNum, copyBtnEl);
    return;
  }}
  const openBtnEl = e.target.closest("[data-week-open]");
  if (openBtnEl) {{
    const wNum = Number(openBtnEl.getAttribute("data-week-open"));
    openModal(wNum);
    return;
  }}
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
  await copyEmailForWeek(activeWeek.week, copyBtn);
}});
</script>
</body>
</html>
"""

all_to_generate = candidates + SEPT_NEW_PEOPLE
dirs = [os.path.join(BASE_DIR, "profiles"), os.path.join(BASE_DIR, "new_stem", "profiles")]
for d in dirs:
    os.makedirs(d, exist_ok=True)
    for c in all_to_generate:
        content = generate_profile_html(c)
        fpath = os.path.join(d, f"{c['slug']}.html")
        with open(fpath, "w", encoding="utf-8") as out:
            out.write(content)

print(f"Generated {len(all_to_generate)} profile pages in both profiles directories with direct copy buttons.")
