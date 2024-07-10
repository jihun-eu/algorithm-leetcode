# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_level = 1
        queue = [(1, root)]
        while queue:
            level, child = queue.pop(0)
            max_level = max(level, max_level)
            next_level = level + 1
            if child.left:
                queue.append((next_level, child.left))
            if child.right:
                queue.append((next_level, child.right))
            
        return max_level