class Solution(object):
    def findClosest(self, x, y, z):
        if abs(x-z) > abs(y-z):
            return 2
        elif abs(x-z) < abs(y-z):
            return 1
        else:
            return 0
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        
