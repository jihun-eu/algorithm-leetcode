class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_prod = min_prod = result = nums[0]
        
        for num in nums[1:]:
            tmp_max = max_prod * num
            tmp_min = min_prod * num

            max_prod = max(tmp_max, tmp_min, num)
            min_prod = min(tmp_max, tmp_min, num)
            
            result = max(max_prod, result)

        return result