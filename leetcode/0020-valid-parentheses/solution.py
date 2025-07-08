class Solution(object):
    def isValid(self, s):
        if len(s) ==0:
            return False
        c= {
            ")":"(",
            "}":"{",
            "]":"["
        }
        a = []
        for i in s:
            if i in c:
                if len(a) == 0:
                    return False
                else:
                   
                    if c[i] != a[-1]:
                        return False
                    else:
                        a.pop()
            else:
                a.append(i)

        if a:
            return False
        else:
            return True





        """
        :type s: str
        :rtype: bool
        """
        
