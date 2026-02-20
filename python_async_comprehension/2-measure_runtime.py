#!/usr/bin/env python3
"""Module that measures runtime of async comprehensions."""
import asyncio
import time
from typing import List

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Execute four async comprehensions in parallel and measure total runtime."""
    start = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end = time.perf_counter()
    return end - start
