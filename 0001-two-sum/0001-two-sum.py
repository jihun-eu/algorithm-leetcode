class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        visited = {}
        size = len(nums)

        for i, num in enumerate(nums):
            sub = target - num
            if sub in visited:
                return [i, visited[sub]]
                
            visited[num] = i
