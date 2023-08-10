class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        best_profit = 0
        cheapest_day = prices[0]

        for i in range(1, len(prices)):
            cheapest_day = min(cheapest_day, prices[i])
            best_profit = max(best_profit, prices[i] - cheapest_day)

        return best_profit