from collections import deque

class GameSession:
    def __init__(self):
        self.guesses = deque()
        self.guess_set = set()
        self.score = 0

    def add_guess(self, guess: str) -> bool:
        if guess.lower() in self.guess_set:
            return False
        self.guesses.append(guess)
        self.guess_set.add(guess.lower())
        self.score += 1
        return True

    def get_history(self):
        return list(self.guesses)
