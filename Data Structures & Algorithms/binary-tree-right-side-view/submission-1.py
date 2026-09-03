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
            for i in range(len(q)):
                curr = q.popleft()
                if i == prevLen - 1:
                    res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            prevLen = len(q)
        
        return res
                
        