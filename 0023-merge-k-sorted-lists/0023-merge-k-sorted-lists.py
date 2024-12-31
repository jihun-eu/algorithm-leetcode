class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        size = len(lists)

        heap = []

        for list_node in lists:
            while list_node:
                tmp = list_node
                list_node = list_node.next
                tmp.next = None
                heap.append(tmp)
        
        heap.sort(key=lambda x: x.val)
    
        newList = ListNode()
        currNode = newList
        for nextNode in heap:
            currNode.next = nextNode
            nextNode.next = None
            currNode = nextNode
        
        return newList.next