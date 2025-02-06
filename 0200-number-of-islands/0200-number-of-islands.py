class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        maxRow, maxCol = len(grid), len(grid[0])
        
        move = [0, 1, 0, -1, 0]

        def flagIslands(row: int, col: int) -> None:
            nonlocal grid, maxRow, maxCol, move
            if row < 0 or maxRow <= row or col < 0 or maxCol <= col or grid[row][col] != "1": return
            grid[row][col] = "0"
            for i in range(4): flagIslands(row+move[i], col+move[i+1])
        
        islandCnt = 0
        for row in range(maxRow):
            for col in range(maxCol):
                if grid[row][col] == "0": continue
                flagIslands(row, col)
                islandCnt += 1

        return islandCnt