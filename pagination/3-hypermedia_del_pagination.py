#!/usr/bin/env python3
"""
Module implementing deletion-resilient hypermedia pagination for a dataset
of popular baby names.
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class used to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with cached dataset attributes."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Return the cached dataset loaded from the CSV file.
        The dataset excludes the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                data = [row for row in reader]
            self.__dataset = data[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Return the dataset indexed by position starting at index 0.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: truncated_dataset[i] for i in range(len(truncated_dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """
        Return a deletion-resilient paginated response.

        Args:
            index (int): Starting index of the page.
            page_size (int): Number of items to return.

        Returns:
            Dict: A dictionary containing:
                - index: the starting index of the page
                - data: the list of returned rows
                - page_size: number of items returned
                - next_index: the next index to query
        """
        if index is None:
            index = 0

        dataset = self.indexed_dataset()

        assert index >= 0 and index <= max(dataset.keys())

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
