class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        num = []
        i = 0


        while i<len(nums)-2:
            if i>0 and nums[i] == nums[i-1]:
                i+=1
                continue
            j=i+1
            k = len(nums)-1
            while j<k:
                r = nums[i]+nums[j]+nums[k]
                if r == 0 :

                    num.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j-1] :
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1

                elif r < 0:
                    j+=1
                else:
                    k-=1
            i+=1
        return num

                
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
