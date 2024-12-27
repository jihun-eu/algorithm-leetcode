class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()
        
        tmp = nums[0]
        for num in nums[1:]:
            if tmp == num:
                return True
            tmp = num
        return False