class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # count =0
        # if x <0:
        #     return False
       
        # x_str = str(x)
        # l = 0
        # r = len(x_str)-1
        
        # while l < r:
        #     if x_str[l] != x_str[r]:
        #         return False
        #     l+=1
        #     r-=1
        # return True
        # if x<0 or (x%10 ==0 and x!=0):
        #     return False
        # reverse = 0
        # while x > reverse:
        #     reverse = reverse*10 + x % 10
        #     x= x//10
        # return x == reverse or x == reverse//10

        # x = str(x)
        # y = x[::-1]
        # return x == y  

        if str(x)[::-1] == str(x):
            return True
        else:
            return False
        

        
