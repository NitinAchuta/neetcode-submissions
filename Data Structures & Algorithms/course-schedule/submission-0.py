class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # dfs bc you must find all courses in reverse, one at a time
        preMap = {i: [] for i in range(numCourses)} # adjacency list of i's prereqs

        for post, pre in prerequisites:
            preMap[post].append(pre)

        visited = set()
        def dfs(node):
            if len(preMap[node]) == 0:
                return True
            
            for preReq in preMap[node]:
                if preReq in visited:
                    return False
                visited.add(preReq)
                if not dfs(preReq): return False
                visited.remove(preReq)
            preMap[node] = []
            return True
            
        for key,value in preMap.items():
            if not dfs(key):
                return False
        return True






