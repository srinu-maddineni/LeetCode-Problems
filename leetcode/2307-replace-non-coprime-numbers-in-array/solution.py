class Solution(object):
    def replaceNonCoprimes(self, nums):
        def gcd(a,b):
            while b !=0:
                a,b = b,a%b
            return a
        def lcm(a,b):
            return (a*b)//gcd(a,b)
        stk = []
        for i in nums:
            stk.append(i)
            while len(stk)>1:

                g = gcd(stk[-1],stk[-2])
                if g >1:
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(lcm(a,b))
                else: break
        return stk
              

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
