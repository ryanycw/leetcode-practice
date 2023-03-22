#
# @lc app=leetcode id=116 lang=python
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root:
            return root

        def traverse(leftNode, rightNode):
            if not leftNode:
                return
            leftNode.next = rightNode
            traverse(leftNode.left, leftNode.right)
            traverse(rightNode.left, rightNode.right)
            traverse(leftNode.right, rightNode.left)

        traverse(root.left, root.right)

        return root

        # @lc code=end
