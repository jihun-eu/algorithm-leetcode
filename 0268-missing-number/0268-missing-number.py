class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        totalSum = 0
        for num in range(len(nums)+1):
            totalSum += num

        for num in nums:
            totalSum -= num
        
        return totalSum