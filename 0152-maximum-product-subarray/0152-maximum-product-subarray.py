class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        result = nums[0]
        size = len(nums)

        left_product = 1
        right_product = 1
        for i in range(size):
            left_product *= nums[i]
            right_product *= nums[-1-i]

            result = max(result, left_product, right_product)

            left_product = left_product or 1
            right_product = right_product or 1

        return result