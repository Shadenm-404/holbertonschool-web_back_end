#!/usr/bin/env python3
"""
Module that provides a helper function for pagination.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return start and end index for pagination.

    Args:
        page (int): Page number (1-indexed)
        page_size (int): Number of items per page

    Returns:
        Tuple[int, int]: start index and end index
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
