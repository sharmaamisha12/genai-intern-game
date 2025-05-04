# Step 6: backend/main.py
from fastapi import FastAPI, Request, Query
from pydantic import BaseModel
from backend.core.cache import get_cached_result, set_cached_result
from backend.core.ai_client import check_if_beats
from backend.core.game_logic import GameSession
from backend.core.moderation import contains_profanity
from backend.db.models import GlobalGuess
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

app = FastAPI()
session_store = {}
engine = create_engine(os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db/postgres"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class GuessRequest(BaseModel):
    session_id: str
    guess: str
    target: str
    persona: str = "serious"

@app.post("/guess")
async def guess_word(payload: GuessRequest):
    if contains_profanity(payload.guess):
        return {"message": "Profanity not allowed"}

    cache_result = await get_cached_result(payload.guess, payload.target)
    if cache_result:
        verdict = cache_result
    else:
        verdict = "YES" if await check_if_beats(payload.guess, payload.target, payload.persona) else "NO"
        await set_cached_result(payload.guess, payload.target, verdict)

    if payload.session_id not in session_store:
        session_store[payload.session_id] = GameSession()

    game = session_store[payload.session_id]
    if verdict == "YES":
        if not game.add_guess(payload.guess):
            return {"message": "Game Over - duplicate guess!", "score": len(game.history)}
        db = SessionLocal()
        global_entry = db.query(GlobalGuess).filter_by(guess=payload.guess.lower()).first()
        if global_entry:
            global_entry.count += 1
        else:
            global_entry = GlobalGuess(guess=payload.guess.lower(), count=1)
            db.add(global_entry)
        db.commit()
        db.close()
        return {
            "message": f"✅ Nice! '{payload.guess}' beats '{payload.target}'",
            "score": len(game.history),
            "history": game.get_last_n_guesses(),
        }
    else:
        return {"message": f"❌ '{payload.guess}' does not beat '{payload.target}'", "score": len(game.history)}