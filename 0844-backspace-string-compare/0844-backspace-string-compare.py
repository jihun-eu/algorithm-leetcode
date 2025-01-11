class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def fullString(keyInput: str) -> str:
            buffer = []
            for key in keyInput:
                if key != "#":
                    buffer.append(key)
                    continue
                if buffer:
                    buffer.pop()

            return "".join(buffer)
        
        return fullString(s) == fullString(t)