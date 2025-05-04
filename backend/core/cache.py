import aioredis
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost")

redis = aioredis.from_url(REDIS_URL, decode_responses=True)

async def get_cached_result(guess: str, target: str) -> str | None:
    key = f"{guess.lower()}:{target.lower()}"
    return await redis.get(key)

async def set_cached_result(guess: str, target: str, result: str):
    key = f"{guess.lower()}:{target.lower()}"
    await redis.set(key, result, ex=3600)