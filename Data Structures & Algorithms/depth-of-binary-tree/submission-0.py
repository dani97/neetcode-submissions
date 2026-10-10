# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        depth = 0
        while len(queue) > 0:
            depth += 1
            currentNodes = len(queue)
            print(queue, depth, currentNodes)
            
            for i in range(currentNodes):
                node  = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return depth

