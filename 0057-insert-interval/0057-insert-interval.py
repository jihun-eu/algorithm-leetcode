class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return [newInterval]
        
        # first you need to find overlapped intervals with newInterval from the intervals list
        # second you need to merge them to one
        newIntervals = []
        visited = 0
        size = len(intervals)

        while visited < size and intervals[visited][1] < newInterval[0]:
            newIntervals.append(intervals[visited])
            visited += 1

        while visited < size and intervals[visited][0] <= newInterval[1]:
            newInterval = [min(intervals[visited][0], newInterval[0]), max(intervals[visited][1], newInterval[1])]
            visited += 1

        newIntervals.append(newInterval)

        while visited < size:
            newIntervals.append(intervals[visited])
            visited += 1

        return newIntervals

        
        f
        
        