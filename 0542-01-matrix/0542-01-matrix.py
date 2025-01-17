class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        maxRow = len(mat)
        maxCol = len(mat[0])
        visited = []
        for x in range(maxRow):
            for y in range(maxCol):
                if mat[x][y]:
                    mat[x][y] = -1
                else:
                    visited.append((x, y))

        while visited:
            pointX, pointY = visited.pop(0)
            for newPointX, newPointY in [(pointX+1,pointY),(pointX,pointY+1),(pointX-1,pointY),(pointX,pointY-1)]:
                if newPointX < 0 or newPointX >= maxRow or newPointY < 0 or newPointY >= maxCol or mat[newPointX][newPointY] != -1:
                    continue
                mat[newPointX][newPointY] = mat[pointX][pointY] + 1
                visited.append((newPointX, newPointY))
        return mat
            
        
        return distMatrix

                
                
