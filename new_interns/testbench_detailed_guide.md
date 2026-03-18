# TestBench Project: Tools and Documentation Guide

## 1. Project Overview
**TestBench** is a DFT (Design for Testability) test pattern management, fault coverage analysis, and design testability tracking tool. The goal of this project is to automate ATPG (Automatic Test Pattern Generation) reports, track coverage trends over time, and achieve a robust 95%+ stuck-at-fault coverage.

---

## 2. Tools Required and Their Purpose

### 1. Synopsys DFT Compiler
**What it is:** A commercial electronic design automation (EDA) tool used during the synthesis of digital logic.
**How it's used in this project:**
- Used in **Week 2** to insert "scan chains" into design blocks. Scan chains are shift registers that allow the testing tools to observe and control the internal state of the chip, making it possible to detect manufacturing defects. 

### 2. TetraMAX
**What it is:** Synopsys's industry-standard ATPG tool.
**How it's used in this project:**
- Used heavily from **Week 2 to Week 5** to automatically generate the optimal set of stick-at and transition test patterns (test vectors).
- It analyzes the gate-level netlist provided by the DFT Compiler and calculates standard fault coverage scores.

### 3. Verilog
**What it is:** A Hardware Description Language (HDL) used to define and model electronic networks/chips.
**How it's used in this project:**
- The existing hardware designs and the resulting gate-level simulations are represented in Verilog. You need to understand it during **Week 1** (Review RTL design) and **Week 5** (Validate test patterns on gate-level simulation) to trace where fault coverage is dropping.

### 4. Python
**What it is:** A high-level programming language excellent for data parsing and automation.
**How it's used in this project:**
- **Week 2:** Writing coverage comparison scripts.
- **Week 3:** Writing validation scripts.
- **Week 4:** Building the core utility—a Python tool that parses large TetraMAX coverage reports, automatically visualizes coverage trends across hardware iterations, and replaces manual data entry.

### 5. TCL (Tool Command Language)
**What it is:** A scripting language commonly used to interface with and automate EDA software.
**How it's used in this project:**
- You will use TCL to script the commands required within Synopsys tools (DFT Compiler and TetraMAX) to run scan insertion and ATPG flows automatically, avoiding manual GUI clicking.

### 6. Excel
**What it is:** Spreadsheet software.
**How it's used in this project:**
- Used as a fallback or supplemental tool for storing test configuration data, logging test point justifications, and serving as the raw data source/destination when presenting your findings to the Technical and Project Leads.

---

## 3. Documentation Required (Chronological)

### Week 1: Analysis Documents
- **Design Block DFT Status:** A report detailing the current state of testability (e.g., existing scan chains, macro blocks, clocking issues) on the baseline design blocks.
- **Coverage Gap Analysis:** After running basic coverage checks, you must submit this document pointing out specific hardware blocks where test coverage falls short of the target.

### Week 3: Memory Testing Docs
- **BIST Configuration Document:** A reference document defining how Memory BIST (MBIST) algorithms and Logic BIST (LBIST) were configured to test the on-chip memory arrays and logic cores automatically without external testers.

### Week 4: Optimization Logs
- **Test Point Insertion Rationale:** Whenever you find a “hard-to-detect” fault, you add a hardware test point. This document outlines *why* each test point was added, proving that the silicon area trade-off was worth the coverage improvement.

### Week 5: Validation Results
- **Final Coverage Numbers:** The definitive summary report detailing the final achieved stuck-at and transition fault coverage across the chip after all your test points and improvements have been applied.

### Week 6: Handoff & Knowledge Transfer Docs
- **DFT Architecture Documentation:** A comprehensive overview of the entire Design for Testability architecture. Serves as the master blueprint for the silicon testers and verification teams.
- **Test Pattern Generation Guide:** A step-by-step Standard Operating Procedure (SOP) detailing how future engineers can run your TCL and Python scripts to regenerate patterns if the hardware design changes.
- **Walkthrough Video:** A 10-minute screen recording demonstrating the entire flow (running the tools, parsing the output via Python).
- **Final Project Report:** A capstone document presenting the start-to-finish story of the internship—the problems faced, solutions implemented, and final coverage goals achieved for the TestBench project.
