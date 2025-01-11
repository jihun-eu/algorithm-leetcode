class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = []
        for num in range(n+1):
            count = 0
            while num:
                count += num & 1
                num = num >> 1
            counts.append(count)

        return counts

# 0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 