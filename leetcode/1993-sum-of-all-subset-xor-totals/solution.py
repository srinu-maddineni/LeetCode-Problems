class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        rel = []
        sol = []
        def back(i,nums):
            sol.append(rel[:])
            for j in range(i,len(nums)):
                rel.append(nums[j])
                back(j+1,nums)
                rel.pop()
        back(0,nums)
        ans = 0
        for i in sol:
            a = 0
            for j in range(len(i)):
                a^=i[j]
            ans+=a
        return ans      
