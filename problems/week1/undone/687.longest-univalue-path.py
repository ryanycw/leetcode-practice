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

        def traverse(node):
            if not node:
                return None, 0

            cumm = 0

            leftVal, leftCumm = traverse(node.left)
            rightVal, rightCumm = traverse(node.right)

            if leftVal == node.val and rightVal == node.val:
                cumm = leftCumm + rightCumm + 1
            elif leftVal == node.val:
                cumm = leftCumm + 1
            elif rightVal == node.val:
                cumm = rightCumm + 1

            self.ans = max(cumm, self.ans)

            return node.val, cumm

        traverse(root)

        return self.ans
        # @lc code=end
