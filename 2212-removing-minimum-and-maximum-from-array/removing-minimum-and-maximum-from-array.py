class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        h = 0
        l_v=nums[0]
        h_v=nums[0]
        for i in range(len(nums)):
            if nums[i]>h_v:
                h=i
                h_v=nums[i]
            if nums[i]<l_v:
                l=i
                l_v=nums[i]
        print(l,h)
        ans=mx = max(l+1,h+1)
        mi = min(l,h)
        an = len(nums)-mi
        a =(mi+1)+(len(nums)-mx+1)

        print(a,an,ans)

        return min(an,a,ans)