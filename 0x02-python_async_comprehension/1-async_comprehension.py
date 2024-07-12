#!/usr/bin/env python3
"""Coroutine that collects 10 random numbers from
   async_generator using async comprehensions.
   """

from importlib import import_module
import asyncio

async_generator = import_module('0-async-generator').async_generator


async def async_comprehension():
    return [i async for i in async_generator()]
