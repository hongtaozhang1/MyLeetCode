__author__ = 'hongtao'
class Solution():
    def isMatch(self, s, p):
        f = [ [False for i in range(len(p)+1)] for j in range(len(s)+1)]

        f[0][0] = True
        for i in range(1, len(p)+1):
            if p[i-1] == "*":
                if i >= 2:
                    f[0][i] = f[0][i-2]

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == "." or s[i-1] == p[j-1]:
                    f[i][j] = f[i-1][j-1]
                elif p[j-1] == "*":
                    f[i][j] = f[i][j-1] or f[i][j-2] or (f[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == "."))

        return f[len(s)][len(p)]

solution = Solution()
print solution.isMatch("aaa", "a*b")