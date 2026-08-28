class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = 0 
        m = {0:-1}
        # for i in range(len(nums)):
        #     m = [0,0]
        #     for j in range(i,len(nums)):
        #         if nums[j] == 0:
        #             m[0]+=1
        #         else: m[1]+=1

        #         if m[0] ==m[1]:
        #             mx = max(mx,m[0]+m[1])
        # return mx
        s = 0
        for i in range(len(nums)):
            if nums[i] ==0: s-=1
            else: s+=1
            print(s)
            if s in m:
                mx = max(mx,i-m[s])
            else:
                m[s]=i
        return mx
            