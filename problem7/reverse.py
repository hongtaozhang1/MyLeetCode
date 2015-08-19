__author__ = 'hongtao'
class Solution:
    def reverse(self, x):
        e = 1
        flag = 0
        if x < 0:
            flag = 1
        x = abs(x)
        while x / e != 0:
            e *= 10
        e /= 10

        ans = 0
        while x!= 0:
            ans += (x % 10) * e
            x /= 10
            e /= 10
        if ans > 4294967295:
            return 0
        if flag == 1:
            return 0-ans
        else:
            return ans

solution = Solution()
print solution.reverse(-123235234)
