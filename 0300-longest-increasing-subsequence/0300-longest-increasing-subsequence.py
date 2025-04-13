class Solution:

    def binarySearch(self, nums: List[int], target: int) -> None:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left


    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [nums[0]]
        maxLength = 1
        for i in range(1, len(nums)):
            if LIS[-1] < nums[i]:
                LIS.append(nums[i])
            else:
                idx = self.binarySearch(LIS, nums[i])
                LIS[idx] = nums[i]
        return len(LIS)
            