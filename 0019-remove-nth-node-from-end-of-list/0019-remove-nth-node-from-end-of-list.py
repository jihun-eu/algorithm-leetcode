# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newList = slow = fast = ListNode(0, head)

        # loop fast pointer until n interval
        for _ in range(n):
            fast = fast.next
        
        # loop together until fast pointer's last
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return newList.next

        
        