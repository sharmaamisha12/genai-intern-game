from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.core.game_logic import Game
from backend.core.moderation import is_clean
from backend.core.client_api import ai_response1, ai_response2
from backend.core.cache import get_verdict, cache, init_cache, cache_count, get_count
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app:FastAPI):
    await init_cache()
    yield 

app = FastAPI(lifespan=lifespan)
sessions={}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Guessing Game API!"}

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://genai-intern-game-production.up.railway.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

@app.get("/")
async def get_index():
    return FileResponse("frontend/index.html")

@app.post("/start")
async def start(request: Request):
    body=await request.json()
    sessions[body['id']]=Game()
    return {"message":"Game started","seed":"Rock"}

@app.post("/guess")
async def make_guess(request: Request):
    body=await request.json()
    id=body['id']
    guess=body['guess']
    await cache_count(guess)
    global_count = await get_count(guess)
    persona=body['persona']
    session = sessions.get(id)
    if not session:
        return {"error": "No session. Start game first."}
    
    if not is_clean(guess):
        return {"error": "Inappropriate guess."}
    
    if not session.add_word(guess.lower()):
        sessions[id]=Game()
        return {"message": "Game Over! Duplicate guess.", "history": [], "score":0,"total":global_count}
    
    seed="rock"
    verdict = await get_verdict(seed,guess)
    if not verdict:
        yes_no = await ai_response1(guess,seed,persona)
        verdict = await ai_response2(guess,seed,persona)
        await cache(seed,guess,verdict)
    if "no" in yes_no.lower():
        sessions[id]=Game()
        return {"verdict":"Wrong Guess! Game Over!","message":verdict,"history":[],"score":0,"total":global_count}
    return {"verdict":"Correct Guess!", "message": verdict, "score": session.score, "history":session.history(),"total":global_count}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
