"""FastAPI wrapper around SimpleRAGTrainer for the Next.js web frontend."""
from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Allow importing the existing trainer from the parent directory
PARENT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PARENT))

from simple_test import SimpleRAGTrainer  # noqa: E402

load_dotenv()

app = FastAPI(
    title="Kinetic AI — RAG Personal Trainer API",
    description="A FastAPI wrapper around the RAG trainer for the Next.js web UI.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AskRequest(BaseModel):
    question: str


class AskResponse(BaseModel):
    answer: str
    grounded: bool = True


_trainer: Optional[SimpleRAGTrainer] = None


def get_trainer() -> SimpleRAGTrainer:
    global _trainer
    if _trainer is None:
        trainer = SimpleRAGTrainer()
        try:
            kb_path = PARENT / "knowledge_base"
            trainer.load_knowledge_base(str(kb_path))
        except Exception as exc:  # pragma: no cover
            raise HTTPException(status_code=500, detail=f"KB load failed: {exc}")
        _trainer = trainer
    return _trainer


@app.get("/healthz")
def healthz():
    return {"ok": True, "kb_loaded": _trainer is not None}


@app.post("/api/ask", response_model=AskResponse)
def ask(req: AskRequest):
    if not req.question.strip():
        raise HTTPException(status_code=400, detail="Question is empty.")

    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(
            status_code=503,
            detail="OPENAI_API_KEY not set — use demo mode in the UI.",
        )

    try:
        trainer = get_trainer()
        answer = trainer.ask_question(req.question)
        return AskResponse(answer=answer, grounded=True)
    except HTTPException:
        raise
    except Exception as exc:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"{type(exc).__name__}: {exc}")
