# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side_view = []
        if not root:
            return right_side_view
        queue = [root]
        while queue:
            epoch = len(queue)
            for i in range(epoch):
                child = queue.pop(0)
                if i == epoch - 1:
                    right_side_view.append(child.val)
                if child.left:
                    queue.append(child.left)
                if child.right:
                    queue.append(child.right)
        return right_side_view