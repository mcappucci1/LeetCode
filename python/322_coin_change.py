class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [0] + [math.inf] * amount
        for i in range(amount):
            if memo[i] == math.inf:
                continue
            for coin in coins:
                if coin + i < amount + 1:
                    memo[coin + i] = min(memo[coin + i], memo[i] + 1)
        return -1 if memo[-1] == math.inf else memo[-1]