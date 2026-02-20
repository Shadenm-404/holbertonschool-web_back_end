#!/usr/bin/env python3
"""
This module defines an asynchronous generator function
that yields random floating-point numbers.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Generate ten random floating-point numbers between 0 and 10,
    waiting one second before yielding each value.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
