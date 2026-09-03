# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        
        def backtracking(root, currSum):
            if not root:
                return False

            currSum += root.val
            print(root.val, currSum, "\n")
            if not root.left and not root.right and currSum  == targetSum:
                return True
            elif not root.left and not root.right:
                return False

            leftVal = False
            rightVal = False
            if root.left:
                leftVal = backtracking(root.left, currSum)
            if root.right:
                rightVal = backtracking(root.right, currSum)
            return leftVal or rightVal
        
        return backtracking(root, 0)
                

        