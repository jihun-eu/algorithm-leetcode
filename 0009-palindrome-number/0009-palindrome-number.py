class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x < 10: return True

        reverse = 0
        tmp = x
        while tmp:
            reverse = (10 * reverse) + (tmp % 10)
            tmp //= 10

        return x == reverse