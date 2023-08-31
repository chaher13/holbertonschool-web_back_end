#!/usr/bin/env python3
"""
    This is  a type-annotated function floor
    which takes a float n as argument
    and returns the floor of the float.
"""
import math


def floor(n: float) -> int:
    """
    Returns the largest integer less than or equal to the input float.

    Args:
        n (float): The input float number.

    Returns:
        int: The largest integer less than or equal to the input float `n`.
    """
    return math.floor(n)
