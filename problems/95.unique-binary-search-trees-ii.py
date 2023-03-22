#
# @lc app=leetcode id=95 lang=python
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def buildTree(low, high):
            res = []

            if low > high:
                return [None]

            for rootVal in range(low, high+1):
                leftTreeCombination = buildTree(low, rootVal-1)
                rightTreeCombination = buildTree(rootVal+1, high)
                for leftTree in leftTreeCombination:
                    for rightTree in rightTreeCombination:
                        res.append(TreeNode(rootVal, leftTree, rightTree))

            return res

        return buildTree(1, n)

# @lc code=end
