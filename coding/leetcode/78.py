from typing import *


class Solution:
    # Return all subsets of nums (the power set). Each element is either
    # in a subset or not, so there are 2^n subsets.
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        # Iterative: start with the empty subset, and for each number
        # append a copy of every existing subset extended with it.
        res = [[]]
        for x in nums:
            res += [sub + [x] for sub in res]
        return res
