__author__ = 'hongtao'
class Solution:
    def isMatch(self, s, p):
        if len(p) == 0:
            return len(s) == 0
        if len(p) == 1 or p[1] != "*":
            if len(s) == 0 or (s[0] != p[0] and p[0] != ".") :
                return False
            return self.isMatch(s[1:], p[1:])
        else:
            i = -1
            length = len(s)
            while (i < length) and (i < 0 or p[0] == "." or s[i] == p[0]):
                if self.isMatch(s[i+1:], p[2:]):
                    return True
                i += 1
            return False

solution = Solution()
print solution.isMatch("aaa", "a*b")

