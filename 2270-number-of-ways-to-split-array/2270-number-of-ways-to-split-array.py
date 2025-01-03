class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        validSplitCnt = 0
        
        size = len(nums)
        prefixSum = [0] * size
        for i in range(size):
            prefixSum[i] = prefixSum[i-1] + nums[i]
        
        totalSum = prefixSum[-1]
        for val in prefixSum[:-1]:
            validSplitCnt += 1 if val >= totalSum - val else 0

        return validSplitCnt

