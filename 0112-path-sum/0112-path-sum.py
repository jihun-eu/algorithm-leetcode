# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False

        stack = [(0, root)]

        while stack:
            accum_value, child = stack.pop()
            
            child_value = accum_value + child.val

            if not (child.left or child.right) and child_value == targetSum:
                return True

            if child.left:
                stack.append((child_value, child.left))
            if child.right:
                stack.append((child_value, child.right))
            
        return False
            