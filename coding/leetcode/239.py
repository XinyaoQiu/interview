from typing import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Idea: report the maximum of every window of size k.
        # First version: brute force, take max of each window.
        if not nums or k <= 0:
            return []
        if k == 1:
            return list(nums)
        k = min(k, len(nums))
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i + k]))
        return res
