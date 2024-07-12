class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        
        def checkIsland(grid: List[List[str]], row: int, col: int):
            if not (-1 < row < len(grid) and -1 < col < len(grid[0])):
                return
            
            if grid[row][col] != "1":
                return

            grid[row][col] = "2"
            for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                checkIsland(grid, row+x, col+y)

        island_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    island_count += 1
                    checkIsland(grid, row, col)
        
        return island_count

        