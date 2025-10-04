class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) ==2:
            return min(height[0],height[1])
        if not height: return
        i=0
        j=len(height)-1
        w = 0
        while i<j:
            # print(((j-i)*min(height[i],height[j])))
            k = ((j-i)*min(height[i],height[j]))
            if w < k :
                w = k

            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return w


