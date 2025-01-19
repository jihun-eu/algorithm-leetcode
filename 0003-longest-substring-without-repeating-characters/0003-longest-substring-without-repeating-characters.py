class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = set()
        max_size = 0
        _length = len(s)
        start_point = 0
        end_point = 0

        while end_point < _length:
            if s[end_point] in tmp:
                while True:
                    if s[start_point] == s[end_point]:
                        start_point += 1
                        break
                    tmp.remove(s[start_point])
                    start_point += 1
                    
            tmp.add(s[end_point])
            end_point += 1
            max_size = max(end_point - start_point, max_size)

        return max_size
