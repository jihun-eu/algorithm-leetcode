class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        zeroPointer = nonZeroPointer = 0
        while nonZeroPointer < size and zeroPointer < size:
            if nums[zeroPointer] != 0:
                zeroPointer += 1
                continue
            if nums[nonZeroPointer] == 0:
                nonZeroPointer += 1
                continue

            if nonZeroPointer < zeroPointer:
                nonZeroPointer = zeroPointer + 1
            else:
                nums[zeroPointer], nums[nonZeroPointer] = nums[nonZeroPointer], nums[zeroPointer]
            