__author__ = 'hongtao'
class Solution:
    def longestCommonPrefix(self, strs):
        strs.sort(key=len)
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0]), 0, -1):
            flag = True
            for j in range(1, len(strs)):
                if strs[j][0:i] != strs[0][0:i]:
                    flag = False
                    break
            if flag == True:
                return strs[0][0:i]

        return ""

solution = Solution()
strs = ["a", "b"]
print solution.longestCommonPrefix(strs)


