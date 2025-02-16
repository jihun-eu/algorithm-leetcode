class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0] * 3
        for color in nums:
            colors[color] += 1
        
        color = 0
        for i in range(len(nums)):
            while color < 3 and colors[color] == 0: color += 1
            if not color < 3: break
            nums[i] = color
            colors[color] -= 1
        
