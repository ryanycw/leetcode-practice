#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.ans = True
        self.prev = None

        def traverse(node):
            if not node:
                return
            traverse(node.left)

            if self.prev and node.val <= self.prev.val:
                self.ans = False

            self.prev = node
            traverse(node.right)

        traverse(root)

        return self.ans

# @lc code=end
