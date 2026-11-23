from typing import *


class Solution:
    # Idea: match s against pattern p where '.' matches any char and
    # 'x*' matches zero or more of x.
    # Time: O(m * n) states, each computed in O(1).
    # Space: O(m * n) for the memo plus recursion depth.
    # For 'x*' we either skip the pair (zero copies) or consume one char of s
    # when it matches x and stay on the same pattern position.
    def isMatch(self, s: str, p: str) -> bool:
        # Top-down DP: memoize match(i, j) = does s[i:] match p[j:].
        memo = {}

        def match(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                res = i == len(s)
            else:
                first = i < len(s) and p[j] in (s[i], ".")
                if j + 1 < len(p) and p[j + 1] == "*":
                    res = match(i, j + 2) or (first and match(i + 1, j))
                else:
                    res = first and match(i + 1, j + 1)
            memo[(i, j)] = res
            return res

        return match(0, 0)
