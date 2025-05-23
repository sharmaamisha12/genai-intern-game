# What Beats Rock? - Generative AI Game

## Setup

1. Clone the repository.
2. Create a `.env` file based on `.env.example`.
3. Run `docker-compose up --build`.

## How to Play

- Enter a word you think beats "Rock".
- The AI will validate your guess.
- Avoid repeating guesses to keep playing.

## Architecture

- **Backend**: FastAPI
- **Frontend**: HTML, CSS, JS
- **AI**: Cohere API
- **Database**: PostgreSQL
- **Cache**: Redis

## Deployment

- Use Docker for local development.
- Deploy on platforms like Render or Railway.

## Testing

Run tests using:

```bash
pytest tests/
