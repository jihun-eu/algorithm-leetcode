class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        maxRow, maxCol = len(grid), len(grid[0])
        visited = [[False] * maxCol for _ in range(maxRow)]
        
        def DFS(row: int, col: int) -> int:
            if row < 0 or row >= maxRow or col < 0 or col >= maxCol or grid[row][col] == 0 or visited[row][col]:
                return 0
            visited[row][col] = True
            return grid[row][col] + DFS(row+1, col) + DFS(row-1, col) + DFS(row, col+1) + DFS(row, col-1)

        maxFish = 0
        for row in range(maxRow):
            for col in range(maxCol):
                if grid == 0 or visited[row][col]: continue
                maxFish = max(maxFish, DFS(row, col))

        return maxFish