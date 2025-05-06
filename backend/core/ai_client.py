import os
import cohere
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

async def validate_guess_with_ai(seed_word: str, guess: str, persona: str = "Serious") -> bool:
    prompt = f"Does '{guess}' beat '{seed_word}' in a creative game? Answer YES or NO."
    if persona == "Cheery":
        prompt = f"Hey there! In our fun game, does '{guess}' beat '{seed_word}'? Please reply with YES or NO."

    response = co.chat(
        model="command-a-03-2025",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.message.content[0].text.strip().upper()
    return answer.startswith("YES")
