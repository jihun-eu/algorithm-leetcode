# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        idx = 0
        def inorderTraverse(root: Optional[TreeNode]) -> Optional[TreeNode]:
            nonlocal idx
            
            if not root:
                return None

            left = inorderTraverse(root.left)
            if left: return left
            idx += 1
            if idx == k:
                return root
            right = inorderTraverse(root.right)
            if right: return right

        return inorderTraverse(root).val
        