# 🦜 LangChain Journey

A hands-on learning repository documenting my journey through **LangChain** — building real AI applications chapter by chapter, from fundamentals to advanced patterns.

> Built with LangChain + Groq LLM · Python 3.12+ · Jupyter Notebooks · `uv` package manager

---

## 📖 What's Inside

This repo is structured as a progressive learning path. Each chapter builds on the last, covering core LangChain concepts through working code examples.

| Chapter | Focus |
|---------|-------|
| [CHAP-1](./CHAP-1) | LangChain Fundamentals — chains, prompts, models |
| [CHAP-2](./CHAP-2) | Memory, history & multi-turn conversations |
| [CHAP-3](./CHAP-3) | Advanced patterns — agents, tools, or RAG pipelines |

> Each chapter lives in its own folder as a Jupyter Notebook (`.ipynb`) for easy step-by-step exploration.

---

## 🛠️ Tech Stack

- **[LangChain](https://www.langchain.com/)** — core framework for building LLM applications
- **[LangChain Groq](https://python.langchain.com/docs/integrations/chat/groq/)** — blazing fast inference via Groq API
- **[LangChain Community](https://github.com/langchain-ai/langchain)** — extended integrations and loaders
- **[Python-dotenv](https://pypi.org/project/python-dotenv/)** — environment variable management
- **[uv](https://docs.astral.sh/uv/)** — modern Python package manager
- **Jupyter / IPyKernel** — interactive notebook execution

---

## 🚀 Getting Started

### Prerequisites

- Python `>= 3.12`
- [uv](https://docs.astral.sh/uv/) installed
- A [Groq API key](https://console.groq.com/) (free tier available)

### 1. Clone the repo

```bash
git clone https://github.com/Dhanushrox10/Langchain-journey.git
cd Langchain-journey
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Set up environment variables

Create a `.env` file in the root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the notebooks

Open any chapter notebook in VS Code or Jupyter:

```bash
uv run jupyter notebook
```

---

## 📁 Project Structure

```
Langchain-journey/
├── CHAP-1/             # Chapter 1 notebooks
├── CHAP-2/             # Chapter 2 notebooks
├── CHAP-3/             # Chapter 3 notebooks
├── main.py             # Entry point
├── pyproject.toml      # Project dependencies (uv)
├── .python-version     # Python version pin
├── .gitignore
└── README.md
```

---

## 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API key for LLM inference |

---

## 📚 Learning Resources

- [LangChain Docs](https://python.langchain.com/docs/introduction/)
- [Groq Console](https://console.groq.com/)
- [LangChain Expression Language (LCEL)](https://python.langchain.com/docs/concepts/lcel/)

---

## 👤 Author

**Dhanush Dev**
- Portfolio: [dhanushdev-portfolio.vercel.app](https://dhanushdev-portfolio.vercel.app)
- GitHub: [@Dhanushrox10](https://github.com/Dhanushrox10)

---

*Part of an ongoing AI/ML learning journey alongside projects in Data Engineering, RAG systems, and full-stack development.*