# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        if not root: return []
        ans,queue = [],[root]
        while queue:
            queueNext,level = [],[]
            for node in queue:
                level.append(node.val)
                if node.left:
                    queueNext.append(node.left)
                if node.right:
                    queueNext.append(node.right)
            queue = queueNext
            ans.insert(0,level)
        return ans


n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

n1 = None
a = Solution()
print a.levelOrderBottom(n1)