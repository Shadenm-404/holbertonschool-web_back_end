#!/usr/bin/env python3
"""
This module measures runtime of parallel async comprehensions.
"""

import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """
    Executes async_comprehension four times in parallel
    and returns total runtime.
    """
    start = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end = time.time()
    return end - start
