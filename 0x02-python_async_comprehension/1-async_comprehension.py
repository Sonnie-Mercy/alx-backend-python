#!/usr/bin/env python3
"""
async comprehensions
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collects 10 random numbers using an async comprehensing
    over the async_generator and return the 10
    """
    random_no = [n async for n in async_generator()]
    return random_no
