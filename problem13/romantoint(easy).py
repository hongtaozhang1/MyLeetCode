__author__ = 'hongtao'

class Solution:
    def romanToInt(self, s):
        numbers = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        # s = s[::-1]
        # last = None
        # ans = 0
        #
        # for x in s:
        #     if last and numbers[x] < numbers[last]:
        #         ans -= 2 * numbers[x]
        #     ans += numbers[x]
        #     last = x

        ans = 0
        for i in range(len(s)):
            if i< len(s)-1:
                if numbers[s[i]] < numbers[s[i+1]]:
                    ans -= numbers[s[i]]
                else:
                    ans += numbers[s[i]]
            else:
                ans += numbers[s[i]]
        return ans

solution = Solution()
print solution.romanToInt("MC")