class Solution(object):
    def addBinary(self, a, b):
        n = int(a,2)+int(b,2)
        return format(n,'b')
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
