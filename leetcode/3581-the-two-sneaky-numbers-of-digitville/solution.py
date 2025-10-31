class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        l = []*2
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                l.append(i)
        return l
        
