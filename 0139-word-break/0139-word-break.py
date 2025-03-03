class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        isGonnaMakeit = [False] * len(s)

        for endOfString in range(len(s)):
            for word in wordDict:
                if endOfString < len(word) - 1:
                    continue
                if len(word) - 1 < endOfString and not isGonnaMakeit[endOfString - len(word)]:
                    continue
                if s[endOfString - len(word) + 1: endOfString + 1] == word:
                    isGonnaMakeit[endOfString] = True

        return isGonnaMakeit[-1]        