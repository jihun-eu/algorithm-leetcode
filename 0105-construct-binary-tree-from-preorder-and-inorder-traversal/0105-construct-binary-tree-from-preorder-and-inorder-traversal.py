# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preorder = deque(preorder)

        inorderIndexMap = {}
        for idx, val in enumerate(inorder):
            inorderIndexMap[val] = idx
        
        def build(start: int, end: int) -> Optional[TreeNode]:
            nonlocal preorder, inorderIndexMap
            if not start < end:
                return None


            node = TreeNode(preorder.popleft())
            
            mid = inorderIndexMap[node.val]
            node.left = build(start, mid)
            node.right = build(mid+1, end)

            return node
            
        return build(0, len(preorder))