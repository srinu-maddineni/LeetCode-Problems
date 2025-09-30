class Solution(object):
    def triangularSum(self, nums):
        if len(nums)==1:
            return nums[0]
        newnums = []
        # i=0
        # while i<len(nums)-1:
        #     newNums = []
        #     for j in range(1,len(nums)):
        #         newNums.append((nums[j-1]+nums[j])%10)
        #     nums=newNums
        #     i+=1
        #     print(nums)
        # return nums[0]

        for i in range(1,len(nums)):
            newnums.append((nums[i-1]+nums[i])%10)
        return self.triangularSum(newnums)

        
        """
        :type nums: List[int]
        :rtype: int
        """
        
