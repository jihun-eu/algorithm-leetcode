class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum & 1:
            return False

        targetNum = totalSum // 2

        dp = [True] + [False] * targetNum
        for num in nums:
            for currNum in range(targetNum, num-1, -1):
                dp[currNum] |= dp[currNum-num]

        return dp[-1]