class Solution(object):
    def buildArray(self, nums):
        ans = []
        k = nums
        for i in range(len(nums)):
            ans.append(nums[k[i]])

        return ans
            
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
