#!/usr/bin/env python3
"""Measure runtime of four parallel async comprehensions."""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Run async_comprehension four times concurrently and return total runtime."""
    start = time.perf_counter()

    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    end = time.perf_counter()
    return end - start
