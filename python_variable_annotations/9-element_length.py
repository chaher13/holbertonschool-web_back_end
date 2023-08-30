#!/usr/bin/env python3
"""
This is an annotation of a function :
    def element_length(lst):
    return [(i, len(i)) for i in lst]
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
