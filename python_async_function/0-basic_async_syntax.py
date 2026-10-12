#!/usr/bin/env python3
"""Provide an asynchronous delay function that returns a random value."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a duration and return a random float."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
