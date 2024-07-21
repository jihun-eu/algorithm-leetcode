class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        # version 1
        # remaining_capacity = list(map(lambda x: x[0] - x[1], zip(capacity, rocks)))

        # version 2
        remaining_capacity = [capacity[i] - rocks[i] for i in range(len(capacity))]
        remaining_capacity.sort()

        count = 0
        for free_space in remaining_capacity:
            if additionalRocks < free_space:
                break
            additionalRocks -= free_space
            count += 1
        return count