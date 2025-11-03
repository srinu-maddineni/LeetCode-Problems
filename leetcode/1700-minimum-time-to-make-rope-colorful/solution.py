class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        count =0
        max_time = neededTime[0]
        for i in range(1,n):
            if colors[i] == colors[i-1]:
                count+= min(max_time,neededTime[i])
                max_time = max(max_time,neededTime[i])
            else:
                max_time = neededTime[i]

        return count
        # max_sum = 0
        # for i in range(n-1):
        #     j =i
        #     k=neededTime[i]
        #     while colors[i] == colors[i+1] and j < n:
        #         if neededTime[j] < neededTime[j+1]:
        #             k = neededTime[j+1]
        #         j+=1
        #     max_sum+=k
        # needTime = sum(neededTime)
        # print(needTime)
        






        
