class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        ans =0 
        mx = weight[0]
        for i in range(1,len(weight)+1):
            if weight[i-1]>mx:
                mx = weight[i-1]

            if weight[i-1]<mx:
                ans+=1
                if i >=len(weight):
                    break
                else:
                    mx = weight[i]
            print(weight[i-1],mx)
        return ans
            