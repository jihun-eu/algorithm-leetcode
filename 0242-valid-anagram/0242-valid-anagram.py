class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        UNICODE_A = 97

        alphabetScore = [0] * 26

        for c in s:
            alphabetScore[ord(c) - UNICODE_A] += 1

        for c in t:
            alphabetScore[ord(c) - UNICODE_A] -= 1

        for score in alphabetScore:
            if score != 0:
                return False
        return True