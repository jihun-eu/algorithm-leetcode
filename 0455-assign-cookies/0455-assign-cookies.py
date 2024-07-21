class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        contents = 0
        child, jar = len(g)-1, len(s)-1
        while child >= 0 and jar >= 0:
            print(child, jar)
            if g[child] <= s[jar]:
                jar -= 1
                contents += 1
            child -= 1
        
        return contents


            