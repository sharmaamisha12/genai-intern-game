# backend/core/ai_client.py
import os
import cohere

API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(API_KEY)

def get_prompt(seed: str, guess: str, persona: str = "serious") -> str:
    if persona == "cheery":
        return f"Hey buddy! Does \"{guess}\" beat \"{seed}\" in a fun or clever way?"
    else:
        return f"Does \"{guess}\" logically or metaphorically beat \"{seed}\"? Answer YES or NO only."

async def validate_guess(seed: str, guess: str, persona: str) -> str:
    prompt = get_prompt(seed, guess, persona)
    response = co.generate(prompt=prompt, max_tokens=5)
    return response.generations[0].text.strip()
