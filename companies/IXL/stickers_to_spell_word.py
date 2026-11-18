def to_counts(stickers):
    counts = []
    for s in stickers:
        arr = [0] * 26
        for ch in s:
            arr[ord(ch) - 97] += 1
        counts.append(arr)
    return counts


def min_stickers(stickers, target):
    n = len(target)
    t = [ord(c) - 97 for c in target]
    counts = to_counts(stickers)
    full = (1 << n) - 1
    memo = {full: 0}

    def dfs(mask):
        if mask in memo:
            return memo[mask]
        first = 0
        while mask >> first & 1:
            first += 1
        res = n + 1
        for base in counts:
            if not base[t[first]]:
                continue
            cnt = base[:]
            nxt = mask
            for i in range(first, n):
                k = t[i]
                if not (mask >> i & 1) and cnt[k]:
                    cnt[k] -= 1
                    nxt |= 1 << i
            res = min(res, dfs(nxt) + 1)
        memo[mask] = res
        return res

    ans = dfs(0)
    return ans if ans <= n else -1


# follow-up: each sticker has a cost, unlimited copies
def min_cost(stickers, costs, target):
    n = len(target)
    t = [ord(c) - 97 for c in target]
    counts = to_counts(stickers)
    full = (1 << n) - 1
    INF = float("inf")
    memo = {full: 0}

    def dfs(mask):
        if mask in memo:
            return memo[mask]
        first = 0
        while mask >> first & 1:
            first += 1
        res = INF
        for base, cost in zip(counts, costs):
            if not base[t[first]]:
                continue
            cnt = base[:]
            nxt = mask
            for i in range(first, n):
                k = t[i]
                if not (mask >> i & 1) and cnt[k]:
                    cnt[k] -= 1
                    nxt |= 1 << i
            res = min(res, dfs(nxt) + cost)
        memo[mask] = res
        return res

    ans = dfs(0)
    return ans if ans < INF else -1


# follow-up: each sticker has a cost, usable at most once (0/1 knapsack)
def min_cost_once(stickers, costs, target):
    n = len(target)
    t = [ord(c) - 97 for c in target]
    counts = to_counts(stickers)
    full = (1 << n) - 1
    INF = float("inf")
    dp = [INF] * (1 << n)
    dp[0] = 0
    for base, cost in zip(counts, costs):
        for mask in range(full, -1, -1):
            if dp[mask] == INF:
                continue
            cnt = base[:]
            nxt = mask
            for i in range(n):
                k = t[i]
                if not (mask >> i & 1) and cnt[k]:
                    cnt[k] -= 1
                    nxt |= 1 << i
            dp[nxt] = min(dp[nxt], dp[mask] + cost)
    return dp[full] if dp[full] < INF else -1


print(min_stickers(["with", "example", "science"], "thehat"))
print(min_stickers(["notice", "possible"], "basicbasic"))
print(min_stickers(["a"], "aaa"))

print(min_cost(["ab", "a", "b"], [10, 3, 3], "ab"))
print(min_cost(["ab", "a", "b"], [5, 3, 3], "ab"))
print(min_cost(["a"], [2], "aaa"))
print(min_cost(["x"], [1], "a"))

print(min_cost_once(["a"], [2], "aaa"))
print(min_cost_once(["a", "aa", "aaa"], [1, 5, 10], "aaa"))
print(min_cost_once(["ab", "a", "b"], [10, 3, 3], "ab"))
