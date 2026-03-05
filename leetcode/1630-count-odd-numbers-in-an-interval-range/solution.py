class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # c =0
        
        # if low %2 != 0:
        #     c+=1
       
        # c+=(high-low)//2
        # if (high - low)%2!= 0:
        #     if high %2 !=0:
        #         c+=1
        # return c
        return ((high+1)//2)-low//2

        
