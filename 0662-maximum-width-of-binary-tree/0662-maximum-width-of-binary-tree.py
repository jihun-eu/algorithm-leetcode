# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = 1
        queue = deque([(1, root)])
        while queue:
            currWidth = queue[-1][0] - queue[0][0] + 1
            maxWidth = max(maxWidth, currWidth)
            
            for _ in range(len(queue)):
                seq, node = queue.popleft()
                nextSeq = 2 * seq
                if node.left:
                    queue.append((nextSeq-1, node.left))
                if node.right:
                    queue.append((nextSeq, node.right))
        
        return maxWidth

