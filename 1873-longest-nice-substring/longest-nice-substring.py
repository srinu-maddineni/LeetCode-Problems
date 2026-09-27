class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        res= ''
        for i in range(n):
            seen = set()
            for j in range(i,n):
                seen.add(s[j])
                v = True
                for k in seen:
                    if k.isupper():
                        if k.lower() not in seen:
                            v = False 
                            break
                    else:
                        if k.upper() not in seen:
                            v = False
                            break
                if v and (j-i+1)> len(res):
                    res = s[i:j+1]
        return res



















