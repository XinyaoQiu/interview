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


if __name__ == "__main__":
    def norm(r):
        return sorted(sorted(s) for s in r)

    cases = [
        ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        ([0], [[], [0]]),
        ([], [[]]),
        ([-1, 5], [[], [-1], [5], [-1, 5]]),
    ]
    for nums, want in cases:
        got = Solution().subsets(nums)
        assert norm(got) == norm(want), (nums, got)
    assert len(Solution().subsets(list(range(10)))) == 2 ** 10
    print("all tests passed")
