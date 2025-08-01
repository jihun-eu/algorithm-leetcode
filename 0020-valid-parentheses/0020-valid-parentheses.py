class Solution:

    brackets = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c not in Solution.brackets:
                stack.append(c)
                continue
            
            if not stack or stack.pop() != Solution.brackets[c]:
                return False
        
        return not stack