class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        c = 0
        seen =1
        prev = 0

        for i in range(1,n):
            if s[i] == s[i-1]:
                seen+=1
            else:
                c += min(seen,prev)
                prev = seen
                seen =1
        c+=min(seen,prev)
        return c

        
