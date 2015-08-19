class Solution:

    def getLongest(self, s, l, r):
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                return s[l+1: r]
            else:
                l -= 1
                r += 1
        else:
            return s[l+1: r]
    def longestPalindrome(self, s):
        # palindromeLen = len(s)
        # while palindromeLen > 0:
        #     for i in range(0, len(s) - palindromeLen +1):
        #         j = i
        #         flag = True
        #         while (j < (i + palindromeLen/2)):
        #             if s[j] != s[palindromeLen + 2*i -j - 1]:
        #                 flag = False
        #                 break
        #             else:
        #                 j += 1
        #         if flag is True:
        #             return s[i: i+palindromeLen]
        #     else:
        #         palindromeLen -= 1
        maxLen = 0
        ans = ""
        for i in range(0, len(s)):

            tempStr = self.getLongest(s, i, i)
            if maxLen < len(tempStr):
                maxLen = len(tempStr)
                ans = tempStr
            if i < len(s)-1 and s[i] == s[i+1] :
                tempStr = self.getLongest(s, i, i+1)
                if maxLen<len(tempStr):
                    maxLen = len(tempStr)
                    ans = tempStr

        return ans
solution = Solution()
s = "abbbaaaabbbbb"
print solution.longestPalindrome(s)


