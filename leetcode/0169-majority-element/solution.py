class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h ={


        }
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i] =1
        for i in nums:
            if h[i] > len(nums)/2:
                return i
                
        
