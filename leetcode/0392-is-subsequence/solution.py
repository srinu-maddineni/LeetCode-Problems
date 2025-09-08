class Solution(object):
    def isSubsequence(self, s, t):
        if s == "": return True
        
        S = len(s)
        T = len(t)
        if S>T: return False
        j = 0 
        for i in range(T) :
            if s[j] == t[i]:
                if S-1 == j:
                    return True
                j+=1
        return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
