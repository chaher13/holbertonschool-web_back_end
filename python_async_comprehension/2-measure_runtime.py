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
    """
    An asynchronous generator that yields random floating-point numbers
    between 0 and 10.

    Yields:
        float: A random floating-point number between 0 and 10.

    Example Usage:
        async def example_usage():
            async for number in async_generator():
                print(number)

        asyncio.run(example_usage())

    Code Analysis:
        Inputs:
            None

        Flow:
            1. The function starts a loop that will iterate 10 times.
            2. Inside the loop, it awaits a 1-second delay
            using `asyncio.sleep`.
            3. After the delay, it yields a random floating-point number
            between 0 and 10 using `random.uniform`.
            4. The loop repeats until it has iterated 10 times.

        Outputs:
            A sequence of 10 random floating-point numbers between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension() -> List[float]:
    """
    Generate a list of random floating-point numbers between 0 and 10
    using an asynchronous generator.

    Returns:
        List[float]: A list of 10 random floating-point numbers
        between 0 and 10.
    """
    result = [x async for x in async_generator()]
    return result


async def measure_runtime() -> float:
    """
    Measures the total runtime of four instances of the async_comprehension
    function executed concurrently using asyncio.gather().

    Returns:
    float: The total runtime of executing four instances
    of the async_comprehension function concurrently.
    """
    began = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    finish = asyncio.get_event_loop().time()
    total = finish - began
    return total
