class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        maxLength = 0
        countMap = {0: -1}
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count in countMap:
                currLength = i - countMap[count]
                maxLength = max(maxLength, currLength)
            else:
                countMap[count] = i

        return maxLength