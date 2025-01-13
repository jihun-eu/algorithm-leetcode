class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        
        zeroPointer = 0
        for nonZeroPointer in range(size):
            if nums[zeroPointer] == 0 and nums[nonZeroPointer] != 0:
                nums[zeroPointer], nums[nonZeroPointer] = nums[nonZeroPointer], nums[zeroPointer]
            
            if nums[zeroPointer] != 0:
                zeroPointer += 1