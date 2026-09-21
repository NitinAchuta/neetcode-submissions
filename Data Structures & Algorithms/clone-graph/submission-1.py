"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copyMap = {}
        if not node:
            return None

        def dfs(node):
            if node in copyMap:
                return copyMap[node]
            copyMap[node] = Node(node.val) 
            for neighbor in node.neighbors:
                dfs(neighbor)
                copyMap[node].neighbors.append(copyMap[neighbor])
            return copyMap[node]
        dfs(node)
        return copyMap[node]
                
        
                



        