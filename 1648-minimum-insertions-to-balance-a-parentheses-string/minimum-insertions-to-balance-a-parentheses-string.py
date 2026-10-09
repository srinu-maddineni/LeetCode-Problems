class Solution:
    def minInsertions(self, s: str) -> int:
        
        stk = []
        ans = 0 
        i = 0
        while i<len(s):
            if s[i] == '(':
                stk.append('(')
                i+=1
            else :
                if i+1 <len(s) and s[i+1] == ')':
                    if len(stk) == 0:
                        ans+=1
                    else:
                        stk.pop()
                    i+=2
                else:
                    if len(stk) == 0:
                        ans+=2
                    else:
                        stk.pop()
                        ans+=1
                    i+=1
        ans+= len(stk)*2
        return ans

