# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        res = [root.val]
        
        def dfs(root):
            if not root:
                return 0
            else:
                left_max = dfs(root.left)
                right_max = dfs(root.right)
                left_max = max(0, left_max)
                right_max = max(0, right_max)
                res[0] = max(res[0], left_max+right_max + root.val)
                return root.val + max(right_max, left_max)
        dfs(root)
        return res[0]
                