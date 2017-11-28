#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
'''

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        self.res = []
        self.findSum(candidates,[],target,0)
        return self.res

    def findSum(self, candidates, sublist, target, last):
        if target == 0:
            self.res.append(sublist[:])
        if target < candidates[0]:
            return
        for n in candidates:
            if n > target:
                return
            if n < last:
                continue
            sublist.append(n)
            self.findSum(candidates,sublist,target - n, n)
            sublist.pop()

if __name__ == '__main__':
    candidates = [2,3,6,7]
    solut = Solution()
    res = solut.combinationSum(candidates, 7)
    print(res)
