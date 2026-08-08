class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        return abs(int(s[::-1]) -n )
