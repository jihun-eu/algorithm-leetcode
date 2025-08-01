class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        size = len(nums)

        for idx in range(size):
            num = nums[idx]
            
            if num in tmp:
                return [tmp[num], idx]
            
            pairNum = target - num
            tmp[pairNum] = idx
            
        return []