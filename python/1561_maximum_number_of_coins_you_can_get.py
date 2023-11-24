class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        total = 0
        n = len(piles)
        piles.sort()
        for i in range(n // 3):
            total += piles[n - (2 * i) - 2]
        return total