#!/usr/bin/env python3
"""
Import wait_random from the previous python file that you’ve written
and write an async routine called wait_n
that takes in 2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without using sort()
because of concurrency.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that generates a random delay and waits
    for that amount of time before returning the delay value.

    :param max_delay: An integer representing the maximum delay in seconds.
    Defaults to 10 if not provided.
    :return: A float value representing the delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
