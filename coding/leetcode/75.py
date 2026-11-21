from typing import *


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Idea: values are only 0, 1, 2, so no general sort is needed.
        Dutch national flag: keep three regions, [0, low) is 0s,
        [low, mid) is 1s, (high, end] is 2s, and [mid, high] is unknown.
        A 2 is swapped to the back without advancing mid, since the value
        swapped in is unseen.
        Time: O(n), single pass. Space: O(1).
        """
        if len(nums) < 2:
            return
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
