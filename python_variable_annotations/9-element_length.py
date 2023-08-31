#!/usr/bin/env python3
"""
This is an annotation of a function :
    def element_length(lst):
    return [(i, len(i)) for i in lst]
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an element
    from the input list and its corresponding length.

    Args:
        lst (Iterable[Sequence]): A list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
        where each tuple contains an element
        from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
