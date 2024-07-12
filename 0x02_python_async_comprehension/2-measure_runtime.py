#!/usr/bin/env python3

import asyncio
import time
from importlib import import_module


async_comprehension = import_module(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime():
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
