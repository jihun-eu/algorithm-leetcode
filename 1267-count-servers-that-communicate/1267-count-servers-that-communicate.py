from itertools import pairwise

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        maxRow = len(grid)
        maxCol = len(grid[0])

        rowServer = [0] * maxRow
        colServer = [0] * maxCol
        existServers = []

        for row in range(maxRow):
            for col in range(maxCol):
                if not grid[row][col]: continue
                rowServer[row] += 1
                colServer[col] += 1
                existServers.append((row, col))
        
        activeServers = 0
        for row, col in existServers:
            if rowServer[row] > 1 or colServer[col] > 1:
                activeServers += 1

        return activeServers
        
