class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = minProd = maxProd = nums[0]
        for i in range(1, len(nums)):
            tmp = (nums[i], minProd * nums[i], maxProd * nums[i])
            minProd, maxProd = min(tmp), max(tmp)
            result = max(result, maxProd)

        return result