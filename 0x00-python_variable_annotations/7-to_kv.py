#!/usr/bin/env python3
"""
complex types - string and int/float to tuple
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ create a tuple with the string k and the square of v"""
    return(k, v ** 2.0)
