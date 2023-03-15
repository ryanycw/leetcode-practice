#
# @lc app=leetcode id=124 lang=python
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # took quite a fex fixes

        self.ans = float('-inf')

        if not root:
            return root.val

        def traverse(node):
            if not node:
                return 0

            leftMax = traverse(node.left) + node.val
            rightMax = traverse(node.right) + node.val
            self.ans = max(leftMax, rightMax, leftMax +
                           rightMax-node.val, node.val, self.ans)

            return max(leftMax, rightMax, node.val)

        traverse(root)

        return self.ans
# @lc code=end
