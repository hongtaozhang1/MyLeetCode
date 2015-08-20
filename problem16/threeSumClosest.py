__author__ = 'hongtao'
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        mindiff = 10000000000
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums) -1
            while l<r:
                diff = target - nums[i] - nums[l] - nums[r]
                if diff == 0:
                    return target
                if diff > 0:
                    l += 1
                if diff < 0:
                    r -= 1
                if abs(diff) < abs(mindiff):
                    mindiff = diff

        return target - mindiff

solution = Solution()
print solution.threeSumClosest([-1, 2, 1, -4], 1)