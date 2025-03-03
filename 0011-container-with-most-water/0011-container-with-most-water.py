class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:
            tmp_area = right - left
            
            if height[left] <= height[right]:
                tmp_area *= height[left]
                left += 1
            else:
                tmp_area *= height[right]
                right -= 1
            
            max_area = max(max_area, tmp_area)

        return max_area
