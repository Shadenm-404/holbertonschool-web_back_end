#!/usr/bin/env python3
"""
This module measures the execution time required
to run multiple asynchronous comprehensions in parallel.
"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times concurrently
    using asyncio.gather and return the total runtime in seconds.
    """
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = time.perf_counter()
    return end - start
