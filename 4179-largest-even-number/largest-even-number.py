class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        # r = []
        n = int(s)
        # while n>
        # print(r)
        for i in range(len(s)-1,-1,-1):
            k = n%10
            if k == 1:
                n/=10
            else:
                return str(n)
        return ''
