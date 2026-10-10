# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        if not root:
            return 0
        def dfs(root: Optional[TreeNode]) -> int:
            if not root.left and not root.right:
                return 0
            nonlocal maxDiameter
            left, right = 0, 0
            if root.left:
                left = dfs(root.left) + 1
            if root.right:
                right = dfs(root.right) + 1
            maxDiameter = max(maxDiameter, left + right)
            return max(left, right)
        dfs(root)
        return maxDiameter