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

            if not stack:
                return False
            
            if stack.pop() != brackets[c]:
                return False
        
        return not stack
