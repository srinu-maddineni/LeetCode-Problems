class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [ i for i in range(1,m+1)]
        rel = []
        for i in queries:
            k=p.index(i)
            rel.append(k)
            r=p.pop(k)
            p.insert(0,r)
        return rel
        
        
