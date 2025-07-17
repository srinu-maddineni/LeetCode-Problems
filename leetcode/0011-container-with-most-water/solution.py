class Solution(object):
    def maxArea(self, height):
        print(height)
        j = len(height)-1
        i = 0
        m = 0
        c = 0
        if j+1 == 2:
            return min(height[i] , height[j])
        while i!=j:
            c =min( height[i],height[j]) *(j-i)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
            
            m = max(m,c)
        return m




        """
        :type height: List[int]
        :rtype: int
        """
        
