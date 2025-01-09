# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def getLongestDiameterWithLevel(root: Optional[TreeNode]) -> int:            
            if not root: return 0, 0

            leftDiameter, leftLevel = getLongestDiameterWithLevel(root.left)
            rightDiameter, rightLevel = getLongestDiameterWithLevel(root.right)
            
            longestDiameter = max(leftDiameter, rightDiameter, leftLevel + rightLevel)
            currentLevel = 1 + max(leftLevel, rightLevel)

            return longestDiameter, currentLevel

        longestDiameter, _ = getLongestDiameterWithLevel(root)

        return longestDiameter


