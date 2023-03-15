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

        if not root or (not root.left and not root.right):
            return root

        def traverse(node):
            if not node.left and not node.right:
                return

            node.left.next = node.right

            traverse(node.right)
            traverse(node.left)

        traverse(root)

        """
        leftTree = root.left
        rightTree = root.right
        while leftTree.right:
            leftTree = leftTree.right
            rightTree = rightTree.left
            leftTree.next = rightTree
        """

        return root

        # @lc code=end
