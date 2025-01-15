class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1BitCnt = self.getBitCnt(num1)
        num2BitCnt = self.getBitCnt(num2)

        if num1BitCnt == num2BitCnt:
            return num1

        return self.flipBit(num1, abs(num1BitCnt-num2BitCnt), num2BitCnt - num1BitCnt < 0)

    def getBitCnt(self, num):
        cnt = 0

        while num:
            num = num & (num - 1)
            cnt += 1

        return cnt

    def flipBit(self, num, cnt, flag):
        bitmask = 1

        while cnt:
            if bool(num & bitmask) == flag:
                num = num ^ bitmask
                cnt -= 1
            bitmask = bitmask << 1
            
        return num
        