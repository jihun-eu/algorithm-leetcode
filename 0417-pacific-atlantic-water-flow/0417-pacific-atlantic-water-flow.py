class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        rowSize = len(heights)
        colSize = len(heights[0])

        def bfs(queue, visited):
            nonlocal heights
            while queue:
                row, col = queue.popleft()
                visited[row][col] = True
                for newRow, newCol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                    if not (0 <= newRow < rowSize and 0 <= newCol < colSize) or visited[newRow][newCol] or heights[newRow][newCol] < heights[row][col]:
                        continue
                    queue.append([newRow, newCol])

        pacificQ = deque()
        atlanticQ = deque()
        
        pacificMap = [[False] * colSize for _ in range(rowSize)]
        atlanticMap = [[False] * colSize for _ in range(rowSize)]
        
        for row in range(rowSize):
            pacificQ.append([row, 0])
            atlanticQ.append([row, colSize-1])
            pacificMap[row][0] = atlanticMap[row][colSize-1] = True
            
        for col in range(colSize):
            pacificQ.append([0, col])
            atlanticQ.append([rowSize-1, col])
            pacificMap[0][col] = atlanticMap[rowSize-1][col] = True
            
        bfs(pacificQ, pacificMap)
        bfs(atlanticQ, atlanticMap)


        flowables = []
        for r in range(rowSize):
            for c in range(colSize):
                if pacificMap[r][c] and atlanticMap[r][c]:
                    flowables.append([r, c])

        return flowables