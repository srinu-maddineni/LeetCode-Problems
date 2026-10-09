class Solution:
    def minInsertions(self, s: str) -> int:
        
        stk = 0
        ans = 0 
        i = 0
        while i<len(s):
            if s[i] == '(':
                stk+=1
                i+=1
            else :
                if i+1 <len(s) and s[i+1] == ')':
                    if stk == 0:
                        ans+=1
                    else:
                        stk-=1
                    i+=2
                else:
                    if stk == 0:
                        ans+=2
                    else:
                        stk-=1
                        ans+=1
                    i+=1
        ans+=stk*2
        return ans

