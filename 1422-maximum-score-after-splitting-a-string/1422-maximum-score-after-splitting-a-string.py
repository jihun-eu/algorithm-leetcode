class Solution:
    def maxScore(self, s: str) -> int:
        
        size = len(s) - 1
        tmp = [0] * size

        zeroCnt = 0
        for i in range(size):
            if s[i] == "0":
                zeroCnt += 1
            tmp[i] = zeroCnt

        maxScore = oneCnt = 0
        for i in range(size, 0, -1):
            if s[i] == "1":
                oneCnt += 1
            maxScore = max(maxScore, tmp[i-1] + oneCnt)

        return maxScore