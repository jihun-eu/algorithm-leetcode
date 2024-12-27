class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        size = len(nums)
        nums.sort()

        tmp = nums[0] - 1
        for i in range(size - 2):
            target = nums[i]
            if tmp == target:
                continue
                
            left = i + 1
            right = size - 1

            while left < right:
                tmp_sum = target + nums[left] + nums[right]
                if tmp_sum < 0:
                    left += 1
                elif tmp_sum > 0:
                    right -= 1
                else:
                    result.append([target, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]: left += 1
                    left += 1
            
            tmp = target
        
        return result
