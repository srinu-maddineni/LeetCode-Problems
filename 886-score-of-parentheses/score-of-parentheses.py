class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]
        # ans = 0
        k=-1
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(0)
            else:
                x = stk.pop()
                if x==0:
                    ans=1
                else:
                    ans=2*x
                
                stk[-1] += ans

        return stk[0]
