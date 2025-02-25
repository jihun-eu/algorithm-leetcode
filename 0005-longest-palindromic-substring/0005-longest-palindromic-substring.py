class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        palindrome = (0, 1)
        length = len(s)
        
        isPalindrome = [[False] * length for _ in range(length)]
        for i in range(length):
            isPalindrome[i][i] = True

        for i in range(length-1):
            if s[i] == s[i+1]:
                isPalindrome[i][i+1] = True
                palindrome = (i, i+2)
        
        for windowSize in range(2, length):
            for left in range(length-windowSize):
                right = left + windowSize
                if s[left] == s[right] and isPalindrome[left+1][right-1]:
                    isPalindrome[left][right] = True
                    palindrome = (left, right+1)

        return s[palindrome[0]:palindrome[1]]
