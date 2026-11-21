from typing import *


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Idea: values are only 0, 1, 2, so no general sort is needed.
        Dutch national flag: keep three regions, [0, zero_end) is 0s,
        [zero_end, i) is 1s, (two_start, end] is 2s, and [i, two_start] is unknown.
        A 2 is swapped to the back without advancing i, since the value
        swapped in is unseen.
        Time: O(n), single pass. Space: O(1).
        """
        if len(nums) < 2:
            return
        zero_end, i, two_start = 0, 0, len(nums) - 1
        while i <= two_start:
            if nums[i] == 0:
                nums[zero_end], nums[i] = nums[i], nums[zero_end]
                zero_end += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[two_start] = nums[two_start], nums[i]
                two_start -= 1


if __name__ == "__main__":
    s = Solution()
    for arr, want in [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([], []),
        ([1, 1, 1], [1, 1, 1]),
        ([2, 2, 1, 1, 0, 0], [0, 0, 1, 1, 2, 2]),
        ([1, 0], [0, 1]),
        ([2, 1], [1, 2]),
    ]:
        s.sortColors(arr)
        assert arr == want, (arr, want)
    print("all tests passed")
