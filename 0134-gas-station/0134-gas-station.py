class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        
        start = 0
        tmp = 0
        for i in range(len(gas)):
            tmp += gas[i] - cost[i]
            if tmp < 0:
                tmp = 0
                start = i + 1
        return start