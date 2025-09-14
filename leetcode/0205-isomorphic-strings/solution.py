class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t): return False
        h ={

        }
        k = {}
        for i , j in zip(s,t):
            if i in h and h[i] != j: return False
            if j in k and k[j] != i: return False
            h[i] =j
            k[j] =i
        return True
            
            
        c =0
        r =0
        for i in s:
            if h[i] == t[r]:
                c+=1
                r+=1
        if c == len(s): return True
        else : return False



        print(h)
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
