class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        rel = 0
        for i in range(len(nums)):
            s = set()
            od = 0
            ev = 0
            for j in range(i,len(nums)):
                x = nums[j]
                if x not in s:
                    s.add(x)
                    if x !=0:
                        if x %2 ==0:
                            ev+=1

                        else:
                            od+=1
                if od == ev:
                    rel = max(rel,j-i+1)
        return rel

