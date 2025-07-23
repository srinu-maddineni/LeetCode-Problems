class Solution(object):
    def climbStairs(self, n):
        if n == 1 or n == 2:
            return n
        one_step = 2
        two_step = 1
        for i in range(2,n):
            new = two_step+one_step
            two_step = one_step
            one_step = new
        
        return one_step
        """
        :type n: int
        :rtype: int
        """
        
