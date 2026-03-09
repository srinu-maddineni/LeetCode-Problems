class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        n =n+1
        while True:
            c = Counter(str(n))
            c1=0
            for key,val in c.items():
                if int(key) !=val:
                    break
                else:
                    c1+=1
            if c1==len(c):
                return n
            n+=1
        
