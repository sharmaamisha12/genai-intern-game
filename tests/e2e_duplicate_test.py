import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_duplicate_guess():
    session_id = "test_session"
    seed = "Rock"
    guess = "Paper"

    response1 = client.post("/play", json={"session_id": session_id, "seed": seed, "guess": guess})
    response2 = client.post("/play", json={"session_id": session_id, "seed": seed, "guess": guess})

    assert response2.json()["message"] == "Game Over"
