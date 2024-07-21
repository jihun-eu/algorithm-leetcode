class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        table = {5:0, 10:0, 20:0}
        for bill in bills:
            table[bill] += 1

            charge = bill - 5
            while charge > 0:
                for change in [10, 5]:
                    if change > charge:
                        continue
                    if table[change] == 0:
                        if change == 5:
                            return False
                        continue
                    charge -= change
                    table[change] -= 1

        return True
