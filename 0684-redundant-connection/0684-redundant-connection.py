class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = len(edges)
        adjacentList = [[] for _ in range(size)]

        def hasCycle(src: int, target: int, visited: List[int], adjacentList: List[List[int]]) -> bool:
            visited[src] = True

            if src == target: return True

            isCycled = False
            for adj in adjacentList[src]:
                if visited[adj]: continue
                isCycled = isCycled or hasCycle(adj, target, visited, adjacentList)
            return isCycled
        
        for edge in edges:
            src, target = edge[0] - 1, edge[1] - 1
            visited = [False] * size

            if hasCycle(src, target, visited, adjacentList): return edge

            adjacentList[src].append(target)
            adjacentList[target].append(src)

        return []