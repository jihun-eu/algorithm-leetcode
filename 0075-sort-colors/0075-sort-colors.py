class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0] * 3
        for color in nums:
            colors[color] += 1
        
        index = 0
        for color in range(3):
            for _ in range(colors[color]):
                nums[index] = color
                index += 1