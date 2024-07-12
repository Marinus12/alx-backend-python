#!/usr/bin/env python3
from importlib import import_module
import asyncio

async_generator = import_module('0-async_generator').async_generator


async def async_comprehension():
    return [i async for i in async_generator()]
