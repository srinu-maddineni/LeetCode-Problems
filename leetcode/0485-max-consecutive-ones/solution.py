class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k = 0
        i =0
        while i<len(nums):
            j = i
            m =0
            while j< len(nums) and nums[j] != 0:
                m+=1
                j+=1
            while j <len(nums) and nums[j] == 0  :
                j+=1
            i = j
            if k<m:
                k = m
        return k


             
        
