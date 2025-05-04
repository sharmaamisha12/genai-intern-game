import requests

API_URL = "http://localhost:8000/api/guess"

def test_duplicate_guess_flow():
    session = requests.Session()
    headers = {"Content-Type": "application/json", "X-Persona": "serious"}
    
    # First correct guess
    response = session.post(API_URL, json={"guess": "Paper"}, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["game_over"] is False
    print("✅ First guess accepted:", data["message"])

    # Duplicate guess → should return game over
    response2 = session.post(API_URL, json={"guess": "Paper"}, headers=headers)
    assert response2.status_code == 200
    data2 = response2.json()
    assert data2["game_over"] is True
    print("💥 Game Over on duplicate guess:", data2["message"])

if __name__ == "__main__":
    test_duplicate_guess_flow()
