from fastapi import APIRouter, Request
from backend.core.ai_client import validate_guess_with_ai
from backend.core.cache import get_cached_verdict, set_cached_verdict
from backend.core.game_logic import GameSession
from backend.core.moderation import is_clean

router = APIRouter()
sessions = {}

@router.post("/play")
async def play(request: Request):
    data = await request.json()
    session_id = data.get("session_id")
    seed = data.get("seed")
    guess = data.get("guess")
    persona = data.get("persona", "Serious")

    if not is_clean(guess):
        return {"error": "Inappropriate content."}

    session = sessions.get(session_id) or GameSession()
    sessions[session_id] = session

    if guess.lower() in session.guess_set:
        return {"message": "Game Over", "score": session.score}

    verdict = await get_cached_verdict(seed, guess)
    if verdict is None:
        verdict = await validate_guess_with_ai(seed, guess, persona)
        await set_cached_verdict(seed, guess, verdict)

    if verdict:
        session.add_guess(guess)
        return {"message": f"Nice! '{guess}' beats '{seed}'.", "score": session.score}
    else:
        return {"message": f"'{guess}' does not beat '{seed}'. Try again.", "score": session.score}
