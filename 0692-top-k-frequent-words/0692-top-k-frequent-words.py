class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        frequency = defaultdict(int)
        for word in words:
            frequency[word] += 1
        
        topKFreq = sorted(frequency, key=lambda x: (-frequency[x], x))[:k]
        
        return topKFreq