# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        minBadVersion = 1
        lastVersion = n

        while minBadVersion < lastVersion:
            mid = (minBadVersion + lastVersion) // 2
            if isBadVersion(mid):
                lastVersion = mid
            else:
                minBadVersion = mid + 1

        return minBadVersion