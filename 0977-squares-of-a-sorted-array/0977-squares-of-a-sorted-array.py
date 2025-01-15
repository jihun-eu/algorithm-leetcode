class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            nums[i] = nums[i] ** 2

        squares = []
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                squares.append(nums[right])
                right -= 1
            else:
                squares.append(nums[left])
                left += 1
        
        return squares[::-1]