#
# @lc app=leetcode id=111 lang=python
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = float('inf')

        if not root:
            return 0

        def traverse(node, depth):
            if not node:
                return

            if not node.left and not node.right:
                self.ans = min(self.ans, depth+1)

            traverse(node.left, depth+1)
            traverse(node.right, depth+1)

        traverse(root, 0)

        return self.ans

# @lc code=end
