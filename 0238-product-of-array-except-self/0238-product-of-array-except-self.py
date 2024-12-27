class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        products = [1] * size

        for i in range(size-1):
            products[i+1] = products[i] * nums[i]

        suffix = 1
        for i in range(size-1, -1, -1):
            products[i] *= suffix
            suffix *= nums[i]

        return products