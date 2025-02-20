"""
You are given a sorted array that contains unique values, along with an integer target.

If the array contains the target value, return its index.
Otherwise, return the insertion index.
This is the index where the target would be if it were inserted in order, maintaining the sorted sequence of the array.
"""

from typing import List


def find_the_insertion_index(nums: List[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)
