class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]
        for vertexA, vertexB in edges:
            graph[vertexA].append(vertexB)
            graph[vertexB].append(vertexA)

        degree = [0] * n
        for vertex in range(n):
            degree[vertex] = len(graph[vertex])
            
        queue = deque()
        for vertex in range(n):
            if len(graph[vertex]) == 1:
                queue.append(vertex)
        
        while queue:
            if n <= 2:
                break

            for _ in range(len(queue)):
                vertex = queue.popleft()
                n -= 1
                for adjacent in graph[vertex]:
                    degree[adjacent] -= 1
                    if degree[adjacent] == 1:
                        queue.append(adjacent)
        
        return list(queue)