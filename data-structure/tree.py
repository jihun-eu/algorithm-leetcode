class Node:
    
    def __init__(self, value) -> None:
        self.value = value
        self.left: Node = None
        self.right: Node = None

def dfs(node: Node):
    visited = []
    stack = [node]
    while stack:
        child = stack.pop()

        visited.append(child.value)

        if child.left:
            stack.append(child.left)
        if child.right:
            stack.append(child.right)
        
    return visited

def recursive_dfs(node: Node):
    visited = []

    def dfs(node: Node):
        visited.append(node.value)
        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right)
    
    dfs(node)
    return visited

def bfs(node: Node):
    visited = []
    queue = [node]

    while queue:
        child = queue.pop(0)
        
        visited.append(child.value)
        
        if child.left:
            queue.append(child.left)
        if child.right:
            queue.append(child.right)
    
    return visited
        