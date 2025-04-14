# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode(0, head)
        slow, fast = newList, head

        while fast and fast.next:
            tmp = fast.next.next
            second = fast.next


            second.next = fast
            fast.next = tmp
            slow.next = second

            slow = fast
            fast = tmp

        return newList.next
