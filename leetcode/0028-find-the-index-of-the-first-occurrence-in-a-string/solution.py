class Solution(object):
    def strStr(self, haystack, needle):
        m = len(haystack)
        n = len(needle)

       
        for i in range(m):
            k = 0
            for j in range(i,m):
               

                if haystack[j] == needle[k]:
                    k+=1
                else:
                    break


                if k == n:
                    return i
        return -1

            
        
        return -1



        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
