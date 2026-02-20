class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        while len(s)>2:
            s1 =''
            for i in range(1,len(s)):
                s1+=str((int(s[i])+int(s[i-1]))%10)
            s=s1
        if s[1] == s[0]:
            return True
        else:
            return False


        
