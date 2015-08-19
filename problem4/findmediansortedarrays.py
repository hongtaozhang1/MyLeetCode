class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        i = 0
        j = 0
        m = len(nums1)
        n = len(nums2)
        nums_all = []
        while i<m and j<n:
            if nums1[i] < nums2[j]:
                nums_all.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                nums_all.append(nums2[j])
                j += 1
            else:
                nums_all.append(nums1[i])
                nums_all.append(nums2[j])
                i += 1
                j += 1
        else:
            while i<m:
                nums_all.append(nums1[i])
                i += 1
            while j<n:
                nums_all.append(nums2[j])
                j += 1
        if ( m + n ) % 2 != 0:
            return float( nums_all[ (m+n-1)/2 ])
        else:
            return float( float( nums_all[ (m+n)/2 ] + nums_all[ (m+n-1)/2 ] )/2 )

solution = Solution()
print solution.findMedianSortedArrays([1,2,3],[4,5,6])
