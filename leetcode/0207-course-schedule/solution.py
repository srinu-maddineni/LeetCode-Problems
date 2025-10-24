class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for u , v in prerequisites:
            graph[v].append(u)
        unvisit = 0
        visit   =1
        visited = 2
        state = [unvisit] * numCourses
        def dfs(node):
            s = state[node]
            if s == visited: return True
            if s == visit: return False
            state[node] = visit
            for nei in graph[node]:
                if not dfs(nei): 
                    return False
            state[node] = visited
            return True
        for i in range(numCourses):
            if not dfs(i): return False
        return True
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
