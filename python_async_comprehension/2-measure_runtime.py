#!/usr/bin/env python3
"""Module that measures runtime of parallel async comprehensions."""
import asyncio
import time
from typing import List

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Run async_comprehension four times concurrently and measure total runtime."""
    start = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end = time.time()
    return end - start
