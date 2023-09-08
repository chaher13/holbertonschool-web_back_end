#!/usr/bin/env python3
"""
The goal here is that if between two queries, certain rows are removed
from the dataset, the user does not miss items from dataset when changing page
with code provided implement:
a get_hyper_index method with two integer arguments:
index with a None default value and page_size with default value of 10.

The method should return a dictionary with the following key-value pairs:
index: the current start index of the return page.
That is the index of the first item in the current page.
For example if requesting page 3 with page_size 20, and no data was removed
from the dataset, the current index should be 60.
next_index: the next index to query with.
That should be the index of the first item
after the last item on the current page.
page_size: the current page size
data: the actual page of the dataset
Requirements/Behavior:

Use assert to verify that index is in a valid range.
If the user queries index 0, page_size 10,
they will get rows indexed 0 to 9 included.
If they request the next index (10)
with page_size 10, but rows 3, 6 and 7 were deleted,
the user should still receive rows indexed 10 to 19 included.
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Returns a tuple containing the start and end indexes
    for a given pagination range.

    Args:
        page (int): The page number for which
        the index range is to be calculated.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indexes
        for the given pagination parameters.
        If either `page` or `page_size` is less than 1, returns None.

    Example:
        start_index, end_index = index_range(2, 10)
        print(start_index)  # Output: 10
        print(end_index)  # Output: 20
    """
    if page < 1 or page_size < 1:
        return None
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """
    A class that manages a dataset and provides methods
    for retrieving data in a paginated manner.

    Attributes:
        DATA_FILE (str): The filename of the CSV file containing the dataset.

    Methods:
        dataset() -> List[List]: Returns the dataset stored in the class.
        get_page(page: int = 1, page_size: int = 10) -> List[List]:
        Retrieves a specific page of data from the dataset.
        get_hyper(page: int = 1, page_size: int = 10) -> dict:
        Returns information about the requested page
        and hyperlinks for pagination.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes the Server class.

        Args:
            None

        Returns:
            None

        Summary:
            The __init__ method initializes the Server class
            by setting the __dataset attribute to None.

        Example Usage:
            server = Server()

        Code Analysis:
            Inputs:
                - None

            Flow:
                1. The __init__ method is called
                when a new instance of the Server class is created.
                2. It sets the __dataset attribute to None,
                indicating that the dataset has not been loaded yet.

            Outputs:
                - None
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Returns the dataset stored in the class.
        If the dataset is not yet loaded, it reads the data
        from the CSV file and stores it.

        Returns:
            List[List]: The dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from the dataset
        based on the given page number and page size.

        Args:
            page (int): The page number to retrieve (default is 1).
            page_size (int): The number of rows per page (default is 10).

        Returns:
            List[List]: The data for the requested page.
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dictionary containing information
        about the requested page and hyperlinks for pagination.

        Args:
            page (int): The page number to retrieve (default is 1).
            page_size (int): The number of rows per page (default is 10).

        Returns:
            dict: A dictionary containing information about the
              requested page and hyperlinks for pagination.
        """
        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        nxt_page = page + 1 if page * page_size < len(self.dataset()) else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": nxt_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
