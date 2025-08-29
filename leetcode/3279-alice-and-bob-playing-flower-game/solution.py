class Solution(object):
    def flowerGame(self, n, m):
        # if n == 1 and m == 1:
        #     return 0
        # m = n+m
        # c = 0
        # for i in range(1,n+1):
        #     for j in range(1,m+1):
        #         # print(i,j)
        #         if (i + j)%2 != 0:
        #             c +=1
        # return c 
        a_odd = (n+1)//2
        a_even = n//2
        b_odd = (m+1)//2
        b_even = m//2
        return a_odd * b_even + a_even * b_odd

        """
        :type n: int
        :type m: int
        :rtype: int
        """
        
