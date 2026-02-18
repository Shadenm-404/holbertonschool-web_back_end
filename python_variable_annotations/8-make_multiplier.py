#!/usr/bin/env python3
"""
This module contains a function that creates a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier.
    """
    def multiply(number: float) -> float:
        return number * multiplier
    return multiply
