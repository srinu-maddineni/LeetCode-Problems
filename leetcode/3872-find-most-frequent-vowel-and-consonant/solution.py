class Solution(object):
    def maxFreqSum(self, s):
        v = {}
        c = {}
        r = 'aeiou'
        for i in s:
            if i in r:
                if i in v:
                    v[i]+=1
                else:
                    v[i] = 1
            else:
                if i in c:
                    c[i] +=1
                else:
                    c[i] = 1
        v_max = 0
        c_max = 0
        if v:
            v_max = max(v.values())
        if c:
            c_max = max(c.values())

        return v_max+c_max
        """
        :type s: str
        :rtype: int
        """
        
