from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        size = len(graph)
        nodeStatus = {}

        def dfs(node: int) -> bool:
            if node in nodeStatus: return nodeStatus[node]
            nodeStatus[node] = False
            nodeStatus[node] = all(dfs(adjacentNode) for adjacentNode in graph[node])
            return nodeStatus[node]

        safeNodes = []
        for currNode in range(size):
            if dfs(currNode):
                safeNodes.append(currNode)

        return safeNodes