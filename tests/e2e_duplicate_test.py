# tests/e2e_duplicate_test.py
import requests

BASE = "http://localhost:8000"

def test_duplicate_guess_game_over():
    sid = requests.post(f"{BASE}/start").json()["session_id"]
    first = requests.post(f"{BASE}/guess", params={"session_id": sid, "guess": "Paper"}).json()
    second = requests.post(f"{BASE}/guess", params={"session_id": sid, "guess": "Paper"}).json()
    assert "Game Over" in second["message"]
git init
