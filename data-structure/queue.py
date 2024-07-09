class Node:
    
    def __init__(self, value) -> None:
        self.value = value
        self.next: Node|None = None


class Queue:

    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None
        self.size: int = 0
    
    def enqueue(self, node: Node) -> None:

        self.size += 1

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self) -> Node:
        
        if self.size == 0:
            return None
        
        tmp = self.head
        self.size -= 1

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:    
            self.head = tmp.next

        return tmp
