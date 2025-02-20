"""
You are given an array of numbers, each representing the height of a vertical line on a graph.
A container can be formed with any pair of these lines, along with the x-axis of the graph.
Return the amount of water which the largest container can hold.
"""

from typing import List


def largest_container(heights: List[int]) -> int:
    left = 0
    right = len(heights) - 1
    max_volume = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        current_volume = width * height
        max_volume = max(max_volume, current_volume)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_volume
