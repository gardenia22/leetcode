# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {integer[]}

    def preorderTraversal(self, root):
        self.preorder = []
        self.traverse(root)
        return self.preorder

    def traverse(self, root):
        if root:
            self.preorder.append(root.val)
            self.traverse(root.left)
            self.traverse(root.right)
