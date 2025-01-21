"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    visited = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        if node in Solution.visited: return Solution.visited[node]

        Solution.visited[node] = Node(node.val)
        for neighbor in node.neighbors:
            Solution.visited[node].neighbors.append(self.cloneGraph(neighbor))

        return Solution.visited[node]
            
            