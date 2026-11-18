from typing import *


class Solution:
    # Find the smallest positive integer that does not appear in nums.
    # Idea: the answer is in [1, n + 1], so place every value v in 1..n at
    # index v - 1 by swapping, then scan for the first index that is wrong.
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target = nums[i] - 1
                nums[i], nums[target] = nums[target], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
