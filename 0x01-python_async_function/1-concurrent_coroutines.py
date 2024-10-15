#!/usr/bin/env python3
"""Task 1's module."""

import asyncio
import random

async def wait_n(n: int, max_delay: int = 10) -> list[float]:
    """Waits for n random delays and returns the results in ascending order."""

    wait_random = __import__('0-basic_async_syntax').wait_random
    tasks = [wait_random(max_delay) for _ in range(n)]  # Create tasks
    results = await asyncio.gather(*tasks)  # Gather results
    return sorted(results)  # Sort results in ascending order
