__author__ = 'hongtao'
class Solution:
    def fourSum(self, nums, target):
        ans = []
        sum_hash = {}
        nums.sort()
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] not in sum_hash:
                    sum_hash[nums[i]+nums[j]] = [[i, j]]
                else:
                    sum_hash[nums[i]+nums[j]].append([i, j])

        for i in range(0, len(nums)-3):
            for j in range(i+1, len(nums)-2):
                if target - nums[i] - nums[j] in sum_hash:
                    for numlist in sum_hash[target - nums[i] - nums[j]]:
                        if numlist[0] > j:
                            tmp = [nums[i], nums[j], nums[numlist[0]], nums[numlist[1]]]
                            if tmp not in ans:
                                ans.append(tmp)



        return ans

solution = Solution()
print solution.fourSum([1, 0, -1, 0, -2, 2], 0)

