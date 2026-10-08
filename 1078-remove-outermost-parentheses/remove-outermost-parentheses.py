class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stk = []
        l=0
        r = []
        for i in range(len(s)):
            if l==0 and len(r)>0:
                stk.append(''.join(r))
                r = []
            if s[i] =='(':
                l+=1
                r.append('(')
            else:
                l-=1
                r.append(')')
        stk.append(''.join(r))
        res = []
        for i in range(len(stk)):
            res.append(stk[i][1:-1])

        return ''.join(res)
