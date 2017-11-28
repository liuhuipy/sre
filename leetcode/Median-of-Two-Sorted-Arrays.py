#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if (m + n) % 2 == 1:
            return self.getKth(nums1, nums2, (m + n) // 2 + 1)
        else:
            return (self.getKth(nums1, nums2, (m + n) // 2) + self.getKth(nums1, nums2, (m + n) // 2 + 1)) / 2

    def getKth(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.getKth(nums2, nums1, k)
        if m == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        pa = min(k//2, m)
        pb = k - pa
        if nums1[pa - 1] <= nums2[pb - 1]:
            return self.getKth(nums1[pa:], nums2, pb)
        else:
            return self.getKth(nums1, nums2[pb:], pa)


if __name__ == '__main__':
    A = [1,3,5,7]
    B = [2,4,6,8,9,10]
    solut = Solution()
    res = solut.findMedianSortedArrays(A, B)
    print(res)
