"""
Determine the number of distinct ways to climb a staircase of n steps by taking either 1 or 2 steps at a time.
"""


def climbing_stairs(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    step1, step2 = 1, 2

    for i in range(3, n + 1):
        current = step1 + step2
        step1 = step2
        step2 = current

    return step2
