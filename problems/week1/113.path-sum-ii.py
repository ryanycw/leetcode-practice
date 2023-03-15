#
# @lc app=leetcode id=113 lang=python
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        self.ans = []

        def traverse(node, prevNodes):
            if not node:
                return

            copyNodes = list(prevNodes)
            copyNodes.append(node.val)

            if not node.right and not node.left:
                if sum(copyNodes) == targetSum:
                    self.ans.append(copyNodes)

            traverse(node.left, copyNodes)
            traverse(node.right, copyNodes)

        traverse(root, [])

        return self.ans

# @lc code=end
