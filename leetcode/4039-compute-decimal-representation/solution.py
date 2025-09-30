class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        k=str(n)
        r =[]
        for i ,d in enumerate(k):
            val =int(d)*10**(len(k)-i-1)
            if val !=0:
                r.append(val)
        return r
            
            
        
        
