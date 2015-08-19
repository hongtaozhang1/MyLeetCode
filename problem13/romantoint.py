__author__ = 'hongtao'
class Solution:
    def romanToInt(self, s):
        i = 0
        ans = 0
        while i < len(s):
            if s[i] == "M":
                ans += 1000
                i += 1
            elif s[i] == "D":
                ans += 500
                i += 1
            elif s[i] == "C":
                if i < len(s) -1:
                    if s[i+1] == "M":
                        ans += 900
                        i += 2
                    elif s[i+1] == "D":
                        ans += 400
                        i += 2
                    else:
                        ans += 100
                        i += 1
                else:
                    ans += 100
                    i += 1
            elif s[i] == "L":
                ans += 50
                i += 1
            elif s[i] == "X":
                if i < len(s) -1:
                    if s[i+1] == "C":
                        ans += 90
                        i += 2
                    elif s[i+1] == "L":
                        ans += 40
                        i += 2
                    else:
                        ans += 10
                        i += 1
                else:
                    ans += 10
                    i += 1
            elif s[i] == "V":
                ans += 5
                i += 1
            elif s[i] == "I":
                if i < len(s)-1:
                    if s[i+1] == "X":
                        ans += 9
                        i += 2
                    elif s[i+1] == "V":
                        ans += 4
                        i += 2
                    else:
                        ans += 1
                        i += 1
                else:
                    ans += 1
                    i += 1

        return ans

solution = Solution()
print solution.romanToInt("")