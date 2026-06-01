class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return cost[0]+cost[1]
        cost.sort(reverse = True)
        print(cost)
        n =0
        for i in range(len(cost)):
            if (i+1)%3 ==0:
                continue
            else:
                n+=cost[i]
        return n

        
