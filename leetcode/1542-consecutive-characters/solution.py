class Solution:
    def maxPower(self, s: str) -> int:
        sol = 0
        i = 0
        j=i+1
        while i<len(s) and j<len(s):
            if s[i] == s[j]:
                sol = max(sol,j-i+1)
                j+=1
            else:
                i=j
                j=i+1
        if sol == 0:
            return 1
        return sol
        
