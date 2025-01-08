from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        strCnt = Counter(s)
        hasOddCnt = 0
        prefixSumEvenCnt = 0
        print(strCnt)

        for cnt in strCnt.values():

            if cnt % 2 == 0:
                prefixSumEvenCnt += cnt
                continue
            else:
                if cnt > 1:
                    prefixSumEvenCnt += cnt - 1
                hasOddCnt = 1

        return hasOddCnt + prefixSumEvenCnt