class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        freq = Counter(nums)
        print(freq)
        nums.sort()
        ans = []
        for k in range(len(nums)):
            if k>0 and nums[k] == nums[k-1]: continue

            i=k+1
            j=len(nums)-1
            while i<j:
                t = nums[k]+nums[i]+nums[j]
                if t<0:
                    i+=1
                elif t>0: j-=1
                else:
                    ans.append([nums[k],nums[i],nums[j]])
                    i+=1
                    j-=1
                    while i<j and nums[i]==nums[i-1]:i+=1
                    while i<j and nums[j] == nums[j+1]:j-=1
        return ans


        