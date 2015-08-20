__author__ = 'hongtao'
class Solution:
    def threeSum(self, nums):
        # ans = []
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         k = 0 - nums[i] - nums[j]
        #         tmp = [nums[i], nums[j], k]
        #         tmp.sort()
        #         if k in nums and tmp not in ans:
        #             ans.append(tmp)
        # return ans

        nums.sort()
        ans = []
        for i in range(len(nums)-1):
            if i ==0 or nums[i] >nums[i-1]:
                l = i+1
                r = len(nums)-1
                neg = -nums[i]
                while (l < r):
                    if nums[l]+nums[r] == neg:
                        ans.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l<r and nums[l] == nums[l-1]:
                            l += 1
                        while l<r and nums[r] == nums[r+1]:
                            r -= 1

                    elif nums[l]+nums[r] < neg:
                        l += 1
                    else:
                        r -= 1

        return ans


solution = Solution()
nums = [-1, 0, 1, 2, -1, 2]
print solution.threeSum(nums)