import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random

async def wait_n(n: int, max_delay: int = 10) -> list[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
