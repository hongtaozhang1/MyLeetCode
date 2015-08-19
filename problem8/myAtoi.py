__author__ = 'hongtao'
class Solution:
    def myAtoi(self, str):
        neg = 0
        flag = 0
        ans = 0
        s = ""
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        str = str.strip(" ")
        if str == "":
            return 0
        else:
            i = 0
            while i < len(str):
                if str[i] not in numbers:
                    if flag == 1:
                        break
                    else:
                        if str[i] == "+":
                            i += 1
                            flag = 1
                        elif str[i] == "-":
                            neg = 1
                            flag = 1
                            i += 1
                        else:
                            break
                else:
                    s += str[i]
                    i += 1
        if s == "":
            return 0
        while s[0] == "0" and len(s)>1:
            s = s[1:]
        e = 1
        for i in range(len(s)):
            ans += (ord(s[len(s)-i-1]) - ord("0")) * e
            e *= 10
        if neg == 1:
            if 0-ans < INT_MIN:
                return INT_MIN
            else:
                return 0-ans
        else:
            if ans > INT_MAX:
                return INT_MAX
            else:
                return ans

solution = Solution()
print solution.myAtoi("    +0 000010")