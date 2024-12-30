class Solution:
    
    mask = 0xffffffff
    maxInt = 2 ** 31 - 1

    def getSum(self, a: int, b: int) -> int:
        a &= Solution.mask
        b &= Solution.mask
        if b == 0:
            return a if a < Solution.maxInt else ~(a ^ Solution.mask)
        return self.getSum(a ^ b, (a & b) << 1)