# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preorderDeque = deque(preorder)

        def build(preorder: int, inorder: int) -> Optional[TreeNode]:
            if not inorder:
                return
            
            inorderIndex = inorder.index(preorder.popleft())
            
            node = TreeNode(inorder[inorderIndex])
            node.left = build(preorder, inorder[:inorderIndex])
            node.right = build(preorder, inorder[inorderIndex+1:])

            return node

        return build(preorderDeque, inorder)
