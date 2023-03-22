#
# @lc app=leetcode id=99 lang=python
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        self.wrongNodeA = None
        self.wrongNodeB = None
        self.prev = None

        # value of inorder traversed BST should be sorted
        # there will be two errors in the inorder traversal
        # store the large one in the first error
        # store the smaller one in the second error
        def traverse(node):
            if not node:
                return

            traverse(node.left)

            if self.prev and node.val < self.prev.val:
                if not self.wrongNodeA:
                    self.wrongNodeA = self.prev
                self.wrongNodeB = node

            self.prev = node

            traverse(node.right)

        traverse(root)
        self.wrongNodeA.val, self.wrongNodeB.val = self.wrongNodeB.val, self.wrongNodeA.val

# @lc code=end
