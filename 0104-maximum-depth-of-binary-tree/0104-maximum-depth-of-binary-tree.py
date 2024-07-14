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
        
        max_level = 0
        queue = [root]
        while queue:
            max_level += 1
            for tries in range(len(queue)):
                child = queue.pop(0)
                if child.left:
                    queue.append(child.left)
                if child.right:
                    queue.append(child.right)
            
        return max_level