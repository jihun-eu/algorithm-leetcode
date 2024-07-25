class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_prod = nums[0]
        min_prod = nums[0]
        curr_prod = nums[0]
        
        for num in nums[1:]:
            
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(max_prod * num, num)
            min_prod = min(min_prod * num, num)

            curr_prod = max(max_prod, curr_prod)
        
        return curr_prod

            