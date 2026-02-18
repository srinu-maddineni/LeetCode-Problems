class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rel = []
        sol = []
        def back(i):
            sol.append(rel[:])
            for j in range(i,len(nums)):
                if j>i and nums[j] == nums[j-1]:
                    continue
                rel.append(nums[j])
                back(j+1)
                rel.pop()
        back(0)
        print(rel)
        return sol

        
