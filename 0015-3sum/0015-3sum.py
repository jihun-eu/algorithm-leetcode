class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = []
        nums.sort()

        for target_idx, target in enumerate(nums[:-2]):
            if target > 0: break
            if target_idx > 0 and target == nums[target_idx-1]: 
                continue

            left = target_idx + 1
            right = len(nums) - 1
            while left < right:
                triplet_sum = target + nums[left] + nums[right]
                if triplet_sum > 0:
                    right -= 1
                elif triplet_sum < 0:
                    left += 1
                else:
                    triplets.append([target, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]: left += 1
        return triplets
