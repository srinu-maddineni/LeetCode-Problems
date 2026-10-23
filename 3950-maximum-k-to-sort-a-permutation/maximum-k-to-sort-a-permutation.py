class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # if nums == nums.sort():
        #     return 0
        # for i in range(len(nums))
        ans = float('inf')
        # ans = 1
        k = 0
        for i in range(len(nums)):
            if i != nums[i]:
                if ans == float('inf'):
                    ans = nums[i]
                k+=1
                ans = ans & nums[i]
        if k ==0:
            return 0
        return ans