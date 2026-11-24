from typing import *


class Solution:
    # Return all subsets of nums (the power set). Each element is either
    # in a subset or not, so there are 2^n subsets.
    # Time: O(n * 2^n) to build all subsets. Space: O(n * 2^n) for the output.
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        # Iterative: start with the empty subset, and for each number
        # append a copy of every existing subset extended with it.
        res = [[]]
        for num in nums:
            res += [subset + [num] for subset in res]
        return res
