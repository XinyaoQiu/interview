from typing import *


class Solution:
    # Return the k most frequent elements of nums.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []
        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1
        # bucket sort: buckets[f] holds the values that appear exactly f times
        buckets = [[] for _ in range(len(nums) + 1)]
        for x, f in counts.items():
            buckets[f].append(x)
        result = []
        for f in range(len(nums), 0, -1):
            for x in buckets[f]:
                result.append(x)
                if len(result) == k:
                    return result
        return result
