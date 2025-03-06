class Solution:
    ALPHABET_COUNT = 26
    UNICODE_A = ord('a')

    
    def isAnagrams(self, list1: List[int], list2: List[int]) -> bool:
        return list1 == list2

    def findAnagrams(self, s: str, p: str) -> List[int]:

        anagrams = []

        windowSize = len(p)
        if len(s) < windowSize:
            return anagrams

        answer = [0] * Solution.ALPHABET_COUNT
        counter = [0] * Solution.ALPHABET_COUNT
        for i in range(len(p)):
            answer[ord(p[i]) - Solution.UNICODE_A] += 1
            counter[ord(s[i]) - Solution.UNICODE_A] += 1

        if answer == counter:
            anagrams.append(0)

        for i in range(len(s)-windowSize):
            counter[ord(s[i]) - Solution.UNICODE_A] -= 1
            counter[ord(s[i+windowSize]) - Solution.UNICODE_A] += 1
            if answer == counter:
                anagrams.append(i+1)

        return anagrams
