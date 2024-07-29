class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        step1 = 1
        step2 = 1
        for i in range(1, n):
            tmp = step1
            step1 = step1 + step2
            step2 = tmp
        return step1
        