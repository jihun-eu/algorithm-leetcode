class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def isGonnaMakeit(endOfString: int) -> bool:
            nonlocal wordDict

            if endOfString < 0:
                return True

            for word in wordDict:
                if s[endOfString - len(word) + 1: endOfString + 1] == word and isGonnaMakeit(endOfString - len(word)):
                    return True
            
            return False

        return isGonnaMakeit(len(s)-1)