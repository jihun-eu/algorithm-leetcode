class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        size = len(nums)
        visited = [False] * size
        
        permutations = []

        def backtracking(permutation: List[int]):
            nonlocal size, visited, permutations
            if len(permutation) == size:
                permutations.append(permutation.copy())
                return
            
            for i in range(size):
                if visited[i]: continue
                visited[i] = True
                permutation.append(nums[i])
            
                backtracking(permutation)
            
                visited[i] = False
                permutation.pop()
        
        backtracking([])
        return permutations

