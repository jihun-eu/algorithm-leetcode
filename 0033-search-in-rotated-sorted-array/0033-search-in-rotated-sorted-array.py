class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # try it again
        front = 0
        tail = len(nums) - 1

        while front <= tail:
            mid = (front + tail) // 2
            print(front, tail, mid)
            if nums[mid] == target:
                return mid
            
            if nums[front] <= nums[mid]:
                if nums[front] <= target <= nums[mid]:
                    tail = mid - 1
                else:
                    front = mid + 1
            else:
                if nums[mid] <= target <= nums[tail]:
                    front = mid + 1
                else:
                    tail = mid - 1
        return -1