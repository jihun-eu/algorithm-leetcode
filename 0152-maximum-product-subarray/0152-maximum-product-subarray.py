class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # try it again
        length = len(nums)
        min_prod = nums[0]
        max_prod = nums[0]
        answer = nums[0]

        for num in nums[1:]:
            if num < 0:
                min_prod, max_prod = max_prod, min_prod
            min_prod = min(min_prod * num, num)
            max_prod = max(max_prod * num, num)
            answer = max(answer, max_prod)
            
        return answer
                
                

