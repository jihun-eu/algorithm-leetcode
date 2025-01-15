# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isMatch(root, subRoot): return True
        if not root: return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isMatch(self, root:Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None or subRoot == None: return root == subRoot

        return root.val == subRoot.val and self.isMatch(root.left, subRoot.left) and self.isMatch(root.right, subRoot.right)
