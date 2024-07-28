class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        if length < 3:
            return min(cost)

        for i in range(2, length):
            cost[i] = min(cost[i] + cost[i-1], cost[i] + cost[i-2])
        
        return min(cost[-2:])