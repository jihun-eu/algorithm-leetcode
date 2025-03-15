class Solution:
    def rob(self, nums: List[int]) -> int:
        maxAmount, tmp = 0, 0
        for i in range(len(nums)):
            maxAmount, tmp = max(maxAmount, tmp+nums[i]), maxAmount

        return maxAmount