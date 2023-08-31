#!/usr/bin/env python3
"""
Import async_generator from the previous task
and then write a coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers
using an async comprehensing over async_generator,
then return the 10 random numbers.
"""

import asyncio
import random
from typing import Generator, List


async def async_generator() -> Generator[float, None, None]:
    async def async_random() -> float:
        await asyncio.sleep(1)
        return random.uniform(0, 10)

    tasks = [async_random() for _ in range(10)]
    results = await asyncio.gather(*tasks)
    for result in results:
        yield result

async def async_comprehension() -> List[float]:
    result = [x async for x in async_generator()]
    return result

