# 🔬 ResearchAI — Autonomous Multi-Agent Research System

> Four specialized AI agents that collaborate to search, read, analyse, and write comprehensive research reports — automatically.

---

## 🧠 What it does

Give ResearchAI any research topic and it autonomously deploys four AI agents that work together to produce a structured, professional research report in minutes — no manual searching, reading, or writing required.

---

## 🤖 The Four Agents

| Agent | Role |
|---|---|
| 🔍 Search Agent | Finds the most relevant sources across the web |
| 📖 Reader Agent | Extracts and processes content from each source |
| 🧠 Analyst Agent | Identifies patterns, themes and key insights |
| ✍️ Writer Agent | Produces a structured, professional report |

---

## ✨ Features

- 🔍 Autonomous web search and content extraction
- 🧠 Multi-agent collaboration pipeline
- 📋 Structured research reports with sections
- 📊 Real-time agent activity log
- 🔗 Source citations for every report
- 📥 Download report as .txt file
- ⚡ Powered by Llama 3.1 via Groq API
- 🎨 Professional dark SaaS-style UI

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| LLM | Llama 3.1 8B via Groq API |
| Web Search | Google Search + BeautifulSoup |
| Content Extraction | BeautifulSoup4 + Requests |
| Frontend | Streamlit |
| Environment | Python dotenv |

---

## 🚀 How to run locally

1. Clone the repo
2. Create virtual environment and activate it
3. Run pip install -r requirements.txt
4. Sign up at https://console.groq.com and get a free API key
5. Create a .env file and add: GROQ_API_KEY=your_key_here
6. Run streamlit run app.py

---

## 💡 How it works

1. User enters a research topic and selects depth
2. Search Agent queries the web and collects relevant URLs
3. Reader Agent visits each URL and extracts clean text
4. Analyst Agent sends all content to Llama 3.1 for analysis
5. Writer Agent generates a structured professional report
6. Report is displayed with sources and available for download

---

## 🎓 Built by

Swapna K.D 
4RA23CI042
Final Year B.E. CSE (AI/ML)
Rajeev Institute of Technology, Hassan 
 VTU Belagavi