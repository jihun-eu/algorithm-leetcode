class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        step = [1, 1]
        for i in range(1, n):
            tmp = step[1]
            step[1] = sum(step)
            step[0] = tmp
        return step[1]
        