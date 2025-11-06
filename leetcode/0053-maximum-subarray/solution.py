class Solution(object):
    def maxSubArray(self, nums):
        max_sum = curr = nums[0]
        for i in nums[1:]:
            curr = max(i,curr+i)
            max_sum = max(curr,max_sum)

        return max_sum
        """
        :type nums: List[int]
        :rtype: int
        """
        
