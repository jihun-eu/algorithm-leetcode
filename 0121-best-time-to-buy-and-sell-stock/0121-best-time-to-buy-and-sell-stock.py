class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        length = len(prices)
        for i in range(length-1, 0, -1):
            if prices[i] <= max_profit:
                continue
            for j in range(i-1, -1, -1):
                max_profit = max(max_profit, prices[i] - prices[j])
        return max_profit