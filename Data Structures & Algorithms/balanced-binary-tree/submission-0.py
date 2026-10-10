# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        balance = True
        
        def dfs(root: TreeNode) -> int:
            nonlocal balance
            if not root.left and not root.right:
                return 0
            
            left, right = 0 , 0

            if root.left:
                left = dfs(root.left) + 1
            if root.right:
                right = dfs(root.right) + 1
            
            balance = balance and abs(left - right) <= 1
            return max(left, right)
        dfs(root)
        return balance
