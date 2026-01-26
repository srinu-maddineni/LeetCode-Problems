class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        a_sum = 0
        dub = 0
        for i in nums:
            a_sum +=i
            if i in seen:
                dub = i
            seen.add(i)
        n = len(nums)
        exp = (n*(n+1)) //2
        mis = exp - (a_sum - dub)
        return [dub,mis]

            
        
