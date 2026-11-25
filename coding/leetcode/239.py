from typing import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Idea: report the maximum of every window of size k.
        # First version: brute force, take max of each window.
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i + k]))
        return res
