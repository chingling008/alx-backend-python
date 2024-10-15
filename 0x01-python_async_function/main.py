#!/usr/bin/env python3

import asyncio
from importlib import import_module  # Use import_module for dynamic import

async def main():
    """
    Calls the wait_random coroutine multiple times with different max_delay values
    and prints the results using asyncio.run.
    """

    wait_random = import_module('0-basic_async_syntax').wait_random  # Import coroutine

    print(f"Result 1: {await asyncio.run(wait_random())}")
    print(f"Result 2: {await asyncio.run(wait_random(5))}")
    print(f"Result 3: {await asyncio.run(wait_random(15))}")

if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine