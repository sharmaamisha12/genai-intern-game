# backend/main.py
from fastapi import FastAPI
from backend.api.routes import router as api_router
import uvicorn

app = FastAPI(title="GenAI Guessing Game")

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
