class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        cnt = 0
        for word in words:
            if not word.startswith(pref):
                continue
            cnt += 1
        
        return cnt