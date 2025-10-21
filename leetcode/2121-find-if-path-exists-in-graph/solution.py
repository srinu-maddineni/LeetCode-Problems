class Solution(object):
    def validPath(self, n, edges, source, destination):
        if source == destination: return True
        seen = set()
        graph = defaultdict(list)
        stk = [source]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        while stk:
            node = stk.pop()
            if node == destination:
                return True
            for inf in graph[node]:
                if inf not in seen:
                    seen.add(inf)
                    stk.append(inf)
        return False


                


        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
