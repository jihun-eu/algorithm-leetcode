class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        steps = [2, 3]
        for i in range(n - 3):
            tmp = steps[1]
            steps[1] = sum(steps)
            steps[0] = tmp

        return steps[1]
        