# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        q = collections.deque()
        res = []
        q.append(root)

        if not root:
            return res

        while len(q) > 0:
            prevLen = len(q)
            rightSide = None
            for i in range(prevLen):
                curr = q.popleft()
                if curr:
                    rightSide = curr.val
                    q.append(curr.left)
                    q.append(curr.right)
            if rightSide:
                res.append(rightSide)
        
        return res
                
        