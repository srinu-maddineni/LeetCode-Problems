class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         d = abs(nums[i]-nums[j])
        #         if d<=limit and nums[j]<nums[i]:
        #             [nums[i],nums[j]] = [nums[j],nums[i]]
        # return nums

        arr = sorted((nums[i], i) for i in range(len(nums)))

        print(arr)
        n = len(nums)
        i = 0
        while i<n:
            j=i
            while j+1<n and arr[j+1][0]-arr[j][0]<=limit:
                j+=1
            val = []
            index = []
            for k in range(i,j+1):
                val.append(arr[k][0])
            index = sorted(arr[k][1] for k in range(i,j+1))
            
            for k in range(len(index)):
                nums[index[k]] = val[k]
            i=j+1
        return nums
