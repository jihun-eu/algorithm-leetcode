class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap: return ""

        values = self.hashMap[key]
        if timestamp < values[0][1]: return ""
        
        left, right = 0, len(values)-1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] == timestamp: return values[mid][0]

            if values[mid][1] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        return values[right][0]
        



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)