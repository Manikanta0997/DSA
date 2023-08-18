# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.li = []
    def max_depth(self, root):
        if root == None:
            return 0
        return 1+max(self.max_depth(root.left), self.max_depth(root.right))
    def diameterOfBinaryTree(self, root):
        if root == None:
            return
        if root.left != None and root.right != None:
            le = self.max_depth(root.left)
            re = self.max_depth(root.right)
        elif root.left == None:
            le = 0
            re = self.max_depth(root.right)
        elif root.right == None:
            le = self.max_depth(root.left)
            re = 0
        self.li.append(abs(le + re))
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        return max(self.li)
        