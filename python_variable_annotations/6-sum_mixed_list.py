#!/usr/bin/env python3
"""
This module contains a function that sums a mixed list of ints and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a mixed list as a float.
    """
    return float(sum(mxd_lst))
