class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        table = {5:0, 10:0, 20:0}
        for bill in bills:
            table[bill] += 1

            charge = bill - 5
            if charge == 15:
                if table[10] > 0 and table[5] > 0:
                    table[10] -= 1
                    table[5] -= 1
                elif table[5] > 2:
                    table[5] -= 3
                else:
                    return False
            if charge == 5:
                if table[5] > 0:
                    table[5] -= 1
                else:
                    return False
        return True
