class Solution:
    def minimumLength(self, s: str) -> int:
        
        ALPHABET_COUNT = 26
        UNICODE_a = 97
        
        alphabetCnt = [0] * ALPHABET_COUNT
        for char in s:
            index = ord(char) - UNICODE_a
            alphabetCnt[index] += 1
        
        minLength = 0
        for count in alphabetCnt:
            while count > 2:
                count = (count // 3) + (count % 3)
            minLength += count
        
        return minLength
