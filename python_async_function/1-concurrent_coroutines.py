#!/usr/bin/env python3
"""Run asynchronous random waits and collect their delays."""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Run up to ``n`` random waits and return
    their delays in completion order.

    Args:
        n: Number of waits to run.
        max_delay: Maximum delay for each wait.

    Returns:
        The completed waits' delays, in the order they finish.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
