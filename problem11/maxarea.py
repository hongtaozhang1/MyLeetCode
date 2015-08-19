__author__ = 'hongtao'
class Solution:
    def maxArea(self, height):
        ans = 0
        i = 0
        j = len(height)-1
        while i < j:
            lh = height[i]
            rh = height[j]
            area = (j-i) * min(lh, rh)
            ans = max(ans, area)
            if rh <= lh:
                while j-1 >= i and height[j-1] <= rh:
                    j -= 1
                j -= 1
                rh = height[j]
            else:
                while i+1 <= j and height[i+1] <= lh:
                    i += 1
                i += 1
                lh = height[i]
        return ans

solution = Solution()
print solution.maxArea([2,4,1,3])