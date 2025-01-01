class Solution:
    def maxScore(self, s: str) -> int:
        
        oneCnt = s.count("1")

        maxScore = zeroCnt = 0
        for c in s[:-1]:
            if c == "0":
                zeroCnt += 1
            if c == "1":
                oneCnt -= 1
            
            maxScore = max(maxScore, zeroCnt + oneCnt)

        return maxScore