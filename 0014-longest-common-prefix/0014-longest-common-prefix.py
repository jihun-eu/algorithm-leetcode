class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return None

        minLength = min(len(s) for s in strs)
        commonPrefix = ""

        sampleString = strs[0]
        left = 1
        right = minLength
        while left <= right:
            mid = (left + right) // 2
            if all(s.startswith(sampleString[:mid]) for s in strs[1:]):
                commonPrefix = sampleString[:mid]
                left = mid + 1
            else:
                right = mid - 1
        
        return commonPrefix



            
            