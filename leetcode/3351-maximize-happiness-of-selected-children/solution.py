class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        c = 0
        sol = 0
        for i in range(k):
            r = happiness[-1]
            if r - c < 0:
                sol+=0
            else:
                sol+= r-c
            happiness.pop()
            c+=1
        return sol
        
