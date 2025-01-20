class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
        maxRow = len(mat)
        maxCol = len(mat[0])
        
        rowCounter = [0] * maxCol
        colCounter = [0] * maxRow

        invertMap = {}
        for row in range(maxRow):
            for col in range(maxCol):
                invertMap[mat[row][col]] = (col, row)
        for index, num in enumerate(arr):
            row, col = invertMap[num]
            rowCounter[row] += 1
            if rowCounter[row] == maxRow:
                break
            colCounter[col] += 1
            if colCounter[col] == maxCol:
                break
        
        return index
