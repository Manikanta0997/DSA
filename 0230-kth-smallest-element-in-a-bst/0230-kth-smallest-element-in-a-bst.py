# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.li = []
    def kthSmallest(self, root, k):
        def hello(root):
            if root == None:
                return
            self.li.append(root.val)
            hello(root.left)
            hello(root.right)
        hello(root)
        self.li.sort()
        return self.li[k-1]
        
        
        