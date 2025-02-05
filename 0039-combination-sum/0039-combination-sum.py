class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtracking(idx, combination, total):
            nonlocal candidates, target, combinations
            if total == target:
                combinations.append(combination.copy())
                return

            if total > target or idx >= len(candidates):
                return

            combination.append(candidates[idx])
            backtracking(idx, combination, total + candidates[idx])
            combination.pop()
            backtracking(idx+1, combination, total)

        backtracking(0, [], 0)
        return combinations