class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # solve it again
        length = len(nums)
        answer = [1] * length
        
        for i in range(1, length):
            answer[i] *= answer[i-1]* nums[i-1]

        suffix = 1
        for i in range(length-2, -1, -1):
            suffix *= nums[i+1]
            answer[i] *= suffix

        return answer
