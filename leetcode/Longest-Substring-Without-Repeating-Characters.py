#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tStr, rStr = '', ''
        length = len(s)
        for i in range(length):
            if s[i] not in tStr:
                tStr += s[i]
            else:
                ind = tStr.index(s[i])
                tStr = tStr[ind+1:] + s[i]
            if len(tStr) > len(rStr):
                rStr = tStr
        return len(rStr)


if __name__ == '__main__':
    s = 'pwwkew'
    solut = Solution()
    long = solut.lengthOfLongestSubstring(s)
    print(long)
