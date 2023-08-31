#!/usr/bin/env python3
""" This a type-annotated function concat
that takes a string str1 and a string str2 as arguments
and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two input strings and returns the result.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: The concatenated string of str1 and str2.
    """
    return str1 + str2
