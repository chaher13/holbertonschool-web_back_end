#!/usr/bin/env python 3

"""
This is a type-annotated function sum_list
which takes a list input_list of floats as argument
and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    result: float = 0.0
    for input in input_list:
        result += input
    return result
