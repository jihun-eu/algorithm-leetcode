class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tmp = nums[0]
        max_value = nums[0]
        for num in nums[1:]:
            tmp = max(tmp + num, num)
            max_value = max(max_value, tmp)

        return max_value
