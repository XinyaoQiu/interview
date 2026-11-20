from typing import *


class Solution:
    # Return the k most frequent elements of nums.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1
        # brute force: sort all distinct values by frequency
        ordered = sorted(counts, key=lambda x: counts[x], reverse=True)
        return ordered[:k]
