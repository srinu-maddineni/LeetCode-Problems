class Solution(object):
    def removeElement(self, nums, val):
        n = len(nums)
        j = n-1
        swap = 0
        for  i in range(n):
            if nums[i] == val:
                swap+=1
        i=0
        while i<j:
            while nums[i] != val and i<j:
                i+=1
            while nums[j] == val and j>i:
                j-=1
            if i >= j: break
            nums[i] , nums[j] = nums[j] , nums[i]

        return n- swap
     
        
        

        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
