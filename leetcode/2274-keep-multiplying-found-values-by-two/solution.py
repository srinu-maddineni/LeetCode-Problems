class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
         
        t =True
        while t:
            if original in nums:
                original *=2
            else:
                return original
        
