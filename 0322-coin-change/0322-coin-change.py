class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_amount = amount + 1
        dp = [max_amount] * max_amount
        dp[0] = 0

        for i in range(1, max_amount):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[-1] if dp[-1] != max_amount else -1

