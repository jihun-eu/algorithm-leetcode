# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        worker = head
        while worker:
            stack.append(worker)
            worker = worker.next

        newList = ListNode()
        currNode = newList
        while len(stack) > 1:
            node1 = stack.pop(0)
            node2 = stack.pop()

            node2.next = None
            node1.next = node2
            currNode.next = node1
            currNode = node2
        
        if stack:
            node = stack.pop()
            node.next = None
            currNode.next = node

        head = newList.next