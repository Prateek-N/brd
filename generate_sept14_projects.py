import openpyxl
import os
import json
import re

EXCEL_PATH = r"f:\New Stem\Stem - Task Sheet (2) (2).xlsx"

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

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"['\’]", "", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")

wb = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
raw_candidates = []
exclude = {"Sylvester Rodrigues", "Niyazuddin Shaik", "Nevil Jack Denis"}

for sheetname in wb.sheetnames:
    sheet = wb[sheetname]
    company = "IPEOPLE CAREER LLC" if "Ipeople" in sheetname else "BRIDGEPOINT CAREERS LLC"
    for row in list(sheet.iter_rows(values_only=True))[2:]:
        if row and row[0] and row[1]:
            name = str(row[0]).strip().replace('\xa0', ' ')
            title = str(row[1]).strip().replace('\xa0', ' ')
            resp_raw = str(row[2]).strip() if len(row)>2 and row[2] else ''
            
            lines = [l.strip().lstrip('•-* ').strip() for l in resp_raw.split('\n') if l.strip()]
            if len(lines) <= 1:
                parts = re.split(r'[\n•\-]+', resp_raw)
                lines = [p.strip() for p in parts if len(p.strip()) > 8]
            
            if name not in exclude:
                raw_candidates.append({
                    "name": name,
                    "jobTitle": title,
                    "company": company,
                    "slug": slugify(name),
                    "responsibilities": lines
                })

print(f"Loaded {len(raw_candidates)} candidates.")

