#!/usr/bin/env python3
"""
Import async_comprehension from the previous file
and write a measure_runtime coroutine
that will execute async_comprehension four times
in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.
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


async def measure_runtime() -> float:
    began = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    finish = asyncio.get_event_loop().time()
    result = finish - began
    return result
