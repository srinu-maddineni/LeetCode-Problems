class Solution:
    def minOperations(self, s: str) -> int:
        if sorted(s) == list(s):
            return 0
        if len(s) ==2:
            return -1

        if sorted(s) == list(s):
            return 0
        
        mn =min(s)
        mx =max(s)
        print((len(s)//2)-1)
        if s[0] == mn or s[-1] ==mx:
            return 1
        elif mn in s[:-1] or mx in s[1:]:
            return 2
        else:
            return 3
        print(mx,mn)