from typing import *


class Solution:
    # Return all subsets of nums (the power set). Each element is either
    # in a subset or not, so there are 2^n subsets.
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        res = []
        path = []

        def dfs(i):
            if i == len(nums):
                res.append(path[:])
                return
            # skip nums[i]
            dfs(i + 1)
            # take nums[i]
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

        dfs(0)
        return res
