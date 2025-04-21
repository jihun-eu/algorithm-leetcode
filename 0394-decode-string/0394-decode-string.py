class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        for char in s:
            if char == "]":
                substring = ''
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()

                digit = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                stack.append(substring * int(digit))
            else:
                stack.append(char)

        return "".join(stack)