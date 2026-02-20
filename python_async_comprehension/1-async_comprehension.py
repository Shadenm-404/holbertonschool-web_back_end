#!/usr/bin/env python3
"""Task 1's module."""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Returns list of 10 random numbers."""
    return [i async for i in async_generator()]

