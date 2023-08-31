#!/usr/bin/env python3
"""
This is  a type-annotated function to_str
that takes a float n as argument
and returns the string representation of the float.
"""


def to_str(n: float) -> str:
    """
    Convert a float to its string representation.

    Args:
        n (float): The input float number.

    Returns:
        str: The string representation of the input float `n`.

    Example:
        >>> result = to_str(3.14)
        >>> print(result)
        "3.14"
    """
    return str(n)
