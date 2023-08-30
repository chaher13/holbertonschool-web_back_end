#!/usr/bin/env python3
"""
This is a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers
and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:

    result: float = 0.0
    for mxd in mxd_lst:
        result += mxd
    return result
