class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        m = {}
        for i ,s1 in enumerate(s):
            if s1 not in m:
                m[s1] = []
            m[s1].append(i)
        sol = -1
        for arr in m.values():
            if len(arr)>=2:
                sol=max(sol,(arr[-1]-arr[0])-1)
        return sol
        
        
