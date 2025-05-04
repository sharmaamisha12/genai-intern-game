# backend/core/moderation.py
import re

def is_clean_input(text: str) -> bool:
    banned_words = ["badword1", "badword2"]
    return all(word not in text.lower() for word in banned_words) and re.match("^[a-zA-Z ]+$", text)
