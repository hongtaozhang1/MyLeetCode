__author__ = 'hongtao'
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        l = 1
        r = 10
        while x / r != 0:
            r *= 10
        r /= 10
        while r >= l:
            if (x/r)%10 != (x/l)%10:
                return False
            else:
                r /= 10
                l *= 10
        return True

solution = Solution()
print solution.isPalindrome(000123100)