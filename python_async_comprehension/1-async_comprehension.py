#!/usr/bin/env python3
"""
This module defines a coroutine that uses async comprehension
to collect random numbers from an asynchronous generator.
"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Collect ten random floating-point numbers asynchronously
    using an async comprehension and return them as a list.
    """
    return [i async for i in async_generator()]
