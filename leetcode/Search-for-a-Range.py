#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp, l = 0, -1
        for i in range(len(nums)):
            if nums[i] == target and temp == 0:
                temp = 1
                l = i
            elif nums[i] == target and temp != 0:
                temp += 1
            else:
                pass
        if l != -1:
            return [l, l+temp-1]
        else:
            return [-1, -1]

if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    solut = Solution()
    res = solut.searchRange(nums, 8)
    print(res)
