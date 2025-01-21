class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        maxCol = len(grid[0])

        secondRobotLv1 = sum(grid[0])
        secondRobotLv2 = 0

        secondRobotMin = secondRobotLv1
        
        for i in range(maxCol):
            secondRobotLv1 -= grid[0][i]
            secondRobotMin = min(secondRobotMin, max(secondRobotLv1, secondRobotLv2))
            secondRobotLv2 += grid[1][i]

        return secondRobotMin