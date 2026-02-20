#!/usr/bin/env python3
"""This module defines an asynchronous generator coroutine
that yields random numbers."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Asynchronously generates ten random floating-point numbers
    between 0 and 10, yielding one every second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

