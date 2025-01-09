class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        UNICODE_ZERO = ord("0")

        binarySum = ""
        indexA = len(a) - 1
        indexB = len(b) - 1

        carryBit = 0
        while indexA >= 0 or indexB >= 0 or carryBit:
            if indexA >= 0:
                carryBit += ord(a[indexA]) - UNICODE_ZERO
            indexA -= 1
            if indexB >= 0:
                carryBit += ord(b[indexB]) - UNICODE_ZERO
            indexB -= 1
            
            binarySum = str(carryBit & 1) + binarySum
            carryBit = carryBit // 2

        return binarySum