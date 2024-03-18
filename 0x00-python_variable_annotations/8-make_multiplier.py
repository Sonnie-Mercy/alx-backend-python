#!/usr/bin/env python3
"""complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a function that multiplies float by multiplier"""
    def func(x: float) -> float:
        """this is the function to use multiplier on"""
        return x * multiplier
    return func
