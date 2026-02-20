class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        rel = []
        c = 0
        st =0
        for i , val in enumerate(s):
            if val == '1':
                c+=1
            else:
                c-=1
            
            if c==0:
                inner = self.makeLargestSpecial(s[st+1:i])
                rel.append('1'+inner+'0')
                st=i+1
        rel.sort(reverse=True)
        return ''.join(rel)
