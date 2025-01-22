from collections import deque
from itertools import pairwise

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        MOVE = [0, 1, 0, -1, 0]

        maxRow = len(isWater)
        maxCol = len(isWater[0])

        queue = deque()

        for row in range(maxRow):
            for col in range(maxCol):
                if isWater[row][col] == 1:
                    queue.append((row, col))
                isWater[row][col] = -1
        
        currLevel = 0
        while queue:
            for i in range(len(queue)):
                currRow, currCol = queue.popleft()
                if isWater[currRow][currCol] != -1:
                    continue
                isWater[currRow][currCol] = currLevel
                for moveRow, moveCol in pairwise(MOVE):
                    movedRow, movedCol = currRow+moveRow, currCol+moveCol
                    if 0 <= movedRow < maxRow and 0 <= movedCol < maxCol and isWater[movedRow][movedCol] == -1:
                        queue.append((movedRow, movedCol))
            currLevel += 1

        return isWater