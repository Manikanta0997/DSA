# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def diameter(root, depth):
            nonlocal ans 
            if not root:
                return 0
            left = diameter(root.left, depth)
            right = diameter(root.right, depth)
            ans = max(ans, left +  right)
            return max(left, right) + 1
            
        diameter(root, 0)
        return ans
        