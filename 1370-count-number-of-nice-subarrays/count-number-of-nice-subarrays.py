class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i  in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        print(nums)
        m = {0:1}
        pre =0
        res =0
        for i in range(len(nums)):
            pre+=nums[i]

            r = pre-k
            if r in m:
                res+=m[r]
            m[pre] = m.get(pre,0)+1
        return res
        