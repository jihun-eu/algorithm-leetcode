class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_price = prices[0]

        for price in prices[1:]:
            curr_price = min(curr_price, price)
            max_profit = max(max_profit, price - curr_price)

        return max_profit