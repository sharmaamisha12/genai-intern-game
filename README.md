<<<<<<< HEAD
🧠 GenAI Interactive Guessing Game
This is a Generative AI-powered interactive game inspired by the "What Beats Rock" concept. Players guess words that beat a seed word (like "Rock") and get AI feedback. The project mixes real-time backend infra with LLM integration, caching, concurrency handling, and Dockerized deployment.

🚀 How to Play
    1.The game starts with a seed word (e.g., "Rock").

    2.You type in something that you believe beats the seed word (e.g., "Paper").

    3.The backend sends your guess to a Generative AI (Cohere) and checks if it makes sense.

    4.✅ If yes:

        Your score increases.

        The guess is saved in a linked list.

        You get back a global count (e.g., "Paper" has been guessed 3 times before).

    5. ❌ If you repeat a previous guess → Game Over.

🛠️ Tech Stack
    Layer	         Tool
    Backend	         Python + FastAPI
    AI Provider	     Cohere LLM API
    Cache	         Redis
    Database	     PostgreSQL
    Frontend	     HTML + JavaScript
    Deployment	     Docker + Render (Free)

⚙️ Setup Instructions
Prerequisites
        Docker Desktop installed
        Cohere API key

1. Clone this repo

    git clone https://github.com/yourusername/genai-intern-game.git
    cd genai-intern-game
2. Configure .env
    Create a .env file with:

    COHERE_API_KEY=your-api-key
    DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
    REDIS_URL=redis://redis:6379
3. Run via Docker

    docker-compose up --build
4. Access
    Open browser at: http://localhost:8000

🧪 Testing
    End-to-end test for duplicate detection:
    python tests/e2e_duplicate_test.py

🧱 Architecture

+---------------------------+
|  Frontend (HTML + JS)     |
|  - input / animation      |
+------------+--------------+
             |
             v
+------------+--------------+
|  FastAPI Backend           |
|  - /api/guess              |
|  - /api/history            |
+------------+--------------+
             |
+------------v--------------+
|  Core Logic               |
|  - game_logic.py (LinkedList) |
|  - ai_client.py (Cohere)  |
|  - cache.py (Redis Layer) |
+------------+--------------+
             |
+----+--------------+--------------+
| Redis (Verdict cache) | PostgreSQL (Guess count DB) |
+----------------------+------------------------------+

📦 Deployment (Render)
Live URL: Coming Soon

Uses render.yaml for one-click deploy.

💡 Prompt Design
Example:

    Does "Paper" beat "Rock"? Answer YES or NO only, without any explanation.
    
👤 Host Personas
    Use query header X-Persona: serious or X-Persona: cheery to change LLM tone.

🎯 Features
    ✅ AI-driven decision making

    🔁 Linked list tracking

    🌍 Global guess stats (DB)

    🚫 Duplicate detection (Game Over)

    🔥 Redis caching for verdicts

    🧵 Async I/O for concurrency

    🧼 Profanity filter

    🎉 Frontend emoji feedback

📄 License
    MIT License

=======
# genai-intern-game
🎮 Build a Generative AI-powered interactive game . It demonstrates backend integration of LLMs using Cohere API, featuring a “What Beats Rock” logic engine, caching, moderation, linked list tracking, and a lightweight frontend. Built with Python, FastAPI, PostgreSQL, Redis, and Docker.
>>>>>>> cb396770487c4fc0fa7d13869a011159b9b5e2e3
