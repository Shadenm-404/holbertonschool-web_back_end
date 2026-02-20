#!/usr/bin/env python3
"""Coroutine that collects random numbers using async comprehension."""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Return a list of ten random floating-point numbers."""
    return [i async for i in async_generator()]
