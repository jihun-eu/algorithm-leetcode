class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        VISITED = 128
        
        maxRow = len(matrix)
        if maxRow == 1: 
            return matrix[0]
        maxCol = len(matrix[0])
        if maxCol == 1: 
            return [el[0] for el in matrix]
        maxTraverse = maxRow * maxCol
        
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direct = 0
        currRow, currCol = 0, 0
        orderedList = [matrix[currRow][currCol]]
        matrix[currRow][currCol] = VISITED
        traverse = 1
        while traverse < maxTraverse:
            print(currRow, currCol, direct)
            nextRow, nextCol = currRow+move[direct][0], currCol+move[direct][1]
            if not(0 <= nextRow < maxRow and 0 <= nextCol < maxCol and matrix[nextRow][nextCol] != VISITED):
                direct = (direct+1) % 4
                continue
            orderedList.append(matrix[nextRow][nextCol])
            matrix[nextRow][nextCol] = VISITED
            currRow, currCol = nextRow, nextCol
            traverse += 1
            
        return orderedList
            

