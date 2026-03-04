#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize Server with cached dataset attributes."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return dataset indexed by sorting position starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a deletion-resilient paginated response.

        Args:
            index (int): starting index of the page
            page_size (int): number of items to return

        Returns:
            Dict containing:
                - index: current index
                - next_index: next index to query
                - page_size: number of items returned
                - data: the dataset page
        """
        dataset = self.indexed_dataset()

        assert index is not None and 0 <= index <= max(dataset.keys())

        data = []
        next_index = index

        while len(data) < page_size and next_index <= max(dataset.keys()):
            if next_index in dataset:
                data.append(dataset[next_index])
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
