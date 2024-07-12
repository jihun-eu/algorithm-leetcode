# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        queue = [root]
        current_level = -1
        while queue:
            
            level_nodes_count = len(queue)
            level_nodes = []
            for i in range(level_nodes_count):
                child = queue.pop(0)
                
                level_nodes.append(child.val)

                if child.left:
                    queue.append(child.left)

                if child.right:
                    queue.append(child.right)

            result.append(level_nodes)        


        return result

            