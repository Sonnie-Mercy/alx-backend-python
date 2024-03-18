#!/usr/bin/env python3
"""
tasks task_wait_n
"""
import asyncio
import random
from typing import List


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawning wait_random n times with the specified max_delay
    """
    float_values: List = []
    delays: List[float] = []
    for _ in range(n):
        float_values.append(task_wait_random(max_delay))

    for float_value in asyncio.as_completed(float_values):
        delays.append(await float_value)
    return delays
