#There are two sorted arrays nums1 and nums2 of size m and n respectively.
#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#Example 1:
#nums1 = [1, 3]
#nums2 = [2]
#The median is 2.0
#Example 2:
#nums1 = [1, 2]
#nums2 = [3, 4]
#The median is (2 + 3)/2 = 2.5

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        median = 0
        nums1 = sorted(nums1 + nums2)
        middle = len(nums1)//2
        if len(nums1)%2 == 1:
            median = nums1[middle]
        else:
            median = (nums1[middle]+nums1[middle-1])/2
        return median

sol = Solution()
nums1 = [1,2]
nums2 = [3,4]
median = sol.findMedianSortedArrays(nums1, nums2)
print(median)
