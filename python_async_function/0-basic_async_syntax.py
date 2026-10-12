#!/usr/bin/env python3
"""Provide an asynchronous delay function that returns a random value."""

import asyncio
import random


async def wait_random(max_delay ):
    """Wait for a duration and return a random float.
    """
    if not max_delay :
        max_delay  = 10
    await asyncio.sleep(max_delay )
    return random.random(0, max_delay )
