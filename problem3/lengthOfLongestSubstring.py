class Solution:
    def lengthOfLongestSubstring(self, s):
        i = 0
        j = 0
        ans = 0
        sub = []
        while i<len(s) and j<len(s):
            if s[j] in sub:
                if ans <len(sub):
                    ans = len(sub)
                flag = sub.index(s[j])
                i += flag + 1
                sub = sub[flag+1:]
            else:
                sub.append(s[j])
                j += 1
        else:
            if ans < len(sub):
                ans = len(sub)
        return ans



solution = Solution()
s = "abcdah"
print solution.lengthOfLongestSubstring(s)
