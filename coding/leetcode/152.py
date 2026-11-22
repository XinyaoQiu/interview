from typing import *


class Solution:
    # Find the contiguous subarray with the largest product.
    # Track both max and min product ending here, since a negative
    # number can turn the min into the max.
    # Time: O(n), Space: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur_max = cur_min = best = nums[0]
        for x in nums[1:]:
            options = (x, cur_max * x, cur_min * x)
            cur_max = max(options)
            cur_min = min(options)
            best = max(best, cur_max)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.maxProduct([2, 3, -2, 4]) == 6
    assert s.maxProduct([-2, 0, -1]) == 0
    assert s.maxProduct([-2]) == -2
    assert s.maxProduct([0]) == 0
    assert s.maxProduct([-2, 3, -4]) == 24
    assert s.maxProduct([0, 2]) == 2
    assert s.maxProduct([-1, -2, -3, 0, 5]) == 6
    assert s.maxProduct([2, -5, -2, -4, 3]) == 24
    print("basic tests passed")
