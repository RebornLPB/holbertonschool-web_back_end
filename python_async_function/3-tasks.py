#!/usr/bin/env python3
"""Create asynchronous tasks that wait for a random duration."""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """Create a task that waits for a random duration.
    """
    return asyncio.create_task(wait_random(max_delay))
