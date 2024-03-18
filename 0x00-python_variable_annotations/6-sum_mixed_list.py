#!/usr/bin/env python3
"""
complex types -mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a mixed list of ints and floats and returns their sum as a float"""
    return sum(mxd_lst)
