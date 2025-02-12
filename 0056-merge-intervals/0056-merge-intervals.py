class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        newIntervals = []
        for interval in intervals:
            if not newIntervals or newIntervals[-1][1] < interval[0]:
                newIntervals.append(interval)
            else:
                newIntervals[-1][1] = max(newIntervals[-1][1], interval[1])
        
        return newIntervals
