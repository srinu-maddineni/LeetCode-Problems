class Solution:
    def checkValidString(self, s: str) -> bool:
        stk1= 0
        stk2 = 0
        for i in range(len(s)):
            if s[i] == '(':
                stk1+=1
                stk2+=1
            elif s[i] == ')':
                stk1-=1
                stk2-=1
            else:
                stk1-=1
                stk2+=1
            
            if stk2<0:
                return False
            stk1 = max(stk1,0)
                
        # print(stk1 ,stk2)
        return stk1 ==0