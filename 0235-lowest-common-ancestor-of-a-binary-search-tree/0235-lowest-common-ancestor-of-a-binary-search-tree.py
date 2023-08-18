# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ro = None
    def lowestCommonAncestor(self, root, p, q):
        if p.val > q.val:
            temp = p
            p = q
            q = temp
        if root.val > p.val and root.val < q.val:
            return root
        elif root.val > p.val and root.val > q.val:
            z = self.lowestCommonAncestor(root.left, p, q)
            return z
        elif root.val < p.val and root.val < q.val:
            z = self.lowestCommonAncestor(root.right, p, q)
            return z
        elif root.val == p.val:
            return root
        elif root.val == q.val:
            return root
        
            