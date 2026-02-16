class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        rel = []
        sol = []
        ar = [1,2,3,4,5,6,7,8,9]
        def back(i,arr):
            if len(rel) == k and sum(rel) == n:
                sol.append(rel[:])
            for j in range(i,len(ar)):
                rel.append(ar[j])
                back(j+1,rel)
                rel.pop()
        back(0,[])
        return sol
        
