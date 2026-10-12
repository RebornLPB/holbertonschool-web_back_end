#!/usr/bin/env python3
"""Provide an asynchronous delay function that returns a random value."""

import asyncio
import random


async def wait_random(time):
    """Wait for a duration and return a random float.
    """
    if not time:
        time = 10
    await asyncio.sleep(time)
    return random.random(0, time)