PROJECT_TEMPLATES = {
    # 1. Aadharsh Jaya Bharath - Supply Chain Data Analyst
    "aadharsh-jaya-bharath": {
        "project": "End-to-End Supply Chain Inventory & Fulfillment Optimization",
        "projectDesc": "Analyze multi-warehouse inventory levels, supplier lead times, and shipping performance using Python and Power BI to build predictive replenishment models and executive KPI dashboards.",
        "tools": "Python (pandas, scikit-learn), Power BI Desktop (free), Excel, Kaggle Supply Chain Dataset, GitHub",
        "tasks": [
            "Download Kaggle supply chain shipment and inventory dataset, inspect schema, missing values, and data dictionary.",
            "Clean and validate inventory records — standardize SKU naming, resolve date formats, and filter anomalies.",
            "Conduct exploratory data analysis (EDA) on order fulfillment cycles, carrier transit times, and delayed deliveries.",
            "Build automated inventory health metrics: stockout rate, days of inventory on hand (DOH), and reorder points.",
            "Perform supplier lead-time variance and on-time in-full (OTIF) delivery performance analysis.",
            "Develop demand forecasting model using ARIMA / Random Forest to predict monthly regional SKU demand.",
            "Build interactive Power BI executive dashboard with drill-downs for stockout risks and fulfillment bottlenecks.",
            "Conduct root-cause analysis on high-cost freight routes and formulate cost-reduction recommendations.",
            "Write standard operating procedure (SOP) documentation and business requirements for inventory alerts.",
            "Perform user acceptance testing (UAT) on dashboard filters, KPI card calculations, and forecast bounds.",
            "Finalize executive summary report with recommendations for vendor SLAs and inventory rebalancing.",
            "Package all data transformation scripts, Power BI templates, and documentation; push to GitHub."
        ]
    },
    # 2. Mary Shreeja Thumma - Data Analyst
    "mary-shreeja-thumma": {
        "project": "E-Commerce Customer Behavior & Web Traffic Analytics Platform",
        "projectDesc": "Collect, clean, and analyze digital customer engagement data, build SQL Server analytical queries and create interactive reporting dashboards for business stakeholders.",
        "tools": "SQL Server / PostgreSQL, Power BI, Python (pandas, matplotlib), REST API client, GitHub",
        "tasks": [
            "Define project scope, extract web session and customer transaction dataset, review data dictionary.",
            "Clean, transform, and validate web clickstream and transaction logs to ensure schema integrity.",
            "Perform exploratory data analysis on user conversion funnels, bounce rates, and session durations.",
            "Write complex SQL stored procedures and queries to aggregate daily, weekly, and monthly customer metrics.",
            "Conduct customer cohort retention analysis to identify drop-off patterns across checkout steps.",
            "Build an interactive Power BI dashboard visualizing conversion rates, product page traffic, and user demographics.",
            "Perform A/B test analysis on promotional landing pages to quantify conversion lift and revenue impact.",
            "Establish automated data quality and consistency checks across reporting tables.",
            "Draft business requirements and analytical documentation for stakeholder self-service reporting.",
            "Perform validation and regression testing across SQL query outputs and visual dashboards.",
            "Synthesize business insights and actionable optimization recommendations into an executive slide deck.",
            "Publish completed dashboard, export SQL scripts, write project README, and commit everything to GitHub."
        ]
    },
    # 3. Durga Phani Vikas Telu - Data Analyst
    "durga-phani-vikas-telu": {
        "project": "Enterprise Financial Performance & Operational KPI Analytics",
        "projectDesc": "Design an automated data pipeline and interactive BI dashboard suite to monitor operational expenses, revenue trends, and departmental KPI variances.",
        "tools": "Power BI Desktop, Python (pandas, numpy), SQL, Excel, GitHub",
        "tasks": [
            "Collect enterprise financial and operational datasets, review data governance policies and column schemas.",
            "Execute exploratory data analysis (EDA) to detect outliers, missing values, and reconcile discrepancies.",
            "Develop ETL data cleansing pipeline using Python pandas to standardize transactional records.",
            "Create structured SQL data models with star schema (fact and dimension tables) for reporting.",
            "Build core financial KPI measures in DAX (Gross Margin, Operating Expense Variance, EBITDA margin).",
            "Develop interactive Power BI dashboard featuring dynamic department-level filtering and forecasting.",
            "Perform trend and variance analysis to identify operational cost overruns across business units.",
            "Build automated data validation scripts to verify nightly data loads and KPI calculations.",
            "Document analytical methodologies, data dictionary, and metric definitions for business users.",
            "Conduct stakeholder review session to gather feedback on report usability and layout enhancements.",
            "Incorporate feedback, optimize DAX query performance, and finalize dashboard views.",
            "Package final analytical report, presentation deck, and data models for repository handoff on GitHub."
        ]
    },
    # 4. Pooja Nigam - AI Software Engineer
    "pooja-nigam": {
        "project": "AI-Powered Customer Feedback Sentiment & Ticket Classification System",
        "projectDesc": "Develop, train, and deploy an NLP machine learning model to classify customer support tickets, analyze sentiment, and provide real-time severity scoring via a FastAPI service.",
        "tools": "Python (PyTorch / scikit-learn, HuggingFace, FastAPI), Docker, SQLite, GitHub",
        "tasks": [
            "Collect customer feedback and support ticket dataset, define classification taxonomy and performance metrics.",
            "Preprocess and clean text data: tokenization, lemmatization, stop-word removal, and class balancing.",
            "Perform exploratory data analysis on ticket categories, resolution times, and common complaint themes.",
            "Train baseline sentiment analysis and multi-class ticket classification models (Logistic Regression, DistilBERT).",
            "Tune hyperparameters, evaluate precision, recall, and F1-score across all support ticket categories.",
            "Build a modular REST API using FastAPI to serve model predictions in real time.",
            "Implement input validation, confidence threshold scoring, and fallback handling for low-confidence texts.",
            "Package the AI application with Docker and write automated unit tests for API endpoints and model pipelines.",
            "Create interactive Streamlit demonstration interface for business stakeholders to test live classifications.",
            "Benchmark model inference latency, optimize memory footprint, and implement logging and error tracking.",
            "Write comprehensive technical documentation, model card, and deployment runbook.",
            "Finalize test suite, record demonstration video, and push complete project repository to GitHub."
        ]
    },
    # 5. Disha Revandkar - Software Engineer
    "disha-revandkar": {
        "project": "Full-Stack Task & Project Milestone Management Application",
        "projectDesc": "Design, build, and test a responsive web application for managing agile sprints, task assignments, and progress tracking with role-based access control and RESTful APIs.",
        "tools": "Node.js / Express, React or Vanilla JS, SQLite / PostgreSQL, Jest, GitHub Actions",
        "tasks": [
            "Define functional requirements, user stories, and system architecture for the sprint tracker application.",
            "Design database relational schema (users, projects, sprints, tasks, comments) with proper indexing.",
            "Build RESTful backend API endpoints for authentication, CRUD operations on tasks, and sprint status tracking.",
            "Implement role-based authorization and input validation middleware to secure API endpoints.",
            "Develop responsive frontend interface featuring interactive Kanban boards and sprint burndown views.",
            "Integrate front-end components with backend APIs using asynchronous fetch and state management.",
            "Write comprehensive unit and integration tests using Jest / Supertest covering core business logic.",
            "Implement error-logging service, audit trails for task updates, and automated schema migrations.",
            "Perform cross-browser compatibility testing, responsive layout optimization, and accessibility pass.",
            "Set up CI/CD pipeline using GitHub Actions to automate linting, testing, and build verification.",
            "Conduct end-to-end user acceptance testing, fix identified edge-case bugs, and optimize load speed.",
            "Publish project documentation, API reference guide, and release package to GitHub."
        ]
    },
    # 6. Ashish Kasam - Supply Chain Specialist
    "ashish-kasam": {
        "project": "Procurement Optimization & Vendor Performance Analytics System",
        "projectDesc": "Analyze global vendor procurement records, delivery lead times, and purchase pricing trends to build a vendor scoring framework and procurement cost-saving strategy.",
        "tools": "Excel (Advanced / Power Query), Power BI Desktop, Python (pandas), Kaggle Procurement Data, GitHub",
        "tasks": [
            "Gather vendor procurement and purchase order datasets, review supplier contract SLAs and metrics.",
            "Cleanse and consolidate multi-source purchase records, eliminating duplicate supplier entries and currency mismatches.",
            "Perform exploratory data analysis on procurement spend by category, vendor lead times, and defect rates.",
            "Build a weighted Vendor Scorecard evaluating quality, price competitiveness, and delivery reliability.",
            "Analyze historical price fluctuations across raw material categories to identify bulk discount opportunities.",
            "Develop an interactive Power BI procurement dashboard with vendor performance matrices and risk flags.",
            "Identify single-source supplier vulnerabilities and propose multi-sourcing contingency strategies.",
            "Conduct safety stock and economic order quantity (EOQ) simulations to reduce excess holding costs.",
            "Draft a comprehensive Procurement Policy and Vendor Management SOP with standardized KPIs.",
            "Validate dashboard data integrity against source purchase orders and conduct user review.",
            "Synthesize cost-reduction insights into an executive business presentation with projected savings.",
            "Finalize procurement toolkit, documentation, and reporting files; publish to GitHub."
        ]
    },
    # 7. Chidi Okeke - Data Analyst
    "chidi-okeke": {
        "project": "Healthcare Operations & Patient Appointment Flow Analytics",
        "projectDesc": "Analyze patient appointment attendance, wait times, and clinic capacity utilization to build predictive no-show models and operational decision-support dashboards.",
        "tools": "SQL, Python (pandas, seaborn, scikit-learn), Power BI, Kaggle Healthcare Dataset, GitHub",
        "tasks": [
            "Obtain healthcare appointment and scheduling dataset, review HIPAA-compliant data masking standards.",
            "Perform data cleaning: impute missing clinical demographic data, parse timestamps, and handle cancellations.",
            "Conduct exploratory data analysis to evaluate clinic peak hours, patient wait times, and no-show patterns.",
            "Write SQL queries to calculate key clinic metrics: capacity utilization, average lead time, and doctor workload.",
            "Build predictive classification model (Random Forest / Logistic Regression) to forecast appointment no-shows.",
            "Evaluate model performance metrics (ROC-AUC, Precision-Recall) to establish proactive reminder thresholds.",
            "Design Power BI clinic operations dashboard with real-time appointment tracking and risk scoring.",
            "Perform root-cause analysis on scheduling bottlenecks and formulate actionable schedule-buffer guidelines.",
            "Document analytical process, data flow diagrams, and clinic management KPIs.",
            "Conduct validation tests on dashboard filters and verify accuracy of patient flow calculations.",
            "Prepare executive presentation summarizing operational insights and staffing recommendations.",
            "Package SQL scripts, Python notebooks, dashboard files, and README; upload to GitHub."
        ]
    },
    # 8. Prince Paneliya - Data Analyst
    "prince-paneliya": {
        "project": "SaaS Subscription Churn & Customer Lifetime Value (CLV) Analytics",
        "projectDesc": "Analyze subscriber lifecycle data, churn behavior, and product feature adoption to create predictive churn models and retention dashboards for SaaS leadership.",
        "tools": "Python (pandas, scikit-learn), Power BI / Tableau, SQL, Kaggle SaaS Churn Dataset, GitHub",
        "tasks": [
            "Import SaaS customer subscription and usage dataset; map customer journey stages and event logs.",
            "Clean data: handle billing status nulls, standardize currency, and engineer tenure/activity features.",
            "Perform EDA on monthly recurring revenue (MRR), churn rate by subscription tier, and support ticket frequency.",
            "Calculate key SaaS metrics: Customer Acquisition Cost (CAC), Lifetime Value (LTV), and LTV/CAC ratios.",
            "Build RFM-style engagement scoring model to categorize active, at-risk, and dormant accounts.",
            "Train machine learning classification model (XGBoost / Random Forest) to identify early churn indicators.",
            "Create interactive Power BI executive dashboard displaying MRR movements, churn cohorts, and feature adoption.",
            "Conduct feature importance analysis to reveal top friction points driving customer cancellations.",
            "Draft comprehensive business report with targeted retention campaigns for high-risk customer tiers.",
            "Perform QA validation on dashboard KPIs and cross-validate model predictions against historical holdouts.",
            "Present key findings and strategic retention recommendations in a formal summary deck.",
            "Organize project files, documentation, and analytical code into a clean GitHub repository."
        ]
    },
    # 9. Lakshmi Prasanna Tanikonda - Software Engineer
    "lakshmi-prasanna-tanikonda": {
        "project": "Secure Cloud-Ready Microservice API for Customer Account Management",
        "projectDesc": "Architect, implement, and test a scalable backend service supporting secure customer profile management, JWT authentication, rate limiting, and PostgreSQL integration.",
        "tools": "Java / Spring Boot or Node.js / Express, PostgreSQL, Docker, JUnit / Jest, Postman, GitHub",
        "tasks": [
            "Define system requirements, API specifications (OpenAPI / Swagger), and microservice architecture.",
            "Set up development environment with Docker, linting rules, and PostgreSQL database migrations.",
            "Design database relational model (users, credentials, roles, audit logs) with foreign keys and indexes.",
            "Implement secure user registration, password hashing (bcrypt), and JWT-based authentication service.",
            "Build CRUD endpoints for customer profile management with strict input validation and sanitization.",
            "Implement middleware for request rate limiting, structured error handling, and security headers.",
            "Write comprehensive unit tests and integration tests achieving >85% code coverage.",
            "Integrate Redis caching layer to optimize read-heavy profile lookup endpoints.",
            "Implement structured JSON application logging and health check / readiness probe endpoints.",
            "Perform security vulnerability audit (OWASP Top 10) and optimize database query execution plans.",
            "Conduct end-to-end API testing using Postman collections and automated test runner.",
            "Document API endpoints with Swagger UI, write deployment runbook, and push codebase to GitHub."
        ]
    },
    # 10. Praveen Kumar Borra - .Net Full Stack Developer
    "praveen-kumar-borra": {
        "project": "Enterprise Inventory & Order Processing Portal (.NET Core & Angular)",
        "projectDesc": "Build a modern full-stack web application for inventory management, real-time order processing, and supplier invoicing using ASP.NET Core Web API and SQL Server.",
        "tools": "C#, ASP.NET Core, SQL Server, Entity Framework Core, Angular / TypeScript, Bootstrap, GitHub",
        "tasks": [
            "Gather business requirements, design software architecture, and create entity relationship diagrams (ERD).",
            "Set up ASP.NET Core Web API project with clean architecture (Controller, Service, Repository layers).",
            "Configure Entity Framework Core Code-First migrations and seed initial product and category data in SQL Server.",
            "Build RESTful API endpoints for inventory stock adjustments, purchase orders, and supplier catalogs.",
            "Implement repository pattern, dependency injection, and centralized exception handling middleware.",
            "Develop responsive front-end user interface using Angular/TypeScript with data tables and modal forms.",
            "Implement JWT authentication and role-based permissions (Admin, Warehouse Manager, Staff).",
            "Write stored procedures and optimized LINQ queries for high-volume sales order reporting.",
            "Write unit tests with xUnit / Moq covering business logic in order calculation services.",
            "Perform cross-browser UI testing, form validation testing, and API load testing.",
            "Draft complete API documentation, database schema diagrams, and developer setup instructions.",
            "Finalize build pipeline, publish release package, and commit complete solution to GitHub."
        ]
    },
    # 11. Sai Anuhya Bandi - Data Engineer
    "sai-anuhya-bandi": {
        "project": "Scalable Cloud Data Pipeline & Lakehouse Ingestion Engine",
        "projectDesc": "Design and build an automated batch and streaming ETL/ELT pipeline using Python, PySpark, and PostgreSQL to ingest, clean, and model clickstream and transaction data.",
        "tools": "Python (PySpark, pandas), PostgreSQL / Snowflake, Apache Airflow / Prefect, Docker, GitHub",
        "tasks": [
            "Define data architecture requirements, ingestion protocols, and data contract specifications.",
            "Set up containerized local data warehouse environment (PostgreSQL + MinIO/S3 simulation) with Docker.",
            "Build modular Python ingestion scripts to extract JSON log files and REST API payload streams.",
            "Develop data transformation and cleansing workflows using PySpark to handle deduplication and typing.",
            "Implement automated data quality checks (Great Expectations) to enforce schema and completeness rules.",
            "Design dimensional model (Star Schema: Fact Sales, Dim Customer, Dim Product, Dim Date) in data warehouse.",
            "Build automated orchestration DAGs in Airflow to schedule nightly pipeline execution and alerting.",
            "Optimize database indexing, partitioning strategies, and query performance on million-row datasets.",
            "Implement error-handling, dead-letter queues, and automated retry mechanisms for failed pipeline runs.",
            "Conduct end-to-end integration tests to verify data reconciliation between source systems and target tables.",
            "Write technical architecture documentation, data lineage diagrams, and operational runbook.",
            "Package orchestration workflows, seed scripts, and documentation; push final project to GitHub."
        ]
    },
    # 12. Harshitha Kakumanu - Front End Developer
    "harshitha-kakumanu": {
        "project": "Interactive Analytics & Business Management Dashboard Web App",
        "projectDesc": "Design and build a high-performance, accessible, and responsive single-page web dashboard featuring dynamic data charts, filtering controls, dark/light mode, and state management.",
        "tools": "HTML5, CSS3, JavaScript (ES6+), Chart.js, Vite, GitHub Pages",
        "tasks": [
            "Review UI/UX wireframes, design system specifications, color palettes, and typography tokens.",
            "Set up project workspace using Vite with modern CSS variables, responsive grid system, and reset styles.",
            "Build semantic and accessible HTML structure with responsive sidebar navigation and header search.",
            "Develop reusable UI component library: metric cards, badges, modal dialogs, and toast notifications.",
            "Integrate Chart.js / ApexCharts to render interactive line, bar, and doughnut charts for KPIs.",
            "Implement multi-attribute filtering, search sorting, and pagination controls for data tables.",
            "Build light/dark theme switcher with localStorage persistence and CSS transition animations.",
            "Implement client-side form validation with accessible ARIA live-region feedback for user inputs.",
            "Perform cross-browser compatibility testing (Chrome, Safari, Firefox, Edge) and responsive layout checks.",
            "Optimize web performance: lazy-loading, asset compression, and Lighthouse score >90 across all categories.",
            "Conduct accessibility audit (WCAG 2.1 AA) ensuring full keyboard navigation and screen reader support.",
            "Deploy live application to GitHub Pages and publish complete code repository with demo documentation."
        ]
    },
    # 13. Karthik Kalyan Kakumanu - Software Developer
    "karthik-kalyan-kakumanu": {
        "project": "Secure Multi-Tenant REST API & User Role Management System",
        "projectDesc": "Develop a robust backend web application featuring secure user management, RBAC authorization, audit logging, and automated unit/integration testing.",
        "tools": "Python / FastAPI or Node.js / Express, SQLite / PostgreSQL, PyTest, Docker, Git, GitHub",
        "tasks": [
            "Analyze software specifications, design API contract (OpenAPI 3.0), and map database entity relations.",
            "Initialize repository with code formatting (Black / Prettier), linting, and environment configuration.",
            "Design database relational schema with foreign key constraints, indexes, and audit timestamp triggers.",
            "Implement user authentication module with password hashing, email format validation, and JWT tokens.",
            "Develop CRUD API endpoints for managing organization tenants, user profiles, and permission roles.",
            "Build authorization middleware enforcing least-privilege role-based access control (Admin, Editor, Viewer).",
            "Write comprehensive unit test suite with PyTest / Mocha covering authentication and authorization flows.",
            "Implement centralized request logging, request-ID tracing, and structured error responses.",
            "Conduct API load testing and benchmark response latencies under concurrent user requests.",
            "Perform security code review, patch input validation vulnerabilities, and sanitize SQL inputs.",
            "Draft complete API documentation with interactive Swagger UI and developer integration guide.",
            "Package Docker deployment container, configure GitHub Actions workflow, and push to GitHub."
        ]
    },
    # 14. Alma Babydasan - Software Developer
    "alma-babydasan": {
        "project": "Real-Time Incident Tracking & Service Desk Management System",
        "projectDesc": "Build a modular web application for creating, prioritizing, assigning, and resolving IT service incidents with status updates, notifications, and audit tracking.",
        "tools": "JavaScript / Node.js, Express, PostgreSQL / SQLite, Jest, CSS3, GitHub",
        "tasks": [
            "Define system requirements, incident lifecycle workflows, and database entity relationships.",
            "Set up backend server architecture with Express, middleware pipeline, and database connection pooling.",
            "Design database schema for incidents, priority SLAs, user assignments, and status change logs.",
            "Implement REST API endpoints for incident creation, assignment updates, and resolution timestamps.",
            "Build responsive front-end interface with incident dashboard, priority color-coding, and status filters.",
            "Implement SLA breach calculation logic and automated priority escalations based on incident age.",
            "Write comprehensive unit and integration tests for incident lifecycle state transitions.",
            "Perform cross-functional code review and refactor codebase to adhere to clean code principles.",
            "Conduct cross-browser UI testing and optimize page responsiveness for mobile and desktop screens.",
            "Implement audit logging service to record all user actions and ticket history modifications.",
            "Conduct end-to-end user acceptance testing and fix edge cases in assignment workflows.",
            "Package release build, write user guide and API documentation, and publish repository to GitHub."
        ]
    },
    # 15. Yash Sodvadiya - Cloud Engineer
    "yash-sodvadiya": {
        "project": "Automated Cloud Infrastructure Provisioning & Security Baseline (Terraform + AWS/LocalStack)",
        "projectDesc": "Design and deploy scalable, secure cloud infrastructure using Infrastructure as Code (IaC), automated backup routines, monitoring alarms, and cost optimization policies.",
        "tools": "Terraform, AWS / LocalStack, Docker, Bash / Python, GitHub Actions",
        "tasks": [
            "Define cloud architecture requirements: multi-tier VPC, public/private subnets, and security groups.",
            "Set up LocalStack / AWS sandbox environment and configure Terraform state backend.",
            "Write modular Terraform code for VPC, Internet Gateway, route tables, and NAT Gateway configurations.",
            "Deploy auto-scaling compute instances (EC2/ECS) behind an Application Load Balancer (ALB).",
            "Configure secure IAM policies, least-privilege roles, and enforced multi-factor authentication policies.",
            "Set up automated S3 storage buckets with lifecycle policies, server-side encryption, and versioning.",
            "Implement infrastructure monitoring using CloudWatch metrics, custom dashboards, and email alert alarms.",
            "Develop automated backup and disaster recovery scripts for databases and snapshot retention.",
            "Perform cloud security audit using tools like tfsec / Checkov and remediate misconfigurations.",
            "Implement cost optimization policies (resource tagging, auto-stop schedules for dev environments).",
            "Write comprehensive cloud infrastructure runbook, architecture diagrams, and disaster recovery plan.",
            "Publish Terraform modules, CI validation workflows, and documentation to GitHub."
        ]
    },
    # 16. Akhila Jangam - Data Analyst
    "akhila-jangam": {
        "project": "E-Commerce Customer Retention & Sales Performance Analytics",
        "projectDesc": "Clean, validate, and analyze multi-channel retail sales data to build customer segmentation models, track monthly revenue velocity, and deliver interactive Power BI dashboards.",
        "tools": "Excel (Power Query), SQL, Power BI Desktop, Python (pandas, matplotlib), GitHub",
        "tasks": [
            "Acquire e-commerce retail dataset, inspect table relationships, and define analysis scope.",
            "Clean and transform raw transactional data using Power Query and Python, handling missing records.",
            "Perform exploratory data analysis on sales volume by product category, discount rate, and geography.",
            "Write advanced SQL queries to calculate customer repurchase rates, churn rates, and average basket sizes.",
            "Build customer segmentation model (RFM: Recency, Frequency, Monetary) to identify top VIP accounts.",
            "Design multi-page Power BI dashboard with dynamic KPI cards, time-series forecasting, and segment slicers.",
            "Conduct discount sensitivity analysis to evaluate profit margins across different promotional campaigns.",
            "Implement automated data validation checks to identify revenue discrepancies and duplicate orders.",
            "Draft detailed business analysis report with data-driven recommendations for inventory and sales teams.",
            "Conduct dashboard usability testing with stakeholders to refine filter interactions and visual clarity.",
            "Prepare executive presentation deck summarizing findings, retention trends, and revenue opportunities.",
            "Organize project files, DAX measures dictionary, and documentation into a public GitHub repository."
        ]
    },
    # 17. Heny Patel - Business System Analyst
    "heny-patel": {
        "project": "ERP Order-to-Cash System Enhancement & Process Automation (BRD + UAT)",
        "projectDesc": "Lead the business analysis for optimizing an enterprise Order-to-Cash (O2C) workflow, preparing comprehensive Business Requirements Documents (BRD), process maps (BPMN), and UAT test suites.",
        "tools": "Jira / Confluence, Lucidchart / Visio, Excel, Postman, Google Slides, GitHub",
        "tasks": [
            "Conduct stakeholder interviews to map the current-state ('As-Is') Order-to-Cash workflow and identify pain points.",
            "Perform gap analysis and create 'To-Be' business process flowcharts using BPMN 2.0 notation in Lucidchart.",
            "Author comprehensive Business Requirements Document (BRD) and Functional Specifications Document (FSD).",
            "Translate business needs into detailed User Stories with MoSCoW prioritization and acceptance criteria (Gherkin).",
            "Collaborate with development team to review technical architecture, API payloads, and database mapping.",
            "Develop detailed User Acceptance Testing (UAT) test plans, test matrices, and test execution scripts.",
            "Execute functional system testing and validate API response codes using Postman collections.",
            "Lead defect triage sessions with QA and engineering teams, tracking resolution status in Jira.",
            "Conduct end-user training sessions and draft standard operating procedures (SOP) and user quick-guides.",
            "Perform post-implementation data reconciliation to verify order throughput and billing accuracy.",
            "Prepare executive project closure report highlighting efficiency gains and process cycle-time reduction.",
            "Package all BRD templates, process maps, test scripts, and presentations; publish to GitHub."
        ]
    },
    # 18. Anvitha Gaddam - Data Analyst
    "anvitha-gaddam": {
        "project": "Marketing Campaign ROI & Lead Conversion Funnel Analytics",
        "projectDesc": "Analyze multi-channel digital marketing campaigns, customer acquisition costs, and conversion funnel bottlenecks to build predictive lead-scoring models and executive dashboards.",
        "tools": "SQL, Python (pandas, seaborn), Power BI Desktop, Excel, GitHub",
        "tasks": [
            "Collect marketing campaign performance and lead generation dataset; inspect attribution channels.",
            "Clean and merge campaign cost data with CRM lead conversion records, standardizing UTM parameters.",
            "Perform exploratory data analysis on conversion rates, cost per acquisition (CPA), and click-through rates (CTR).",
            "Write SQL queries to analyze lead progression through MQL (Marketing Qualified) and SQL (Sales Qualified) stages.",
            "Build an interactive Power BI marketing analytics dashboard comparing ROI across organic, paid, and email channels.",
            "Conduct attribution modeling (first-touch vs. last-touch vs. linear) to assess true channel impact on closed revenue.",
            "Develop a rule-based lead scoring model in Python to prioritize high-intent prospects for sales outreach.",
            "Perform data quality audits to reconcile tracking discrepancies between Google Analytics and CRM tables.",
            "Document analytical methodologies, KPI formulas, and data dictionary for marketing stakeholders.",
            "Conduct stakeholder walkthrough to gather feedback on dashboard usability and filter responsiveness.",
            "Synthesize strategic recommendations for marketing budget reallocation into an executive presentation.",
            "Organize SQL scripts, Python notebooks, dashboard files, and README in a GitHub repository."
        ]
    },
    # 19. Anil Budhathoki - Data Analyst
    "anil-budhathoki": {
        "project": "Retail Customer Behavior & Basket Association Analysis",
        "projectDesc": "Analyze large-scale retail point-of-sale transactions to discover item affinities, seasonal purchasing surges, and customer loyalty trends using Python and Power BI.",
        "tools": "Python (pandas, mlxtend, matplotlib), Power BI Desktop, SQL, Kaggle Retail Data, GitHub",
        "tasks": [
            "Download Kaggle retail transaction dataset; explore schema, transaction timestamps, and item catalogs.",
            "Clean data: handle null customer IDs, filter cancelled/refunded transactions, and standardize product codes.",
            "Perform EDA on top-selling products, revenue distribution by country, and peak shopping hours.",
            "Build Market Basket Analysis using Apriori algorithm to identify frequently co-purchased item pairings.",
            "Calculate key association metrics (Support, Confidence, Lift) to inform cross-selling recommendations.",
            "Perform customer segmentation using RFM analysis to distinguish one-time buyers from repeat loyalists.",
            "Design an interactive Power BI dashboard featuring product affinity networks and sales KPI cards.",
            "Write SQL queries for ad-hoc business reporting (top revenue drivers, low-margin inventory items).",
            "Perform statistical hypothesis testing to evaluate the impact of promotional pricing on total basket size.",
            "Conduct QA validation across dashboard visualizations and verify calculations against raw data sources.",
            "Write comprehensive analytical report outlining cross-selling strategies and shelf-placement recommendations.",
            "Upload Python notebooks, SQL scripts, Power BI dashboard, and project README to GitHub."
        ]
    },
    # 20. Hrishikesh Hete - Data Analyst
    "hrishikesh-hete": {
        "project": "Telecom Customer Churn Prediction & Retention Analytics",
        "projectDesc": "Evaluate customer usage patterns, contract structures, and service complaints to build machine learning churn prediction models and operational retention dashboards.",
        "tools": "Python (pandas, scikit-learn, seaborn), Power BI Desktop, SQL, Kaggle Telco Churn Data, GitHub",
        "tasks": [
            "Acquire Kaggle Telecom customer dataset, inspect feature types, and identify class imbalances.",
            "Clean data: impute missing total charges, convert categorical variables, and remove duplicate records.",
            "Perform exploratory data analysis on churn rates across contract types, payment methods, and tenure bands.",
            "Write SQL queries to segment customer cohorts by monthly charges and customer service call frequency.",
            "Train and evaluate machine learning models (Logistic Regression, Decision Trees, Random Forest) for churn prediction.",
            "Analyze feature importance and SHAP values to identify key drivers behind customer churn decisions.",
            "Build an interactive Power BI dashboard displaying real-time churn risk scores and revenue at risk.",
            "Develop targeted customer retention strategies for high-risk cohorts based on contract tenure and usage.",
            "Establish automated data validation rules to verify accuracy of incoming customer telemetry data.",
            "Perform model calibration and threshold tuning to balance precision and recall for proactive outreach.",
            "Draft executive summary report and slide presentation with projected ROI of retention initiatives.",
            "Package all data transformation code, models, and visualization files into a GitHub repository."
        ]
    },
    # 21. Vivek Kathrotiya - Product Manager (Growth & AI Experimentation)
    "vivek-kathrotiya": {
        "project": "AI-Powered Product Recommendation Engine & Growth Experimentation Framework",
        "projectDesc": "Define the product vision, experimentation roadmap, PRDs, and user experience for integrating personalized AI recommendations into a SaaS platform to drive user engagement and conversion.",
        "tools": "Figma (Wireframing), Jira / Notion, Amplitude / Mixpanel (Simulated), Google Analytics, GitHub",
        "tasks": [
            "Conduct competitive market research and user interviews to identify personalization opportunities in the user journey.",
            "Define product vision, strategic goals, OKRs, and north-star metrics for the recommendation engine.",
            "Author comprehensive Product Requirements Document (PRD) detailing user stories, UX flows, and acceptance criteria.",
            "Design low-fidelity wireframes and interactive user journey maps for recommendation widgets in Figma.",
            "Formulate hypothesis-driven Growth Experimentation backlog prioritized using the RICE framework.",
            "Design A/B testing experiment specifications: sample sizing, primary/secondary metrics, and guardrail metrics.",
            "Collaborate with engineering and data science teams to define API contracts and model evaluation criteria.",
            "Build interactive analytics dashboard mockups tracking CTR, conversion lift, and session engagement.",
            "Conduct usability testing sessions with target users to gather qualitative feedback on recommendation relevance.",
            "Analyze simulated A/B test results, perform statistical significance testing, and determine rollout decisions.",
            "Create Go-to-Market (GTM) rollout plan, product release notes, and stakeholder presentation.",
            "Organize all PRDs, experiment blueprints, wireframes, and documentation in a GitHub repository."
        ]
    },
    # 22. Snehal Ashok Gulve - Project Manager
    "snehal-ashok-gulve": {
        "project": "Enterprise Agile Software Delivery & Governance Framework (SaaS Migration)",
        "projectDesc": "Establish an end-to-end Agile project management framework for a core SaaS platform migration, including WBS, sprint schedules, risk registries, stakeholder communication plans, and budget tracking.",
        "tools": "Jira / Trello, MS Project / Excel, Confluence, Miro, Google Slides, GitHub",
        "tasks": [
            "Develop comprehensive Project Charter outlining scope, objectives, success criteria, and stakeholder matrix.",
            "Create Work Breakdown Structure (WBS) and map milestone dependencies across engineering and QA teams.",
            "Establish Agile sprint cadence: define sprint planning, daily stand-up, review, and retrospective rituals.",
            "Build dynamic Project Schedule and Gantt chart tracking critical path activities and resource allocation.",
            "Create Risk, Assumptions, Issues, and Dependencies (RAID) log with quantitative mitigation strategies.",
            "Implement project budget tracker monitoring planned vs. actual labor hours and software licensing costs.",
            "Design executive weekly status report template highlighting milestone velocity, burn-down, and key blockers.",
            "Facilitate cross-functional backlog refinement sessions, ensuring high-quality user story definitions.",
            "Establish quality governance gates and acceptance criteria checklist for milestone sign-offs.",
            "Conduct mid-project retrospective and implement process improvements to optimize team velocity.",
            "Prepare final Project Closeout Report, lessons learned repository, and benefits realization framework.",
            "Package all project management artifacts, templates, schedules, and reports for GitHub handoff."
        ]
    },
    # 23. Supreet Kaur - Data Analyst
    "supreet-kaur": {
        "project": "Banking Fraud Detection & Transaction Risk Pattern Analytics",
        "projectDesc": "Analyze high-volume financial transaction records to uncover fraudulent transaction patterns, anomaly clusters, and merchant risk profiles using SQL and Python.",
        "tools": "SQL, Python (pandas, scikit-learn, seaborn), Power BI Desktop, Kaggle Credit Fraud Dataset, GitHub",
        "tasks": [
            "Acquire Kaggle credit card transaction dataset; analyze class imbalance and PCA feature transformations.",
            "Clean data: scale transaction amounts and time offsets, and verify zero data leakage across partitions.",
            "Conduct exploratory data analysis to profile fraudulent transaction amounts, geographic spikes, and times.",
            "Write complex SQL queries to identify rapid-succession transactions and unusual velocity spikes.",
            "Train anomaly detection and classification models (Isolation Forest, Logistic Regression, XGBoost).",
            "Evaluate model performance using Precision-Recall curves, F1-scores, and cost-matrix optimization.",
            "Design an interactive Power BI fraud risk dashboard with real-time alert filters and merchant risk rankings.",
            "Perform root-cause analysis on false positives to establish rule-based decision thresholds for transaction holds.",
            "Document fraud detection rules, data governance policies, and compliance procedures.",
            "Validate dashboard data consistency against underlying SQL models and verify query performance.",
            "Synthesize operational fraud findings and prevention strategies into an executive report.",
            "Organize Python notebooks, SQL scripts, Power BI dashboard, and project README on GitHub."
        ]
    },
    # 24. Sai Satya Pavan Kalepu - Network Engineer
    "sai-satya-pavan-kalepu": {
        "project": "Enterprise Multi-Site Network Architecture & VPN Security Hardening",
        "projectDesc": "Design, configure, and simulate a resilient multi-branch corporate network featuring VLAN segmentation, OSPF routing, site-to-site IPsec VPN, and SNMP performance monitoring.",
        "tools": "Cisco Packet Tracer / GNS3, Wireshark, Python (Netmiko / Scapy), Bash, GitHub",
        "tasks": [
            "Gather enterprise connectivity requirements and design network topology diagram (Core, Distribution, Access).",
            "Design IPv4 and IPv6 subnetting schemes with VLAN segmentation for corporate, guest, and server tiers.",
            "Configure Cisco router interfaces and implement dynamic routing protocols (OSPF Multi-Area).",
            "Implement Access Control Lists (ACLs) and stateful firewall rules to enforce least-privilege traffic flow.",
            "Configure site-to-site IPsec VPN tunnels between headquarters and remote branch offices with AES-256 encryption.",
            "Set up remote access SSL-VPN with user authentication and role-based access restrictions.",
            "Implement network services: DHCP snooping, Dynamic ARP Inspection (DAI), and Port Security on switches.",
            "Simulate network performance stress tests and capture/analyze packet flows using Wireshark.",
            "Configure SNMPv3 monitoring and Syslog forwarding to track device uptime, interface bandwidth, and errors.",
            "Perform disaster recovery and failover testing (HSRP / VRRP) to verify zero-downtime redundant links.",
            "Write comprehensive network documentation: topology diagrams, IP configuration audit, and security baseline SOP.",
            "Package network simulation files (.pkt / .gns3), Python automation scripts, and runbook; push to GitHub."
        ]
    },
    # 25. Sai Manohar Palevar - Java Full Stack Developer
    "sai-manohar-palevar": {
        "project": "Enterprise Microservices Healthcare Patient Portal (Spring Boot + React)",
        "projectDesc": "Build a secure full-stack web application for patient health records, appointment scheduling, and doctor consultations using Java Spring Boot, Hibernate, PostgreSQL, and React.",
        "tools": "Java 17, Spring Boot, Spring Security, PostgreSQL, React, Docker, JUnit, GitHub",
        "tasks": [
            "Define application requirements, microservice boundaries, and REST API contracts using OpenAPI 3.0.",
            "Set up Spring Boot project with Maven, Spring Data JPA, and PostgreSQL database migrations (Flyway).",
            "Design database relational entities (Patient, Doctor, Appointment, MedicalRecord) with relational constraints.",
            "Implement Spring Security with JWT authentication, password hashing, and role-based access control.",
            "Build RESTful APIs for appointment booking, doctor availability scheduling, and medical history lookup.",
            "Develop responsive frontend single-page application using React, Axios, and modern CSS components.",
            "Implement global exception handling, custom response wrappers, and request validation in Spring Boot.",
            "Write unit and integration tests using JUnit 5, Mockito, and SpringBootTest with >80% code coverage.",
            "Containerize backend and frontend applications using multi-stage Dockerfiles and Docker Compose.",
            "Perform performance optimization: database query indexing, Hibernate connection tuning, and caching.",
            "Conduct end-to-end user acceptance testing across appointment creation and cancellation workflows.",
            "Publish complete application code, API documentation, Swagger UI, and setup instructions to GitHub."
        ]
    },
    # 26. Shraddha Chandrakant Jathar - Data Scientist
    "shraddha-chandrakant-jathar": {
        "project": "Predictive Customer Lifetime Value & Dynamic Churn Risk Modeling",
        "projectDesc": "Develop and deploy an end-to-end machine learning pipeline to predict customer churn probability, forecast lifetime value, and explain model decisions using SHAP in a Streamlit web application.",
        "tools": "Python (pandas, scikit-learn, XGBoost, SHAP, Streamlit), Docker, MLflow, GitHub",
        "tasks": [
            "Define project objectives, acquire customer behavioral dataset, and establish validation benchmarks.",
            "Perform extensive exploratory data analysis (EDA), evaluating correlation structures and distribution skews.",
            "Execute feature engineering: customer tenure recency, interaction frequency, and rolling spend velocity.",
            "Build baseline statistical and machine learning models (Logistic Regression, Random Forest, XGBoost, LightGBM).",
            "Tune hyperparameters using Optuna / GridSearchCV and perform cross-validation with stratified splits.",
            "Evaluate model performance metrics: ROC-AUC, Precision-Recall AUC, Brier score, and expected monetary value.",
            "Implement model explainability using SHAP and LIME to generate global and individual prediction insights.",
            "Develop interactive Streamlit web application enabling business users to test predictions interactively.",
            "Containerize the data science application with Docker and write unit tests for feature transformation pipelines.",
            "Perform model fairness, bias audits, and stability tests across diverse demographic subgroups.",
            "Draft comprehensive technical documentation, model governance card, and executive presentation deck.",
            "Package Python notebooks, Streamlit app, Dockerfile, and project README for GitHub repository release."
        ]
    },
    # 27. Adarsh Mohanty - Business System Analyst
    "adarsh-mohanty": {
        "project": "Core Banking Loan Origination & Approval System Modernization (BRD + UAT)",
        "projectDesc": "Lead business systems analysis for modernizing a digital loan origination platform, producing comprehensive BRD/FRD documentation, automated workflow diagrams, and end-to-end UAT test suites.",
        "tools": "Jira, Confluence, Lucidchart, Excel, Postman, Google Slides, GitHub",
        "tasks": [
            "Conduct stakeholder discovery workshops to document current loan intake, credit assessment, and approval workflows.",
            "Perform gap analysis and design future-state process workflows in Lucidchart with BPMN 2.0 notation.",
            "Author comprehensive Business Requirements Document (BRD) and Functional Requirements Document (FRD).",
            "Create user stories with detailed acceptance criteria (Given-When-Then format) and story point estimations.",
            "Map data flow integrations between front-end loan application portal, credit bureau APIs, and core banking database.",
            "Develop comprehensive User Acceptance Testing (UAT) test plans, traceability matrix, and scenario test cases.",
            "Execute API integration verification tests using Postman to validate credit check request/response schemas.",
            "Facilitate sprint planning, backlog grooming, and defect triage meetings with engineering and QA teams.",
            "Conduct UAT execution sessions with business underwriters and capture feedback for system enhancements.",
            "Draft end-user training materials, standard operating procedures (SOP), and system admin guide.",
            "Prepare executive implementation readiness report highlighting risk assessments and rollout milestones.",
            "Consolidate all BRDs, process flows, test matrices, and training decks into a GitHub repository."
        ]
    }
}

enriched_candidates = []
for p in raw_candidates:
    slug = p["slug"]
    tmpl = PROJECT_TEMPLATES.get(slug)
    if not tmpl:
        tmpl = {
            "project": f"{p['jobTitle']} Enterprise Capstone Project",
            "projectDesc": f"Deliver a comprehensive 3-month sample project aligned with {p['jobTitle']} responsibilities and industry best practices.",
            "tools": "Python, SQL, Power BI, Excel, Git, GitHub",
            "tasks": [f"Milestone task {i+1} covering {p['jobTitle']} core competencies" for i in range(12)]
        }
    
    enriched_candidates.append({
        "name": p["name"],
        "jobTitle": p["jobTitle"],
        "company": p["company"],
        "slug": slug,
        "responsibilities": p["responsibilities"],
        "project": tmpl["project"],
        "projectDesc": tmpl["projectDesc"],
        "tools": tmpl["tools"],
        "weekTasks": tmpl["tasks"]
    })

print(f"Enriched {len(enriched_candidates)} candidates with detailed 12-week projects.")

with open(r"f:\New Stem\sept14_candidates.json", "w", encoding="utf-8") as f:
    json.dump(enriched_candidates, f, indent=2)

print("Saved sept14_candidates.json successfully.")
