class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ALPHABET_COUNT = 26
        UNICODE_A = 97
        size = len(s)
        dp = [0] * size

        for start, end, direction in shifts:
            adder = 1 if direction else -1
            dp[start] = (dp[start] + adder) % ALPHABET_COUNT
            
            end += 1
            if end < size:
                dp[end] = (dp[end] + ALPHABET_COUNT - adder) % ALPHABET_COUNT

        for i in range(1, size):
            dp[i] = (dp[i] + dp[i-1]) % ALPHABET_COUNT
        
        shifted = ''
        for i in range(size):
            shifted += chr(((ord(s[i]) - UNICODE_A + dp[i]) % ALPHABET_COUNT) + UNICODE_A)

        return shifted