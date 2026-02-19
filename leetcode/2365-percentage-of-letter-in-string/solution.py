class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c = 0
        for i in range(len(s)):
            if s[i] == letter:
                c+=1
        return (c*100//len(s))
        
