#!/usr/bin/env python3
"""This module defines an asynchronous comprehension coroutine
that collects random numbers generated asynchronously."""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Collects ten random floating-point numbers from an asynchronous
    generator using an asynchronous comprehension and returns them."""
    return [i async for i in async_generator()]

