# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def swapChildren(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.left, root.right = root.right, root.left

    def traverseTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
        self.traverseTree(root.left)
        self.traverseTree(root.right)
        self.swapChildren(root)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverseTree(root)
        return root