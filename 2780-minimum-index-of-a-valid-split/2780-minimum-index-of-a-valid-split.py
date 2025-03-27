class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counter = Counter(nums)
        mostCommonVal, mostCommonFreq = counter.most_common(1)[0]
        if mostCommonFreq * 2 < len(nums):
            return -1

        count = 0
        for i in range(len(nums)):
            total = i + 1
            if nums[i] == mostCommonVal:
                count += 1
                mostCommonFreq -= 1
            if total < count * 2 and (len(nums) - total) < mostCommonFreq * 2:
                return total - 1

        return -1
            
