class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        stack = []

        for c in s:
            if c not in brackets:
                stack.append(c)
                continue

            if len(stack) == 0:
                return False

            tmp = brackets[c]
            if stack.pop() != brackets[c]:
                return False
        
        return len(stack) == 0
            