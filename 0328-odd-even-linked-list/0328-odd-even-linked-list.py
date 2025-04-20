# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
        isOdd = False

        pre = odd = head
        curr = evenStart = even = head.next
        while curr:
            tmp = curr
            pre.next = curr.next
            pre = curr
            curr = curr.next
            if isOdd:
                odd.next = tmp
                odd = odd.next
                odd.next = evenStart
            else:
                even.next = tmp
                even = even.next
                even.next = None
            isOdd = not isOdd

            odd.next = evenStart
        return head
            