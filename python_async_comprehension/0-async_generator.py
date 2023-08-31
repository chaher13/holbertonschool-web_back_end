#!/usr/bin/env python3
"""
this is a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times,
each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields random floating-point numbers.

    Returns:
        Generator[float, None, None]: A generator
        that yields random floating-point numbers.
    """
    async def async_random() -> float:
        await asyncio.sleep(1)
        return random.uniform(0, 10)

    tasks = [async_random() for _ in range(10)]
    results = await asyncio.gather(*tasks)
    for result in results:
        yield result
