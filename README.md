# 🛡️ SOC Analyst Lab – “Hello XSS” Demo

Welcome to a focused mini-lab that lets you **run, exploit, and harden** a deliberately vulnerable Flask web-app.  
Your goal is to experience a real-world Cross-Site Scripting (XSS) workflow from **detection ➜ exploitation ➜ mitigation** and to produce concise, SOC-grade documentation of your findings.

---

## 1. Prerequisites

| Tool / Skill | Minimum version | Why you need it |
|--------------|-----------------|-----------------|
| Python       | 3.8+            | Run the Flask app |
| pip          | latest          | Install Flask |
| Browser      | any modern      | Launch the attack |
| Text editor  | your choice     | Draft answers / notes |

> **Tip:** Use an isolated VM or container if possible.

---

## 2. Setup & Launch

```bash
git clone https://github.com/your-org/hello-xss-lab.git
cd hello-xss-lab
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt     # installs Flask
python main.py


