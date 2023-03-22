#
# @lc app=leetcode id=669 lang=python
#
# [669] Trim a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """

        def traverse(node):
            if not node:
                return None

            elif node.val > high:
                return traverse(node.left)

            elif node.val < low:
                return traverse(node.right)

            else:
                node.left = traverse(node.left)
                node.right = traverse(node.right)
                return node

        return traverse(root)

# @lc code=end
