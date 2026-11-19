from typing import *


class Solution:
    # Find the largest rectangle that fits inside a histogram.
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        # Idea: each popped bar can extend left back to the start of the popped
        # range and right up to the current index.
        # Time O(n): every bar is pushed and popped once. Space O(n) for the stack.
        # monotonic stack of (start index, height) with increasing heights
        stack = []
        best = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                start_idx, height = stack.pop()
                best = max(best, height * (i - start_idx))
                start = start_idx
            stack.append((start, h))
        n = len(heights)
        for start_idx, height in stack:
            best = max(best, height * (n - start_idx))
        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert sol.largestRectangleArea([2, 4]) == 4
    assert sol.largestRectangleArea([1]) == 1
    print("all tests passed")
