class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(arr: List[int], target: int):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False

        flatten_matrix = [el for arr in matrix for el in arr]
        return binarySearch(flatten_matrix, target)
