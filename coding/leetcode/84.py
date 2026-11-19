from typing import *


class Solution:
    # Find the largest rectangle that fits inside a histogram.
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        # monotonic stack of (start index, height) with increasing heights
        stack = []
        best = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                best = max(best, height * (i - idx))
                start = idx
            stack.append((start, h))
        for idx, height in stack:
            best = max(best, height * (len(heights) - idx))
        return best
