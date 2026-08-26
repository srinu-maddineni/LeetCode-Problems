class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        dumy = x
        r = 0
        if x<0 or (x%10 ==0 and x!=0): return False
        while x>0:
            # print(r)
            n = x%10
            print(n)
            r = r*10 + n
            x = x//10
        print(r)
        return r == dumy 