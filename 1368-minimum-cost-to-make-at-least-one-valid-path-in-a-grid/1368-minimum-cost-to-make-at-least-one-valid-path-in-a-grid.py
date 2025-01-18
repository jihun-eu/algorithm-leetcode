class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        maxRow = len(grid)
        maxCol = len(grid[0])

        minChanges = [[float("inf")] * maxCol for _ in range(maxRow)]
        minChanges[0][0] = 0

        while True:
            prevState = [row[:] for row in minChanges]

            for row in range(maxRow):
                for col in range(maxCol):
                    if row > 0:
                        minChanges[row][col] = min(
                            minChanges[row][col], 
                            minChanges[row-1][col] + (0 if grid[row-1][col] == 3 else 1)
                        )

                    if col > 0:
                        minChanges[row][col] = min(
                            minChanges[row][col],
                            minChanges[row][col-1] + (0 if grid[row][col-1] == 1 else 1)
                        )

            for row in range(maxRow - 1, -1, -1):
                for col in range(maxCol - 1, -1, -1):
                    if row < maxRow - 1:
                        minChanges[row][col] = min(
                            minChanges[row][col],
                            minChanges[row+1][col] + (0 if grid[row+1][col] == 4 else 1)
                        )

                    if col < maxCol - 1:
                        minChanges[row][col] = min(
                            minChanges[row][col],
                            minChanges[row][col+1] + (0 if grid[row][col+1] == 2 else 1)
                        )

            if prevState == minChanges:
                break

        return minChanges[maxRow-1][maxCol-1]
