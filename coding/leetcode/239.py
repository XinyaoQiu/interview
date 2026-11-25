from typing import *
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Idea: report the maximum of every window of size k.
        # Monotonic deque of indices, values decreasing from front to back.
        if not nums or k <= 0:
            return []
        if k == 1:
            return list(nums)
        k = min(k, len(nums))
        res = []
        dq = deque()
        for i, num in enumerate(nums):
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(i)
            if dq[0] <= i - k:
                dq.popleft()
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res
