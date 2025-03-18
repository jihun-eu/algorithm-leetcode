class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        firstDecr = len(nums) - 1
        while firstDecr > 0 and nums[firstDecr-1] >= nums[firstDecr]:
            firstDecr -= 1
        
        if firstDecr == 0:
            self.reverse(nums)
            return
        
        swapper = len(nums) - 1
        while swapper >= firstDecr and nums[swapper] <= nums[firstDecr-1]:
            swapper -= 1
        nums[firstDecr-1], nums[swapper] = nums[swapper], nums[firstDecr-1]

        self.reverse(nums, firstDecr)


    def reverse(self, nums:List[int], start:int = 0):
        left, right = start, len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

