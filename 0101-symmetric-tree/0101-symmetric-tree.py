# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_same(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            elif (left and not right) or (not left and right) or (left.val != right.val):
                return False
            else:
                return is_same(left.left, right.right) and is_same(left.right, right.left)
        
        if not root:
            return True
        else:
            return is_same(root.left, root.right)