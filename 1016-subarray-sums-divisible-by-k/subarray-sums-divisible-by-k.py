class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m ={0:1}
        pre = 0
        res =0
        for i in range(len(nums)):
            pre+=nums[i]
            r = pre%k
            if r in m:
                res+=m[r]
            
            m[r]=m.get(r,0)+1
        print(m)
        return res
        