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
| Basic Code Agent (HuggingFace AI Agents course) | Simple Code agents with tools such as web search, current time in any timezone given a city, etc grounded on a base code agent  | ✅ Completed | [HuggingFace](https://huggingface.co/learn/agents-course/unit1/tutorial) |
| Multi Step Code Agent (HuggingFace AI Agents course) | A collection tools for the party planning smol-agent to choose from  | ✅ Completed | [HuggingFace](https://huggingface.co/learn/agents-course/unit2/tutorial) |
| Data Analyst Agent | A simple Data Analyst Agent (smolagent's CodeAgent with data science library access) solving the famous Kaggle Titanic problem  | ✅ Completed | [HuggingFace](https://huggingface.co/learn/cookbook/agent_data_analyst) |
| RAG Agent (HuggingFace AI Agents course) | A collection of both a simple and an Agentic RAG agent  | 🛠️ In Progress | [HuggingFace](https://huggingface.co/learn/agents-course/unit2/smolagents/retrieval_agents) |
| Code Analyzer Agent | End-End code Analyzer Agent    | 🛠️ In Progress | - |

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

#### Setting up an environmental variables file (.env):
- Create a .env file in the root directory.
- Add your API keys and other necessary environment variables
```bash
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```
- This is safe because the .env file will be ignored by Git as it has been added to .gitignore.
- We load the env variables like so:
```python
from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")
```