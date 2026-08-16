class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        # s =0 
        # a =True
        # for i in range(len(stones)):
        #     r = s 
        #     for j in range(len(stones)):
        #         if (r+stones[j]) % 3 != 0:
        #             r +=stones[j]
        #             del stones[j]
        #             a = not a
        #             break
        #     if r ==s:
        #         if a: return False
        #         else : return True
        #     s= r    
        #     if len(stones) ==1 :
        #         s +=stones[0]
        #         a=not a
        #         break
        # print(s)
        # if (s % 3) == 0 and  a:
        #     return True
        # else:
        #     return False

        s0,s1,s2 = 0,0,0
        for i in stones:
            r = i%3
            if r ==0: s0+=1
            elif r == 1: s1+=1
            else: s2+=1
        if s0%2 ==0: return s1>=1 and s2>=1
        else: return abs(s1-s2)>2 