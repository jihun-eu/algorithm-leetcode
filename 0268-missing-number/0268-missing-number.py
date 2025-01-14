class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        missed = 0
        for num in range(len(nums)+1):
            missed ^= num

        for num in nums:
            missed ^= num
        
        return missed