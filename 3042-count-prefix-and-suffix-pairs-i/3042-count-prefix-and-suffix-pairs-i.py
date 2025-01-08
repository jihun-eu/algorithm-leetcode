class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pairsCnt = 0
        for i, subString in enumerate(words[:-1]):
            for word in words[i+1:]:
                if not word.startswith(subString) or not word.endswith(subString):
                    continue
                pairsCnt += 1

        return pairsCnt