class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        queue = deque([0])
        seen = set()

        while queue:
            start = queue.popleft()
            if start == len(s):
                return True

            for end in range(start+1, len(s)+1):
                if end in seen or s[start:end] not in wordSet: continue
                queue.append(end)
                seen.add(end)

        return False