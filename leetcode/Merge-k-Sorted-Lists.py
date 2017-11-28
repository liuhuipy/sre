#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        temp, indx = nums[0], 0
        for i in range(1, len(nums)):
            if nums[i] > temp:
                temp = nums[i]
            else:
                indx = i
                break
        if self.searchTwo(nums[:indx], target) == -1:
            if self.searchTwo(nums[indx:], target) == -1:
                return -1
            else:
                return self.searchTwo(nums[indx:], target) + indx
        else:
            return self.searchTwo(nums[:indx], target)

    def searchTwo(self, nums, target):
        if not nums:
            return -1
        if target > max(nums) or target < min(nums):
            return -1
        length = len(nums)
        l, r = 0, length - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    solut = Solution()
    res = solut.search(nums, 6)
    print(res)
