from typing import *
from collections import Counter


class Solution:
    # Return the k most frequent elements of nums.
    # Idea: count occurrences, then group values by frequency (a frequency
    # can be at most len(nums)) and read the buckets from high to low.
    # Time O(n), space O(n).
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []
        counts = Counter(nums)
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


if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert sol.topKFrequent([1], 1) == [1]
    assert sorted(sol.topKFrequent([4, 4, 5, 5, 6], 2)) == [4, 5]
    assert sol.topKFrequent([], 3) == []
    assert sol.topKFrequent([1, 2, 3], 0) == []
    assert sorted(sol.topKFrequent([-1, -1, 0, 0, 0, 7], 1)) == [0]
    assert sorted(sol.topKFrequent([1, 2, 3], 3)) == [1, 2, 3]
    import random
    from collections import Counter as C

    for _ in range(300):
        nums = [random.randint(-5, 5) for _ in range(random.randint(1, 30))]
        cnt = C(nums)
        k = random.randint(1, len(cnt))
        got = sol.topKFrequent(nums, k)
        assert len(got) == k and len(set(got)) == k
        # every returned value must be at least as frequent as any omitted one
        threshold = sorted(cnt.values(), reverse=True)[k - 1]
        assert all(cnt[x] >= threshold for x in got)
    print("all tests passed")
