class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}

        # i=0
        # j = len(nums)-1
        # while i<j:
        #     x = nums[i] +nums[j]
        #     if x == target:
        #         return [i,j]
        #     elif x > target:
        #         j-=1
        #     else:
        #         i+=1
        for i in range(len(nums)):
            t = target - nums[i]
            if t in m:
                return [i,m[t]]
            else:
                m[nums[i]] = i
        