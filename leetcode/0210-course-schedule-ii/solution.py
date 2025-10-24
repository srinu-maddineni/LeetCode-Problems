class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for u , v in prerequisites:
            graph[u].append(v)
        unvisit, visit,visited = 0,1,2
        state = [unvisit] * numCourses
        result = []
        def dfs(node):
            s = state[node]
            if s == visited: return True
            if s == visit : return False
            state[node] = visit
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            state[node] = visited
            result.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return result
        
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
