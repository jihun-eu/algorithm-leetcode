class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        contents = 0
        while g and s:
            if g[-1] <= s[-1]:
                s.pop()
                contents += 1
            g.pop()
        
        return contents


            