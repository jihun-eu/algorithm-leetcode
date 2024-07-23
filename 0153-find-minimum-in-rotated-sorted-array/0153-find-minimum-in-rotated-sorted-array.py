class Solution:
    def findMin(self, nums: List[int]) -> int:
        front = 0
        tail = len(nums) - 1
        
        while front < tail:
            mid = (front + tail) // 2
            if nums[mid] > nums[tail]:
                front = mid + 1
            else:
                tail = mid
        return nums[tail]