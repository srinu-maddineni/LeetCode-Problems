class Solution(object):
    def minLengthAfterRemovals(self, s):
        """
        :type s: str
        :rtype: int
        """
        stk = []
        for i in range(len(s)):
            if s[i] =='a' and (len(stk)>0 and stk[-1] == 'b'):
                stk.pop()
            elif s[i] == 'b' and (len(stk)>0 and stk[-1] == 'a'):
                stk.pop()
            else:
                stk.append(s[i])
        return len(stk)
        