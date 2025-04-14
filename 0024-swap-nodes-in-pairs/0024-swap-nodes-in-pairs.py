# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode(0, head)
        prev = newList
        curr = head

        while curr and curr.next:
            second = curr.next
            tmp = curr.next.next

            second.next = curr
            curr.next = tmp
            prev.next = second

            prev = curr
            curr = tmp

        return newList.next