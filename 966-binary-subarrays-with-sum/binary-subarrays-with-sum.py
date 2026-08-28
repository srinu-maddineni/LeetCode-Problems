class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        m = {0:1}
        pre = 0
        res=0
        for i in range(len(nums)):
            pre+=nums[i]
            t = pre-goal
            if t in m:
                res+=m[t]
            m[pre] = m.get(pre,0)+1
        return res
