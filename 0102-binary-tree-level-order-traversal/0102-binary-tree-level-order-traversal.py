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

        queue = [(0, root)]
        current_level = -1
        while queue:
            (level, child) = queue.pop(0)
            if level > current_level:
                current_level = level
                result.append([])

            result[level].append(child.val)
            next_level = level + 1

            if child.left:
                queue.append((next_level, child.left))

            if child.right:
                queue.append((next_level, child.right))

        return result

            