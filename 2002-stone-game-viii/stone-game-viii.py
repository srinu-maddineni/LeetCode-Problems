class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        arr = []
        s =0
        for i in range(len(stones)):
            s+=stones[i]
            arr.append(s)

        max_diff = arr[-1]
        for i in range(len(arr)-2,0,-1):
            max_diff = max(max_diff,arr[i]-max_diff)
        return max_diff