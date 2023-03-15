#
# @lc app=leetcode id=106 lang=python
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        # [leftTree root rightTree]
        # [leftTree rightTree root]

        hashmap = {}
        for idx, val in enumerate(inorder):
            hashmap[val] = idx

        def createSubtree(inorder, inStart, inEnd, postorder, postStart, postEnd):
            if postEnd < postStart:
                return None

            rootVal = postorder[postEnd]
            index = hashmap[rootVal]
            leftSize = index-inStart

            root = TreeNode(rootVal)
            root.left = createSubtree(
                inorder, inStart, index-1, postorder, postStart, postStart+leftSize-1)
            root.right = createSubtree(
                inorder, index+1, inEnd, postorder, postStart+leftSize, postEnd-1)
            return root

        return createSubtree(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)

# @lc code=end
