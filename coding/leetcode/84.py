from typing import *


class Solution:
    # Find the largest rectangle that fits inside a histogram.
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        # brute force: for every bar, expand left and right while bars are >= it
        best = 0
        for i in range(len(heights)):
            left = i
            while left > 0 and heights[left - 1] >= heights[i]:
                left -= 1
            right = i
            while right < len(heights) - 1 and heights[right + 1] >= heights[i]:
                right += 1
            best = max(best, heights[i] * (right - left + 1))
        return best
