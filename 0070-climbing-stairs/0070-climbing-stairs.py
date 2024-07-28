class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        memory = [1, 2]
        for i in range(2, n):
            memory.append(memory[i-1] + memory[i-2])
        return memory[n-1]
        