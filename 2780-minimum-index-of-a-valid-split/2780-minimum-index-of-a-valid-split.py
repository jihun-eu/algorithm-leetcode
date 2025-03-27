class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counter = Counter(nums)
        mostCommonVal, mostCommonFreq = counter.most_common(1)[0]
        if mostCommonFreq * 2 < len(nums):
            return -1

        leftMostCommonFreq = 0
        idx = -1
        for i in range(len(nums)):
            leftSideCount = i + 1
            if nums[i] == mostCommonVal:
                leftMostCommonFreq += 1
                mostCommonFreq -= 1
            if leftSideCount < leftMostCommonFreq * 2 and (len(nums) - leftSideCount) < mostCommonFreq * 2:
                idx = i
                break

        return idx
            
