class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # dfs bc you must find all courses in reverse, one at a time
        preMap = {i: [] for i in range(numCourses)} # adjacency list of i's prereqs

        for post, pre in prerequisites:
            preMap[post].append(pre)

        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if preMap[node] == []:
                return True
            visited.add(node)
            for crs in preMap[node]:
                if not dfs(crs):
                    return False
            visited.remove(node)
            preMap[node] = []
            return True

        for key, value in preMap.items():
            if not dfs(key):
                return False
        return True

