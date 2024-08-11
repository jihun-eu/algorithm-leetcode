class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # try it again
        head = 0
        rows = len(matrix)
        cols = len(matrix[0])

        tail = rows * cols - 1

        while head <= tail:
        
            mid = (head+tail) // 2
            row = mid // cols 
            col = mid % cols 
            
            num = matrix[row][col]

            if num == target:
                return True
            
            if num > target:
                tail = mid - 1
            else:
                head = mid + 1
        
        return False
