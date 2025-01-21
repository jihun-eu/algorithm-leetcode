"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}
        queue = [node]
        
        visited[node] = Node(node.val)

        while queue:
            currNode = queue.pop(0)
            for neighbor in currNode.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                visited[currNode].neighbors.append(visited[neighbor])

        return visited[node]
            
            