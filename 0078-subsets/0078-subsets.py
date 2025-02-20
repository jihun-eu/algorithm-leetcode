class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        uniqSubsets = []
        limit = len(nums)
        def backtracking(idx: int, subset: List[int]) -> List[int]:
            nonlocal nums, uniqSubsets, limit
            if limit <= idx:
                uniqSubsets.append(subset.copy())
                return
            subset.append(nums[idx])
            backtracking(idx+1, subset)
            subset.pop()
            backtracking(idx+1, subset)
        
        backtracking(0, [])
        return uniqSubsets
