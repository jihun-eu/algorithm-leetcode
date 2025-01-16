class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        isNums1Odd = len(nums1) & 1
        isNums2Odd = len(nums2) & 1
        if not(isNums1Odd | isNums2Odd):
            return 0
        
        nums1Xor = reduce(lambda x, y: x ^ y, nums1)
        nums2Xor = reduce(lambda x, y: x ^ y, nums2)
        
        if isNums1Odd & isNums2Odd:
            return nums1Xor ^ nums2Xor
        if isNums1Odd & 1:
            return nums2Xor ^ 0
        if isNums2Odd & 1:
            return nums1Xor ^ 0