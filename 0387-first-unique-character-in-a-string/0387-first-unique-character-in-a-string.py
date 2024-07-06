class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hashmap = {}
        
        for c in s:
            if c not in hashmap:
                hashmap[c] = 0
            hashmap[c] += 1
            
        index = 0
        for key in s:
            if hashmap[key] == 1:
                return index
            index += 1
        
        return -1