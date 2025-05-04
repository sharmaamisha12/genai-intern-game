import re

def contains_profanity(text: str) -> bool:
    banned_words = ["badword1", "badword2"]  # Add actual words
    return any(re.search(rf"\\b{word}\\b", text.lower()) for word in banned_words)

# Step 5: backend/db/models.py
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GlobalGuess(Base):
    __tablename__ = "global_guesses"

    guess = Column(String, primary_key=True)
    count = Column(Integer, default=0)