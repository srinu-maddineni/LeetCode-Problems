class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2 !=0:
            return False
        stk = 0

        for i in range(len(s)):
            if locked[i] == '1':
                if s[i] == '(':
                    stk+=1
                else:
                    stk-=1
            else:
                stk+=1

            if stk<0:
                return False
        stk=0
        for i in range(len(s)-1,-1,-1):
            if locked[i] == '1':
                if s[i] == ')':
                    stk+=1
                else:
                    stk-=1
            else:
                stk+=1

            if stk<0:
                return False

        
        return True