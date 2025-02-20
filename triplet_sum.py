"""
Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0. 
The solution must not contain duplicate triplets (e.g., [1, 2, 3] and [2, 3, 1] are considered duplicates).
If no such triplets are found, return an empty array.
Each triplet can be arranged in any order, and the output can be returned in any order.
"""

from typing import List


def triplet_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    triplets = []
    length = len(nums)

    for i in range(length - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, length - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return triplets
