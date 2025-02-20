# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSideNodes = []
        
        if not root: return rightSideNodes

        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if len(rightSideNodes) < level:
                rightSideNodes.append(node.val)
            
            nextLevel = level + 1
            if node.right:
                queue.append((node.right, nextLevel))
            if node.left:
                queue.append((node.left, nextLevel))
        
        return rightSideNodes