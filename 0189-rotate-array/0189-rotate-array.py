class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        rotated = [0] * length

        for i in range(length):
            rotated[(i+k) % length] = nums[i]

        for i in range(length):
            nums[i] = rotated[i]