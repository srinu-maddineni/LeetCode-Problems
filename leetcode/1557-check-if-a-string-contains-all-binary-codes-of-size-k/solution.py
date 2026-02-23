class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        sol = set()
        for i in range(len(s)):
            s1=s[i:k+i]
            if len(s1) == k:
                sol.add(s1)
        return len(sol) == 2**k
        
        
