class Solution:
    def myAtoi(self, s: str) -> int:
        minInt = -2 << 30
        maxInt = (2 << 30) - 1

        noWhitespace = s.lstrip()
        sign = 1
        index = 0
        if len(noWhitespace) == 0: return 0
        if noWhitespace[0] == '-':
            sign = -1
            index = 1
        elif noWhitespace[0] == '+':
            index = 1
        
        result = 0
        while index < len(noWhitespace) and noWhitespace[index].isdigit(): 
            digit = int(noWhitespace[index])
            result = result * 10 + digit
            index += 1
            if result > maxInt:
                return maxInt if sign == 1 else minInt
        
        return result * sign