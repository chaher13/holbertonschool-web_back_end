#!/usr/bin/env python3
"""
This is a type-annotated function sum_list
which takes a list input_list of floats as argument
and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of all the floats in the input_list.

    Example:
        >>> input_list = [1.5, 2.3, 3.7]
        >>> result = sum_list(input_list)
        >>> print(result)
        7.5
    """
    result: float = 0.0
    for input in input_list:
        result += input
    return result
