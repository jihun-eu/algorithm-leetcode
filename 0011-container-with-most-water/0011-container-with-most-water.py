class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Problem: Get maximum area
        # Assumed Topic: Two pointers

        max_area = 0

        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            curr_area = 0
            if height[left] < height[right]:
                curr_area = width * height[left]
                left += 1
            else:
                curr_area = width * height[right]
                right -= 1

            max_area = max(max_area, curr_area)
        
        return max_area