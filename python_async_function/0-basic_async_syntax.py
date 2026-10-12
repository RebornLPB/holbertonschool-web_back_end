#!/usr/bin/env python3
"""Provide an asynchronous delay function that returns a random value."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a duration and return a random float."""
    await asyncio.sleep(max_delay)
    return random.uniform(0, max_delay)
