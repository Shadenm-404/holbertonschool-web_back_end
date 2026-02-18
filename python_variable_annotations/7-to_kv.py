#!/usr/bin/env python3
"""
This module contains a function that returns a key-value tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string and the square of the value.
    """
    return (k, float(v * v))
