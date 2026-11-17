from typing import *


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Idea: find the rightmost ascent, swap with the next larger value
        on its right, then reverse the suffix.
        """
        n = len(nums)
        if n < 2:
            return
        i = n - 2
        # find the rightmost index i with nums[i] < nums[i + 1]
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            # find the rightmost value larger than nums[i] and swap
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # suffix is in descending order, reverse it to ascending
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
