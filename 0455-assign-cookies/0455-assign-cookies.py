class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        contents = 0
        child, cookie = 0, 0

        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
                contents += 1
            cookie += 1
        
        return contents


            