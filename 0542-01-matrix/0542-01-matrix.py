class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        maxRow = len(mat)
        maxCol = len(mat[0])
        INF = maxRow * maxCol

        for row in range(maxRow):
            for col in range(maxCol):
                if mat[row][col] > 0:
                    topNeighbor = mat[row-1][col] if row > 0 else INF
                    leftNeighbor = mat[row][col-1] if col > 0 else INF
                    mat[row][col] = min(topNeighbor, leftNeighbor) + 1

        for row in range(maxRow - 1, -1, -1):
            for col in range(maxCol - 1, -1, -1):
                if mat[row][col] > 0:
                    bottomNeighbor = mat[row+1][col] if row < maxRow - 1 else INF
                    rightNeighbor = mat[row][col+1] if col < maxCol - 1 else INF
                    mat[row][col] = min(mat[row][col], bottomNeighbor + 1, rightNeighbor + 1)
        
        return mat