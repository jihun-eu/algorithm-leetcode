class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: sum(el ** 2 for el in x) ** 0.5)[:k]
