class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        steps = [3, 5]
        for _ in range(n - 3):
            steps[0], steps[1] = steps[1], sum(steps)

        return steps[0]