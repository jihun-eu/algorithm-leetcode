class Solution:


    def mergeLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not(list1 and list2):
            return list1 or list2
        
        currNode = None
        if list1.val < list2.val:
            currNode = list1
            currNode.next = self.mergeLists(list1.next, list2)
        else:
            currNode = list2
            currNode.next = self.mergeLists(list1, list2.next)
        
        return currNode

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            lists.append(self.mergeLists(lists.pop(0), lists.pop(0)))
        
        return lists[0]