#!/usr/bin/env python3
"""
This is a type-annotated function make_multiplier
that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ """
    def called_multiplier(n: float) -> float:
        return n * multiplier
    return called_multiplier
