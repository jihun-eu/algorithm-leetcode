class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        front = 0
        tail = len(nums) - 1

        while front < tail:
            mid = (front + tail) // 2
            if nums[mid] > nums[tail]:
                front = mid + 1
            else:
                tail = mid
        
        rotated = front
        orderd_nums = nums[rotated:] + nums[:rotated]

        front = 0
        tail = len(nums) - 1
        while front < tail:
            mid = (front + tail) // 2
            if orderd_nums[mid] < target:
                front = mid + 1
            else:
                tail = mid
        target_index = (front + rotated) % len(nums)
        if nums[target_index] == target:
            return target_index
        else:
            return -1