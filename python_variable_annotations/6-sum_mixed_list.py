#!/usr/bin/env python3
"""
This is a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers
and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of all the integers and floats in the input list.

    Example:
        >>> mxd_lst = [1, 2.5, 3, 4.2]
        >>> result = sum_mixed_list(mxd_lst)
        >>> print(result)
        10.7
    """
    result: float = 0.0
    for mxd in mxd_lst:
        result += mxd
    return result
