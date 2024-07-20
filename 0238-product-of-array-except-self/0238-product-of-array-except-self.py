class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length
        for i in range(length-1):
            answer[i+1] = answer[i] * nums[i]
        suffix = 1
        for i in range(length-1, 0, -1):
            suffix *= nums[i]
            answer[i-1] *= suffix

        return answer