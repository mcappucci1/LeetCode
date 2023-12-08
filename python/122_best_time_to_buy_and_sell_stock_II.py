class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for day in range(1, len(prices)):
            if prices[day] > prices[day-1]:
                profit += prices[day] - prices[day-1]
        return profit