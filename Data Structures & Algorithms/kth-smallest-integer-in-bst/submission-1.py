# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        c = k
        res = root.val

        def dfs(root):
            nonlocal c, res
            if not root:
                return

            dfs(root.left)
            if c == 0:
                return
            
            c -= 1
            if c == 0:
                res = root.val
                return
            dfs(root.right)
        
        dfs(root)
        return res