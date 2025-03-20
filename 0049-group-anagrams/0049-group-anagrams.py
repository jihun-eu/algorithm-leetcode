class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        UNICODE_a = ord('a')
        ALPHABET_COUNT = 26

        anagrams = defaultdict(list)
        for string in strs:
            alphabets = [0] * ALPHABET_COUNT
            for char in string:
                alphabets[ord(char) - UNICODE_a] += 1
            anagrams[tuple(alphabets)].append(string)
        
        return list(anagrams.values())