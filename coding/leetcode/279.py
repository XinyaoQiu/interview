from typing import *


class Solution:
    # Idea: find the fewest perfect squares that sum to n.
    # Time: O(n * sqrt(n)), Space: O(n)
    def numSquares(self, n: int) -> int:
        # dp[i] = fewest squares summing to i
        dp = [0] + [float("inf")] * n
        squares = []
        k = 1
        while k * k <= n:
            squares.append(k * k)
            k += 1
        for i in range(1, n + 1):
            for sq in squares:
                if sq > i:
                    break
                dp[i] = min(dp[i], dp[i - sq] + 1)
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    assert s.numSquares(1) == 1
    assert s.numSquares(12) == 3
    assert s.numSquares(13) == 2
    assert s.numSquares(16) == 1
    assert s.numSquares(7) == 4
    assert s.numSquares(10000) == 1
    print("all tests passed")
