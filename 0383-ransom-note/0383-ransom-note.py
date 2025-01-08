class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ALPHABET_COUNT = 26
        UNICODE_A = 97
        
        alphabetCounter = [0] * ALPHABET_COUNT

        for char in magazine:
            alphabetCounter[ord(char) - UNICODE_A] += 1

        for char in ransomNote:
            index = ord(char) - UNICODE_A
            alphabetCounter[index] -= 1
            if alphabetCounter[index] < 0:
                return False
        
        return True
