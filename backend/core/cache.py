# backend/core/cache.py
import aioredis
import os

redis = aioredis.from_url("redis://localhost")

async def get_cached_verdict(seed, guess):
    key = f"{seed}:{guess}"
    return await redis.get(key)

async def cache_verdict(seed, guess, verdict):
    key = f"{seed}:{guess}"
    await redis.set(key, verdict, ex=3600)
