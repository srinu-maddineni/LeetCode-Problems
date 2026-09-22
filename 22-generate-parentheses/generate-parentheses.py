class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans ,s=[],[]
        
        def  back(o,c):
            if len(s) == 2*n:
                ans.append(''.join(s))
                return
            
            if o <n:
                s.append('(')
                back(o+1,c)
                s.pop()
            if c<o:
                s.append(')')
                back(o,c+1)
                s.pop()

        back(0,0)
        return ans
            
            
