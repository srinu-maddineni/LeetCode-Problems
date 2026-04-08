class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for q in queries:
            l = q[0]
            r = q[1]
            k = q[2]
            v = q[3]
            for i in range(l,r+1,k):
                nums[i] = (nums[i]*v)%((10**9)+7)
        print(nums)
        result = nums[0]
        for i in range(1,len(nums)):
            result^=nums[i]
        return result
        
