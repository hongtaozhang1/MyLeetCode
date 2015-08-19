__author__ = 'hongtao'
class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        ans = ""
        for i in range(numRows):
            j = i
            flag = 1
            if i==0 or i==numRows-1:
                while j < len(s):
                    ans += s[j]
                    j += 2*numRows - 2
            else:
                while j < len(s):
                    ans += s[j]
                    if flag ==1 :
                        j += 2*(numRows-1-i)
                        flag = 0
                    else:
                        j += 2*i
                        flag = 1
        return ans

solution = Solution()
print solution.convert("PAYPALISHIRING", 3)

