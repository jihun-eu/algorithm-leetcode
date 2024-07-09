class Node:
    
    def __init__(self, value) -> None:
        self.value = value
        self.next: Node|None = None


class Stack:

    def __init__(self) -> None:
        self.head: Node = None
    
    def push(self, node: Node) -> None:
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def pop(self) -> Node:
        tmp = self.head
        self.head = self.head.next
        return tmp
    
    def peek(self) -> Node:
        return self.head