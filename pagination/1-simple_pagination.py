#!/usr/bin/env python3
"""
from index_range of the previous task, implement :
a method named get_page that takes two integer arguments page
with default value 1 and page_size with default value 10.

You have to use this CSV file
Use assert to verify that both arguments are integers greater than 0.
Use index_range to find the correct indexes to paginate the dataset correctly
and return the appropriate page of the dataset (i.e. the correct list of rows).
If the input arguments are out of range for the dataset,
an empty list should be returned.

"""
import csv
from typing import List


class Server:
    """
    A class that manages a dataset stored in a CSV file and provides methods to retrieve specific pages of data.

    Attributes:
        DATA_FILE (str): The path to the CSV file containing the dataset.
        __dataset (List[List]): The dataset retrieved from the CSV file.

    Methods:
        __init__: Initializes the Server class and sets the dataset to None.
        dataset: Retrieves the dataset from the CSV file and caches it for future use.
        get_page: Retrieves the specified page of data from the dataset based on the given page number and page size.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes the Server class.

        Args:
            None

        Returns:
            None
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Retrieves the dataset from the CSV file and caches it for future use.

        Args:
            None

        Returns:
            List[List]: The dataset retrieved from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves the specified page of data from the dataset based on the given page number and page size.

        Args:
            page (int): The page number to retrieve (default is 1).
            page_size (int): The number of rows per page (default is 10).

        Returns:
            List[List]: The data of the specified page from the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        total_rows = len(dataset)

        start_index, end_index = index_range(page, page_size)

        if start_index >= total_rows:
            return []

        page_data = dataset[start_index:end_index]

        return page_data
