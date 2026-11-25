from typing import *
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Idea: report the maximum of every window of size k.
        # Approach: keep a deque of indices whose values are decreasing, so the
        # front always holds the index of the current window maximum.
        # - pop from the back while the new value is >= the back value
        # - pop from the front when its index has left the window
        # Time: O(n), each index is pushed and popped at most once.
        # Space: O(k) for the deque (plus O(n) for the output).
        if not nums or k <= 0:
            return []
        if k == 1:
            return list(nums)
        k = min(k, len(nums))
        res = []
        window = deque()  # indices of candidate maxima
        for i, num in enumerate(nums):
            while window and nums[window[-1]] <= num:
                window.pop()
            window.append(i)
            if window[0] <= i - k:
                window.popleft()
            if i >= k - 1:
                res.append(nums[window[0]])
        return res


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sol.maxSlidingWindow([1], 1) == [1]
    assert sol.maxSlidingWindow([1, -1], 1) == [1, -1]
    assert sol.maxSlidingWindow([9, 11], 2) == [11]
    assert sol.maxSlidingWindow([4, -2], 2) == [4]
    assert sol.maxSlidingWindow([5, 5, 5, 5], 2) == [5, 5, 5]
    assert sol.maxSlidingWindow([7, 6, 5, 4, 3], 3) == [7, 6, 5]
    assert sol.maxSlidingWindow([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    print("all tests passed")
