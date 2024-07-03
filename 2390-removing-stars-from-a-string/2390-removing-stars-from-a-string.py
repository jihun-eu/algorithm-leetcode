class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for w in s:
            if w == "*":
                if not stack:
                    continue
                stack.pop()
            else:
                stack.append(w)

        result = "".join(stack)
        return result