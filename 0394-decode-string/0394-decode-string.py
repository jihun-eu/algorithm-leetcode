class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        for c in s:
            if c == "]":

                tmp = ""
                while stack and stack[-1] != "[":
                    tmp = stack.pop() + tmp
                stack.pop()

                tmpNum = ""
                while stack and stack[-1].isdigit():
                    tmpNum = stack.pop() + tmpNum

                stack.append(tmp * int(tmpNum))

            else:
                stack.append(c)

        decodeString = "".join(stack)
        return decodeString