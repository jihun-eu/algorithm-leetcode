class Solution:

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        size = len(words)
        vowels = "aeiou"
        wordScores = [0] * (size + 1)

        for i in range(size):
            wordScores[i+1] = wordScores[i] + (1 if words[i][0] in vowels and words[i][-1] in vowels else 0)

        ans = []
        for l, r in queries:
            ans.append(wordScores[r+1] - wordScores[l])

        return ans
            
