# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def is_good(root: TreeNode, parent: int):
            
            count = 0
            
            if not root:
                return count
            
            if parent <= root.val:
                count = 1
                parent = root.val

            return count + is_good(root.left, parent) + is_good(root.right, parent)

        return is_good(root, -100000000)
        