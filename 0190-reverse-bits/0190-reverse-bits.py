class Solution:
    def reverseBits(self, n: int) -> int:

        reverseBit = 0
        for _ in range(32):
            reverseBit = (reverseBit << 1) | (n & 1)
            n = n >> 1

        return reverseBit
