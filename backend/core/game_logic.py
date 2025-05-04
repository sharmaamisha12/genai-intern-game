# Step 3: backend/core/game_logic.py
from collections import defaultdict
from typing import Optional

class Node:
    def __init__(self, value: str):
        self.value = value
        self.next = None

class GameSession:
    def __init__(self):
        self.head = None
        self.tail = None
        self.guess_set = set()
        self.history = []

    def add_guess(self, guess: str) -> bool:
        guess = guess.lower()
        if guess in self.guess_set:
            return False
        node = Node(guess)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.guess_set.add(guess)
        self.history.append(guess)
        return True

    def get_last_n_guesses(self, n: int = 5):
        return self.history[-n:]
