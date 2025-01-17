class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return [newInterval]
        
        newIntervals = []
        visited = 0
        size = len(intervals)

        # First, fill intervals that doesn't overlapped
        while visited < size and intervals[visited][1] < newInterval[0]:
            newIntervals.append(intervals[visited])
            visited += 1

        # Second, assemble the intervals that overlapped with newInterval
        while visited < size and intervals[visited][0] <= newInterval[1]:
            newInterval = [min(intervals[visited][0], newInterval[0]), max(intervals[visited][1], newInterval[1])]
            visited += 1

        newIntervals.append(newInterval)

        # Third, fill intervals left
        while visited < size:
            newIntervals.append(intervals[visited])
            visited += 1

        return newIntervals