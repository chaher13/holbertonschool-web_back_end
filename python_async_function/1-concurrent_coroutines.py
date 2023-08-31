#!/usr/bin/env python3
"""
Import wait_random from the previous python file
that you’ve written and write an async routine called wait_n
that takes in 2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without using sort()
because of concurrency.
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously executes `n` tasks with a maximum delay
    of `max_delay` and returns a sorted list of the delays.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A sorted list of floats representing
        the delays of the completed tasks.

    Example Usage:
        delays = await wait_n(3, 5)
        print(delays)
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
