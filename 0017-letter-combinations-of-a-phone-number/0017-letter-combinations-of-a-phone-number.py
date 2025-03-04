class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        buttons = {
            "2":['a','b','c'],
            "3":['d','e','f'],
            "4":['g','h','i'],
            "5":['j','k','l'],
            "6":['m','n','o'],
            "7":['p','q','r','s'],
            "8":['t','u','v'],
            "9":['w','x','y','z']
        }
        combinations = []
        def getCombinations(combination: str, idx: int) -> List[str]:
            nonlocal digits, combinations
            if idx == len(digits):
                combinations.append(combination)
                return
            for char in buttons[digits[idx]]:
                getCombinations(combination+char, idx+1)

            return
        getCombinations('', 0)
        return combinations
