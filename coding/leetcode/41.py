from typing import *


class Solution:
    # Find the smallest positive integer that does not appear in nums.
    # Idea: the answer is in [1, n + 1], so place every value v in 1..n at
    # index v - 1 by swapping, then scan for the first index that is wrong.
    # Time: O(n), each swap puts one value in its final spot.
    # Space: O(1) extra, the input array is reused as the hash table.
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


if __name__ == "__main__":
    solution = Solution()
    cases = [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([1], 2),
        ([2], 1),
        ([1, 1], 2),
        ([2, 2, 1, 1], 3),
        ([-1, -2, 0], 1),
        ([1, 2, 3, 4, 5], 6),
    ]
    for nums, expected in cases:
        result = solution.firstMissingPositive(list(nums))
        assert result == expected, (nums, result, expected)
    print("all tests passed")
