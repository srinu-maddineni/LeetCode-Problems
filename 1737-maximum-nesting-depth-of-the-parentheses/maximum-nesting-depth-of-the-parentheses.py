class Solution:
    def maxDepth(self, s: str) -> int:
        mx = 0
        stk = 0
        for i in range(len(s)):
            if s[i] == '(':
                stk+=1
                mx = max(stk,mx)
            elif s[i] == ')':
                stk-=1
        return mx