class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        sol = [pref[0]]
    
        for i in range(1,len(pref)):
            k = pref[i]^pref[i-1]
            sol.append(k)
        print(sol)
        return sol
        
