from typing import *


class Solution:
    # Find the smallest positive integer that does not appear in nums.
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)
        answer = 1
        while answer in seen:
            answer += 1
        return answer
