class LRUCache:

    class Node:
        def __init__(self, key:int=-1, val:int=-1) -> None:
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.latest = self.Node()
        self.oldest = self.Node()
        self.latest.prev = self.oldest
        self.oldest.next = self.latest
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert(self, node):
        node.next = self.latest
        node.prev = self.latest.prev
        self.latest.prev.next = node
        self.latest.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = self.Node(key, value)
        self._insert(self.cache[key])

        if self.capacity < len(self.cache):
            tmp = self.oldest.next
            self._remove(tmp)
            del self.cache[tmp.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)