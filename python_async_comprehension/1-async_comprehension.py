#!/usr/bin/env python3
"""
This module collects values using async comprehension.
"""

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """
    Collects 10 random numbers from async_generator.
    """
    return [i async for i in async_generator()]
