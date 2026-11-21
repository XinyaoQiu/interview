from typing import *


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Idea: values are only 0, 1, 2, so no general sort is needed.
        """
        if len(nums) < 2:
            return
        counts = [0, 0, 0]
        for x in nums:
            counts[x] += 1
        i = 0
        for color in range(3):
            for _ in range(counts[color]):
                nums[i] = color
                i += 1
