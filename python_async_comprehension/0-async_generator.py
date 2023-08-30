#!/usr/bin/env python3


import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    async def async_random() -> float:
        await asyncio.sleep(1)
        return random.uniform(0, 10)

    tasks = [async_random() for _ in range(10)]
    results = await asyncio.gather(*tasks)
    for result in results:
        yield result


