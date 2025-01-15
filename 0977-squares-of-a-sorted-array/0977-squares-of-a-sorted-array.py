class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []

        left = 0
        right = len(nums) - 1
        while left <= right:
            leftSquare = nums[left] ** 2
            rightSquare = nums[right] ** 2
            
            if leftSquare < rightSquare:
                squares.append(rightSquare)
                right -= 1
            else:
                squares.append(leftSquare)
                left += 1
        
        return squares[::-1]