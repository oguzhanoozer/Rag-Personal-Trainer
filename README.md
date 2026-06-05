# Kinetic — RAG Personal Trainer

A retrieval-augmented coach. Ask anything about training, recovery and nutrition — answers are grounded in a curated knowledge base. Ships in two flavors:

- **`web/`** — Next.js + Tailwind portfolio frontend (the recommended one for demos / deploy)
- **`app.py`** — original Streamlit interface (still works)
- **`api/`** — FastAPI wrapper that both share

**Web live:** _add Vercel URL_  ·  **API live:** _add Railway URL_

---

## What this demonstrates

| AI Engineer skill | Where it shows up |
|---|---|
| **RAG pipeline** | `rag_trainer.py` — LangChain + Chroma version |
| **Lightweight RAG** | `simple_test.py` — direct OpenAI calls with assembled context |
| **API layer** | `api/main.py` — typed FastAPI endpoint over the trainer |
| **Domain-specific KB** | `knowledge_base/` — curated fitness corpus |
| **Demo mode** | Frontend has cached Q&A so the UI is usable without a key |

## Stack

- **Web:** Next.js 15 · React 19 · Tailwind v4 · TypeScript (Inter + Syne display)
- **API:** FastAPI · OpenAI · python-dotenv
- **Streamlit (original):** Streamlit · custom HTML/CSS

## Run locally

```bash
# 1. API
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt fastapi uvicorn
cp .env.example .env       # add OPENAI_API_KEY
uvicorn api.main:app --reload   # http://localhost:8000

# 2. Web (recommended)
cd web
cp .env.example .env.local
npm install
npm run dev   # http://localhost:3000

# 3. (Optional) original Streamlit
streamlit run app.py
```

The web app has a **Demo mode** toggle — you can browse the UI without any backend.

## Deploy

- **API → Railway / Fly.io:** root `Dockerfile`. Set `OPENAI_API_KEY`.
- **Web → Vercel:** root `web/`. Set `API_URL` to the public API URL.
- **Streamlit version → Streamlit Community Cloud:** point at `app.py`.

## File map

```
api/main.py                  # FastAPI: POST /api/ask
rag_trainer.py               # Full LangChain + Chroma pipeline
simple_test.py               # Lightweight direct-OpenAI version
knowledge_base/              # *.txt corpus
app.py                       # Original Streamlit UI
web/
  src/
    app/page.tsx             # Chat + hero + demo mode
    app/layout.tsx           # Inter + Syne fonts
    app/globals.css          # Kinetic theme
    lib/demoData.ts          # Cached Q&A
```

---

> Built as part of an AI Engineer portfolio.
