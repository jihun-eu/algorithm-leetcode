class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        ALPHABET_COUNT = 26
        UNICODE_a = ord("a")

        def countAlphabets(word):
            nonlocal ALPHABET_COUNT, UNICODE_a
            
            alphabetCnt = [0] * ALPHABET_COUNT
            for c in word:
                alphabetCnt[ord(c) - UNICODE_a] += 1
            
            return alphabetCnt

        subsetAlphabetCnt = [0] * ALPHABET_COUNT
        for word in words2:
            for i, count in enumerate(countAlphabets(word)):
                subsetAlphabetCnt[i] = max(subsetAlphabetCnt[i], count)

        universalStrings = []
        for word in words1:
            if all(x >= y for x, y in zip(countAlphabets(word), subsetAlphabetCnt)):
                universalStrings.append(word)
        
        return universalStrings