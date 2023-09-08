#!/usr/bin/env python3
"""
This is a function named index_range
that takes two integer arguments page and page_size.

The function should return a tuple of size two containing
a start index and an end index corresponding to the range of indexes
to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""


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
