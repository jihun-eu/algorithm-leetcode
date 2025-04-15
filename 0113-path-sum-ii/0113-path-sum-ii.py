# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []

        def dfs(root: Optional[TreeNode], path: List[int], total: int) -> None:
            if not root:
                return

            path.append(root.val)
            total -= root.val

            if not (root.left or root.right):
                if total == 0:
                    paths.append(path.copy())
            
            dfs(root.left, path, total)
            dfs(root.right, path, total)
            
            path.pop()
            
            
            

        dfs(root, [], targetSum)
        return paths