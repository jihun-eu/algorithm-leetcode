class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
        totalXor = reduce(lambda x, y: x ^ y, derived)
        return totalXor == 0