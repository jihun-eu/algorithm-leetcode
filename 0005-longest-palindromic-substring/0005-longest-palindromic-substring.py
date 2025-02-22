class Solution:
    def longestPalindrome(self, s: str) -> str:

        palindrome = (0, 0)
        dp = [[False] * len(s) for _ in s]
        
        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                palindrome = (i, i+1)

        for diff in range(2, len(s)):
            for left in range(len(s) - diff):
                right = left + diff
                if s[left] == s[right] and dp[left+1][right-1]:
                    dp[left][right] = True
                    palindrome = (left, right)

        return s[palindrome[0]:palindrome[-1]+1]
