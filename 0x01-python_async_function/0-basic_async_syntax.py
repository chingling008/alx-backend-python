#!/usr/bin/python3
import random

async def wait_random(max_delay=10):
    """
    Waits for a random amount of time between 0 and max_delay (inclusive) seconds
    using asyncio.sleep and returns the actual delay.

    Args:
        max_delay (int, optional): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay that the coroutine waited for.
    """

    delay = random.uniform(0, max_delay)  # Generate random delay
    await asyncio.sleep(delay)  # Pause for the random delay
    return delay                 # Return the actual delay