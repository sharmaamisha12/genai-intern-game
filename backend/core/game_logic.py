# backend/core/game_logic.py
from collections import defaultdict, deque
import uuid

class GameSessionManager:
    def __init__(self):
        self.sessions = defaultdict(lambda: {"seed": "Rock", "guesses": deque()})

    def create_session(self):
        session_id = str(uuid.uuid4())
        self.sessions[session_id]  # Initializes it
        return session_id

    def add_guess(self, session_id, guess):
        self.sessions[session_id]["guesses"].append(guess.lower())

    def already_guessed(self, session_id, guess):
        return guess.lower() in self.sessions[session_id]["guesses"]

    def get_history(self, session_id):
        return list(self.sessions[session_id]["guesses"])

    def get_seed_word(self, session_id):
        return self.sessions[session_id]["seed"]
