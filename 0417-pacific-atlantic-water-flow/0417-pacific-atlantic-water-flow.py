class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rowSize = len(heights)
        colSize = len(heights[0])

        pacificMap = [[False] * colSize for _ in range(rowSize)]
        atlanticMap = [[False] * colSize for _ in range(rowSize)]

        def bfs(queue, oceanMap, visited):
            nonlocal heights
            while queue:
                row, col = queue.popleft()
                print(row, col)
                visited[row][col] = oceanMap[row][col] = True
                for addr, addc in move:
                    newRow = row + addr
                    newCol = col + addc
                    if not (0 <= newRow < rowSize and 0 <= newCol < colSize):
                        continue
                    if visited[newRow][newCol]:
                        continue
                    if heights[newRow][newCol] < heights[row][col]:
                        continue
                    queue.append([newRow, newCol])

            print(oceanMap)
            return oceanMap

        queue = deque()
        visited = [[False] * colSize for _ in range(rowSize)]
        for row in range(rowSize):
            queue.append([row, 0])
            visited[row][0] = True
        for col in range(colSize):
            queue.append([0, col])
            visited[0][col] = True
        pacificMap = bfs(queue, pacificMap, visited)
        queue = deque()
        visited = [[False] * colSize for _ in range(rowSize)]
        for row in range(rowSize):
            queue.append([row, colSize-1])
            visited[row][colSize-1] = True
        for col in range(colSize):
            queue.append([rowSize-1, col])
            visited[rowSize-1][col] = True
        atlanticMap = bfs(queue, atlanticMap, visited)


        flowables = []
        for r in range(rowSize):
            for c in range(colSize):
                if pacificMap[r][c] and atlanticMap[r][c]:
                    flowables.append([r, c])

        return flowables







        
