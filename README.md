# AI Agents Portfolio 🚀

A growing portfolio of self-contained AI agents, each built with a combination of **Python (backend)** and **React/JavaScript (frontend)**.

We leverage tools and services like **GroqCloud** and **Agno** for agentic LLM queries.

---

## 📂 Repository Structure

Each AI agent exists as its own independent module inside this repository.

---

## 🧱 Current Agents

| Agent Name               | Purpose                                 | Status     | Credits (if any) |
|--------------------------|-----------------------------------------|------------|------------------|
| Portfolio Helper Agent   | Provides portfolio insights via LLMs and APIs | ✅ Completed | [Andrew Baisden](https://www.freecodecamp.org/news/build-a-team-of-ai-agents-for-your-website-for-free/) |
| Financial Analysis Agent | Fetch real-time financial news and investment insights | ✅ Backend Completed | [Saimadhu Polamuri](https://dataaspirant.com/building-financial-agent-agno-groq/) |

---

## 🛠️ Tech Stack

- **Backend:** Python (Flask / FastAPI / Custom)
- **Frontend:** React (Vite)
- **AI / LLM:** GroqCloud, Agno
- **Dev Tools:** Axios, Tailwind, ESLint, etc.

---

## 🏗️ How to Run Locally

### Running a specific agent (Example: Portfolio Helper Agent):

#### Backend (Python)
```bash
cd portfolio-helper-agents
python -m venv venv
venv\Scripts\activate   # (On Windows)
pip install -r requirements.txt
python main.py

cd portfolio-helper-agents/frontend
npm install
npm run dev
```