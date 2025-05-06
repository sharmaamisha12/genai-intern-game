import aioredis
import json
import os

redis = None

async def get_redis():
    global redis
    if not redis:
        redis = await aioredis.create_redis_pool((os.getenv("REDIS_HOST", "localhost"), 6379))
    return redis

async def get_cached_verdict(seed: str, guess: str) -> bool:
    redis = await get_redis()
    key = f"verdict:{seed.lower()}:{guess.lower()}"
    verdict = await redis.get(key)
    if verdict:
        return json.loads(verdict)
    return None

async def set_cached_verdict(seed: str, guess: str, verdict: bool):
    redis = await get_redis()
    key = f"verdict:{seed.lower()}:{guess.lower()}"
    await redis.set(key, json.dumps(verdict), expire=86400)
