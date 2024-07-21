class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        capacity.sort()

        filled = 0
        for box in capacity[::-1]:
            if apples <= 0:
                break
            filled += 1
            apples -= box
        return filled