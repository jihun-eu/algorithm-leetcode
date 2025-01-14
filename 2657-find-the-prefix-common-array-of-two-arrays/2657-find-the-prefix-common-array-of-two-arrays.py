class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        size = len(A)
        prefixCommonArray = [0] * size
        numCnt = [0] * (size + 1)

        numCnt[A[0]] += 1
        numCnt[B[0]] += 1

        if A[0] == B[0]:
            prefixCommonArray[0] += 1

        for i in range(1,size):
            numCnt[A[i]] += 1
            numCnt[B[i]] += 1
            
            adder = 1 if A[i] == B[i] else (numCnt[A[i]] // 2) + (numCnt[B[i]] // 2)

            prefixCommonArray[i] = prefixCommonArray[i-1] + adder

        return prefixCommonArray

