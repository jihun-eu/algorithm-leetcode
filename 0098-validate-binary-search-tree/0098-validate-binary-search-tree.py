# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validateBST(root: Optional[TreeNode], minVal: int = -math.inf, maxVal: int = math.inf) -> bool:
            if not root: return True
            if root.val <= minVal or maxVal <= root.val: return False
            return validateBST(root.left, minVal, root.val) and validateBST(root.right, root.val, maxVal)

        return validateBST(root)
        
        