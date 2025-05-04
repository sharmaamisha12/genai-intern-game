# backend/api/routes.py
from fastapi import APIRouter, Request, Query
from backend.core.game_logic import GameSessionManager
from backend.core.moderation import is_clean_input
from backend.core.ai_client import validate_guess
from backend.core.cache import get_cached_verdict, cache_verdict
from backend.db.models import update_global_counter, get_global_count

router = APIRouter()
game_manager = GameSessionManager()

@router.post("/start")
async def start_game():
    session_id = game_manager.create_session()
    return {"session_id": session_id, "message": "Game started. Seed word is Rock."}

@router.post("/guess")
async def guess(request: Request, session_id: str, guess: str, persona: str = Query("serious")):
    if not is_clean_input(guess):
        return {"error": "Inappropriate content"}

    seed = game_manager.get_seed_word(session_id)

    cached = await get_cached_verdict(seed, guess)
    if cached:
        verdict = cached
    else:
        verdict = await validate_guess(seed, guess, persona)
        await cache_verdict(seed, guess, verdict)

    if verdict.lower() == "yes":
        if game_manager.already_guessed(session_id, guess):
            return {"message": "Game Over! Already guessed."}
        game_manager.add_guess(session_id, guess)
        count = update_global_counter(guess)
        return {"message": f"✅ Nice! “{guess}” beats “{seed}”. {guess} has been guessed {count} times before."}
    else:
        return {"message": f"❌ Sorry, “{guess}” does not beat “{seed}”."}

@router.get("/history")
async def history(session_id: str):
    return {"history": game_manager.get_history(session_id)}
