#!/usr/bin/env python3
"""
This is a type-annotated function make_multiplier
that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function called 'called_multiplier'
    that multiplies a float number by the provided multiplier.

    Args:
        multiplier (float): The multiplier value to be used.

    Returns:
        called_multiplier (function):
        A function that takes a float number as an argument
        and multiplies it by the multiplier value.

    Example:
        # Create a function that multiplies numbers by 2
        multiply_by_2 = make_multiplier(2)

        # Use the created function to multiply a number by 2
        result = multiply_by_2(5)
        print(result)  # Output: 10
    """
    def called_multiplier(n: float) -> float:
        return n * multiplier
    return called_multiplier
