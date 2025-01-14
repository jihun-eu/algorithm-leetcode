class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        tmp = set(nums)
        for num in range(len(nums) + 1):
            if num not in tmp:
                break
        
        return num