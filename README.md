# 🤖 AI-Powered Incident Analyzer (SRE Copilot)

An AI-driven tool that analyzes logs, detects anomalies, and generates incident summaries with likely root causes and suggested remediation steps.

Built to explore how AI can enhance **Site Reliability Engineering (SRE)** workflows by reducing time spent debugging production issues.

---

## 📌 Why This Project Exists

In modern distributed systems, incident response often involves:
- Searching through thousands of log lines  
- Correlating signals across services  
- Identifying what changed under time pressure  

This process is time-consuming and error-prone.

This project explores a simple idea:

> What if AI could act as a first-pass incident investigator?

---

## 🚀 What It Does

The Incident Analyzer simulates an AI-assisted SRE workflow:

### Input
- Application logs (JSON or text)

### Processing
- Splits logs into chunks
- Uses an LLM to:
  - Detect anomalies
  - Identify error patterns
  - Summarize behavior

### Output
- 📊 Incident summary  
- 🧠 Likely root cause  
- 🛠 Suggested remediation steps  

---

## 🏗 High-Level Architecture
            ┌──────────────┐
            │   Raw Logs   │
            └──────┬───────┘
                   │
            ┌──────▼───────┐
            │  Chunking    │
            └──────┬───────┘
                   │
    ┌──────────────▼──────────────┐
    │   AI Analysis (per chunk)   │
    └──────────────┬──────────────┘
                   │
            ┌──────▼───────┐
            │ Aggregation  │
            └──────┬───────┘
                   │
            ┌──────▼───────┐
            │ Final Report │
            └──────────────┘



---

## 🔍 Example Use Case

Given logs like:
ERROR: Database connection timeout
ERROR: Failed to fetch user data
INFO: Latency increased to 1200ms
ERROR: Service A dependency failure


The system generates:
Summary:
Database timeouts are causing increased latency and cascading failures.

Root Cause:
Likely database connection exhaustion or network instability.

Suggested Actions:

Check DB health and connection pool limits
Review recent config/deploy changes
Scale database resources if needed


---

## 🧱 Tech Stack

- **Python** – core application logic  
- **OpenAI API** – log analysis & summarization  
- **dotenv** – environment configuration  

---

## 📂 Project Structure
incident-analyzer/
│── main.py # Entry point
│── analyzer.py # AI processing logic
│── sample_logs.json # Example logs
│── requirements.txt
│── .env


---

## ⚙️ Setup

### 
1. Clone the repository
```bash
git clone https://github.com/your-username/incident-analyzer.git
cd incident-analyzer

2. Install dependencies
pip install -r requirements.txt

3. Configure environment

4. Run the Project
python main.py