#!/usr/bin/env python3
"""Measure the average time per coroutine in a batch."""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """Measure the average time taken by each coroutine.

    Args:
        n: Number of coroutines to run.
        max_delay: Maximum delay for each coroutine.

    Returns:
        Average elapsed time per coroutine.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_time = end_time - start_time
    return total_time / n
