class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        cheapestPrice = prices[0]
        for price in prices[1:]:
            cheapestPrice = min(cheapestPrice, price)
            profit = max(profit, price - cheapestPrice)
        
        return profit

