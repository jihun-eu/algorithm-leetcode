class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        substrings = []

        words.sort(key=len)

        for i in range(len(words)-1):
            for compare in words[i+1:]:
                if words[i] in compare:
                    substrings.append(words[i])
                    break
        
        return substrings