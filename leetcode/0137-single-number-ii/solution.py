class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        h ={}
        for n in nums:
            if n not in h:
                h[n] = 1
            else:
                h[n] +=1
        print(h)
        for i in h:
            if h[i] ==1:
                return i


        
