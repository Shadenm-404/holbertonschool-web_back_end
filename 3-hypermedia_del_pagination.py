#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

import csv
from typing import Dict, List, Optional


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset: Optional[List[List]] = None
        self.__indexed_dataset: Optional[Dict[int, List]] = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE, newline="") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """
        Return deletion-resilient hypermedia pagination.

        Args:
            index (int): Start index of the current page (0-indexed).
            page_size (int): Number of items to return.

        Returns:
            Dict: Contains index, next_index, page_size and data.
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed = self.indexed_dataset()
        max_index = max(indexed.keys()) if indexed else 0
        assert index <= max_index

        data: List[List] = []
        current = index

        while len(data) < page_size and current <= max_index:
            row = indexed.get(current)
            if row is not None:
                data.append(row)
            current += 1

        return {
            "index": index,
            "next_index": current,
            "page_size": len(data),
            "data": data,
        }
