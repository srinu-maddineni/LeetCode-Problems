class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        if len(s) == 1:
            return s
        if s == s[::-1]:
            return s
        
        s1 = ""
        l=""
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                s1 = s[i:j]
                if s1 == s1[::-1] and len(s1)>len(l):
                    l = s1
        return l



        
