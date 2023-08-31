#!/usr/bin/env python3
"""
This is a type-annotated function to_kv
that takes a string k and an int OR float v as arguments
and returns a tuple. The first element of the tuple is the string k.
The second element is the square of the int/float v
and should be annotated as a float.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the first element as the string `k`
    and the second element as the square of `v` (annotated as a `float`).

    Args:
        k (str): The key as a string.
        v (int or float): The value as an `int` or `float`.

    Returns:
        Tuple[str, float]: The tuple containing the string `k`
        and the square of `v` as a `float`.
    """
    return k, v ** 2
