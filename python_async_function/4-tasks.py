#!/usr/bin/env python3
"""
I Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Perform asynchronous tasks and return sorted list of delays.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay value for each task.

    Returns:
        List[float]: A sorted list of delay values obtained
        from the completed tasks.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
