class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        maxRow, maxCol = len(grid), len(grid[0])

        rottenQueue = deque()
        for row in range(maxRow):
            for col in range(maxCol):
                if grid[row][col] == 2: rottenQueue.append((row, col))

        infect = [0, 1, 0, -1, 0]
        minutes = -1
        if not rottenQueue: 
            minutes = 0
        
        while rottenQueue:
            for _ in range(len(rottenQueue)):
                currentRow, currentCol = rottenQueue.popleft()
                for i in range(4):
                    nextRow, nextCol = currentRow+infect[i], currentCol+infect[i+1]
                    if nextRow < 0 or maxRow <= nextRow or nextCol < 0 or maxCol <= nextCol or grid[nextRow][nextCol] != 1:
                        continue
                    grid[nextRow][nextCol] = 2
                    rottenQueue.append((nextRow, nextCol))
            minutes += 1
                
        for row in grid:
            for el in row:
                if el == 1: return -1
                
        return minutes
