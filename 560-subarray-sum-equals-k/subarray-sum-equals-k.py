class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = {}
        m[0] = 1 
        s = 0
        res =0
        for i in range(len(nums)):
            s +=nums[i]
            
            if s-k in m:
                res+=m[s-k]
            # if s not in m:
            m[s] = m.get(s,0)+1
        return res

        