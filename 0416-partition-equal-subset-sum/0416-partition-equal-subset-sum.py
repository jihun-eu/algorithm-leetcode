class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1: return False
        targetScore = total // 2
        
        dp = [True] + [False] * targetScore
        for num in nums:
            for currScore in range(targetScore, num-1, -1):
                dp[currScore] |= dp[currScore-num]
        
        return dp[-1]