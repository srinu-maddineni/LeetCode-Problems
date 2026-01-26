class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        k = []
        for i in range(2*len(nums)):
            if i >= len(nums):
                k.append(nums[i-len(nums)])
            else:
                k.append(nums[i])

        return k
        
