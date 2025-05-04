# Step 1: backend/core/ai_client.py
import os
import cohere
from dotenv import load_dotenv

load_dotenv()

cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(cohere_api_key)

async def check_if_beats(guess: str, target: str, persona: str) -> bool:
    prompt = f"In a fun logic game, does '{guess}' beat '{target}'? Answer YES or NO only."
    if persona == "cheery":
        prompt = f"Hey there! In our upbeat game, do you think '{guess}' beats '{target}'? Just say YES or NO!"
    elif persona == "serious":
        prompt = f"Strict logic time. Does '{guess}' beat '{target}'? Respond with YES or NO."

    response = co.generate(
        model="command",
        prompt=prompt,
        max_tokens=5
    )
    return "YES" in response.generations[0].text.upper()
