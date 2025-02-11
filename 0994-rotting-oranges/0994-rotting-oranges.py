class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        maxRow, maxCol = len(grid), len(grid[0])

        rottenOranges = deque()
        freshOranges = 0

        for row in range(maxRow):
            for col in range(maxCol):
                if grid[row][col] == 2: rottenOranges.append((row, col))
                elif grid[row][col] == 1: freshOranges += 1
        
        move = [0, 1, 0, -1, 0]
        minutes = -1 if rottenOranges else 0
            
        while rottenOranges:
            for _ in range(len(rottenOranges)):
                currRow, currCol = rottenOranges.popleft()
                for i in range(4):
                    nextRow, nextCol = currRow+move[i], currCol+move[i+1]
                    if not(0 <= nextRow < maxRow and 0 <= nextCol < maxCol and grid[nextRow][nextCol] == 1): continue
                    grid[nextRow][nextCol] = 2
                    freshOranges -= 1
                    rottenOranges.append((nextRow, nextCol))
            minutes += 1

        return minutes if freshOranges == 0 else -1


