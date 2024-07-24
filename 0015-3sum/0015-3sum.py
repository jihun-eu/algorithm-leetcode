class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for target_idx in range(len(nums)-2):
            if target_idx > 0 and nums[target_idx] == nums[target_idx-1]: continue
            
            left = target_idx + 1
            right = len(nums) - 1

            while left < right:
                tmp = nums[target_idx] + nums[left] + nums[right]
                if tmp > 0:
                    right -= 1
                elif tmp < 0:
                    left += 1
                else:
                    triplet = [nums[target_idx], nums[left], nums[right]]
                    results.append(triplet)
                    left += 1
                    while nums[left] == nums[left-1] and left < right: left += 1

        return results

