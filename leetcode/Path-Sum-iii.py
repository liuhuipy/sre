#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'

'''
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.resNum = 0
        self.findSum(root, sum)
        return self.resNum

    def findSum(self, root, sum):
        print(root.val, sum)
        if root.val == sum:
            self.resNum += 1
            return
        if root.left:
            self.findSum(root.left, sum - root.val)
        if root.right:
            self.findSum(root.right, sum - root.val)


if __name__ == '__main__':
    node1 = TreeNode(10)
    node2 = TreeNode(5)
    node3 = TreeNode(-3)
    node4 = TreeNode(3)
    node5 = TreeNode(2)
    node6 = TreeNode(11)
    node7 = TreeNode(3)
    node8 = TreeNode(-2)
    node9 = TreeNode(1)

    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.right = node6
    node4.left, node4.right = node7, node8
    node5.right = node9

    solut = Solution()
    resNum = solut.pathSum(node1, 8)
    print(resNum)
