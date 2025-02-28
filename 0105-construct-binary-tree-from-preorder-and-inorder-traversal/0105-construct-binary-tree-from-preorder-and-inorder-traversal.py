# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preorderDeque = deque(preorder)

        inorderIndexMap = {}
        for i, node in enumerate(inorder):
            inorderIndexMap[node] = i

        def build(start: int, end: int) -> Optional[TreeNode]:
            nonlocal preorderDeque, inorderIndexMap
            if end < start:
                return

            node = TreeNode(preorderDeque.popleft())
            mid = inorderIndexMap[node.val]

            node.left = build(start, mid-1)
            node.right = build(mid+1, end)

            return node

        return build(0, len(inorder)-1)
