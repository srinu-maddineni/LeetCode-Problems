class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans =0
        stk =0
        for i in range(len(s)):
            if s[i] == '(':
                stk+=1
            else:
                if stk ==0:
                    ans+=1
                else:
                    stk-=1
        return ans+stk
        