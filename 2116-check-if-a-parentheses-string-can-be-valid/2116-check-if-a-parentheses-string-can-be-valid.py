class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) & 1 == 1:
            return False

        unlockedStack = []
        lockedOpenParentheseStack = []
        for i in range(len(s)):
            if locked[i] == "0":
                unlockedStack.append(i)
                continue

            if s[i] == "(":
                lockedOpenParentheseStack.append(i)
            else:
                if lockedOpenParentheseStack:
                    lockedOpenParentheseStack.pop()
                elif unlockedStack:
                    unlockedStack.pop()
                else:
                    return False

        while lockedOpenParentheseStack and unlockedStack:
            if unlockedStack.pop() < lockedOpenParentheseStack.pop():
                return False
        
        return not lockedOpenParentheseStack and len(unlockedStack) & 1 == 0
        

                
        