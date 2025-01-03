class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        LIS = [nums[0]]

        for num in nums[1:]:
            if LIS[-1] < num:
                LIS.append(num)
            else:
                start = 0
                end = len(LIS)
                while start < end:
                    mid = (start + end) // 2
                    if LIS[mid] < num:
                        start = mid + 1
                    else:
                        end  = mid
                LIS[start] = num

        return len(LIS)
            
            