# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
       
        def left_bfs(root):
            visited = []
            queue = [root]
            while queue:
                child = queue.pop(0)

                if child is not None:
                    visited.append(child.val)
                    queue.append(child.left)
                    queue.append(child.right)
                else:
                    visited.append(None)

            return visited
                    
        
        def right_bfs(root):
            visited = []
            queue = [root]
            while queue:
                child = queue.pop(0)

                if child is not None:
                    visited.append(child.val)
                    queue.append(child.right)
                    queue.append(child.left)
                else:
                    visited.append(None)

            return visited

        return left_bfs(root) == right_bfs(root)
                    
