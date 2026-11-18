def change(amount, coins):
    dp = [1] + [0] * amount
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]


# follow-up: limited count per coin, top-down memo on (coin index, remaining)
def change_limited_dfs(amount, counts):
    items = list(counts.items())
    memo = {}

    def dfs(i, rem):
        if rem == 0:
            return 1
        if i == len(items):
            return 0
        if (i, rem) in memo:
            return memo[(i, rem)]
        coin, cnt = items[i]
        total = 0
        for k in range(cnt + 1):
            if k * coin > rem:
                break
            total += dfs(i + 1, rem - k * coin)
        memo[(i, rem)] = total
        return total

    return dfs(0, amount)


# follow-up: bottom-up, O(types * amount * count)
def change_limited_dp(amount, counts):
    dp = [1] + [0] * amount
    for coin, cnt in counts.items():
        for a in range(amount, -1, -1):
            k = 1
            while k <= cnt and k * coin <= a:
                dp[a] += dp[a - k * coin]
                k += 1
    return dp[amount]


# follow-up: sliding window, O(types * amount)
def change_limited_fast(amount, counts):
    dp = [1] + [0] * amount
    for coin, cnt in counts.items():
        new = dp[:]
        for a in range(coin, amount + 1):
            new[a] += new[a - coin]
            if a - (cnt + 1) * coin >= 0:
                new[a] -= dp[a - (cnt + 1) * coin]
        dp = new
    return dp[amount]


print(change(5, [1, 2, 5]))
print(change(3, [2]))
print(change(0, [7]))

limits = {1: 2, 2: 3, 5: 1}
print(change_limited_dfs(5, limits), change_limited_dp(5, limits), change_limited_fast(5, limits))
print(change_limited_dfs(0, limits), change_limited_dp(0, limits), change_limited_fast(0, limits))
print(change_limited_dfs(13, limits), change_limited_dp(13, limits), change_limited_fast(13, limits))
print(change_limited_dfs(14, limits), change_limited_dp(14, limits), change_limited_fast(14, limits))
print(change_limited_dfs(4, {1: 4}), change_limited_dp(4, {1: 4}), change_limited_fast(4, {1: 4}))
print(change_limited_dfs(5, {1: 4}), change_limited_dp(5, {1: 4}), change_limited_fast(5, {1: 4}))
