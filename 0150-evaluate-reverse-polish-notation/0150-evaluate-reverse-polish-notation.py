class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': lambda x, y: y + x,
            '-': lambda x, y: y - x,
            '*': lambda x, y: y * x,
            '/': lambda x, y: int(y / x),
        }

        stack = []
        for token in tokens:
            if token not in operations: stack.append(int(token))
            else: stack.append(operations[token](stack.pop(), stack.pop()))
        
        return stack.pop()
                