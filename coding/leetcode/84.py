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
    assert sol.largestRectangleArea([]) == 0
    assert sol.largestRectangleArea([0]) == 0
    assert sol.largestRectangleArea([5, 5, 5, 5]) == 20
    assert sol.largestRectangleArea([1, 2, 3, 4, 5]) == 9
    assert sol.largestRectangleArea([5, 4, 3, 2, 1]) == 9
    assert sol.largestRectangleArea([2, 0, 2]) == 2
    import random
    for _ in range(300):
        arr = [random.randint(0, 9) for _ in range(random.randint(1, 12))]
        expected = max(
            min(arr[i:j + 1]) * (j - i + 1)
            for i in range(len(arr))
            for j in range(i, len(arr))
        )
        assert sol.largestRectangleArea(arr) == expected, arr
    print("all tests passed")
