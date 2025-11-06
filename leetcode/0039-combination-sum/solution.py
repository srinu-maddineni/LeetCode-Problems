class Solution(object):
    def combinationSum(self, candidates, target):
        rel = []
        sol = []
        def back(i):
            if sum(sol) == target:
                rel.append(sol[:])
                return
            if i == len(candidates) or sum(sol) > target:
                return
            back(i+1)
            sol.append(candidates[i])
            back(i)
            sol.pop()
        back(0)
        return rel
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
