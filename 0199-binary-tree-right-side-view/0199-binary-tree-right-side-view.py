# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSideNodes = []
        def dfs(root: Optional[TreeNode], level: int) -> None:
            nonlocal rightSideNodes
            if not root: return root
            if len(rightSideNodes) < level:
                rightSideNodes.append(root.val)
            nextLevel = level + 1
            dfs(root.right, nextLevel)
            dfs(root.left, nextLevel)
        
        dfs(root, 1)
        return rightSideNodes
