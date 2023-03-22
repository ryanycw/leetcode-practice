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
        self.ans = 0

        def traverse(node):
            if not node:
                return 0

            leftCumm = traverse(node.left)
            rightCumm = traverse(node.right)

            leftCumm = leftCumm + 1 if node.left and node.left.val == node.val else 0
            rightCumm = rightCumm + 1 if node.right and node.right.val == node.val else 0

            self.ans = max(self.ans, rightCumm + leftCumm)

            return max(rightCumm, leftCumm)

        traverse(root)

        return self.ans
        # @lc code=end
