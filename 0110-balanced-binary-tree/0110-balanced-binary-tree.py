# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeight(root) >= 0

    def getHeight(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0

        left, right = self.getHeight(root.left), self.getHeight(root.right)
        if left >= 0 and right >= 0 and (left - right) ** 2 <= 1:
            return 1 + max(left, right)
        else:
            return -1
            