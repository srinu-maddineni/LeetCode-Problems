class Solution(object):
    def convert(self, s, numRows):
        if numRows <= 1:
            return s
        h = ['']*numRows
        j = 0
        i =0
        d = 1
        while j<len(s):
            while d == 1 and j<len(s):
                h[i]+=s[j]
                i+=1
                j+=1
                if i == numRows-1:
                    d = 0

            while d == 0 and j<len(s):
                h[i]+=s[j]
                j+=1
                i-=1
                if i == 0:
                    d = 1
        result = ''
        for i in range(numRows):
            result+=h[i]
        return result

            


        # print(ord('A'),ord('Z'))


        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
