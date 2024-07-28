class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2: return n
        memory = [0, 1, 1]
        
        for i in range(n-2):
            tmp = memory[2]
            memory[2] = sum(memory)
            memory[0] = memory[1]
            memory[1] = tmp
        return memory[-1]
        