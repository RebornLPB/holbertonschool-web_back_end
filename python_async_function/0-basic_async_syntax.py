import asyncio
import random

async def wait_random(time):
    if not time:
        time = 10
    await asyncio.sleep(time)
    return random.random()
