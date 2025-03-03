class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def dp(endOfString: int) -> bool:
            if endOfString < 0:
                return True

            for word in wordDict:
                if endOfString < len(word)-1:
                    continue
                if s[endOfString-len(word)+1:endOfString+1] == word and dp(endOfString-len(word)):
                    return True
            
            return False
        
        return dp(len(s)-1)