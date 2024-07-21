class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        contents = 0
        child, cookie = len(g)-1, len(s)-1
        while child >= 0 and cookie >= 0:
            if g[child] <= s[cookie]:
                cookie -= 1
                contents += 1
            child -= 1
        
        return contents


            