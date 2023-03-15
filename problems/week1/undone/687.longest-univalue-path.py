#
# @lc app=leetcode id=687 lang=python
#
# [687] Longest Univalue Path
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = float('-inf')

        def traverse(node, cummCount, prevVal):
            if not node:
                return
            traverse(node.left, cummCount, node.val)
            if node.val == prevVal:
                cummCount += 1
            else:
                cummCount = 0

            self.ans = max(self.ans, cummCount)
            traverse(node.right, cummCount, node.val)

        traverse(root, 0, None)

        return self.ans
        # @lc code=end
