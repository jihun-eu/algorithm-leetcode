class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        size = len(boxes)
        intBoxes = [int(box) for box in boxes]
        operations = [0] * size

        oneCnt = 0
        for i in range(1, size):
            operations[i] = operations[i-1] + oneCnt + intBoxes[i-1]
            oneCnt += intBoxes[i-1]

        suffix = oneCnt= 0
        for i in range(-1, -size, -1):
            suffix += oneCnt + intBoxes[i]
            oneCnt += intBoxes[i]
            operations[i-1] += suffix

        return operations