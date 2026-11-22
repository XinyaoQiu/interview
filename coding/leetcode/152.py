from typing import *


class Solution:
    # Find the contiguous subarray with the largest product.
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        best = nums[0]
        for i in range(len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                best = max(best, prod)
        return best
