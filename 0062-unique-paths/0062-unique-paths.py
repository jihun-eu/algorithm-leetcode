class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        if m == 2 or n == 2:
            return max(m, n)
        minimum, maximum = min(m, n), max(m, n)
        
        dp = [num for num in range(1, minimum+1)]
        for _ in range(maximum-2):
            for col in range(1, minimum):
                dp[col] = dp[col] + dp[col-1]

        return dp[-1]