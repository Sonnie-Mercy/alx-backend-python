#!/usr/bin/env python3
"""
executing multiple coroutines at the same time with async
"""
import asyncio
import random
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawning wait_random n times with the specified max_delay
    """
    float_values: List = []
    delays: List[float] = []
    for _ in range(n):
        float_values.append(wait_random(max_delay))

    for float_value in asyncio.as_completed(float_values):
        delays.append(await float_value)
    return delays
