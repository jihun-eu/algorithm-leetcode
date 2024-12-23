class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        size = len(nums)
        
        for ptr1 in range(size-1):
            for ptr2 in range(ptr1+1, size):
                val = nums[ptr1] + nums[ptr2]
                if val == target:
                    return [ptr1, ptr2]

        
