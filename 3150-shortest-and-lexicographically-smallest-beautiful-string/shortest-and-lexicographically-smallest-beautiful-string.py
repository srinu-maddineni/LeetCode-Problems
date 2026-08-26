class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        # i=0
        # j=0
        # r = s
        # while j<len(s):
        #     if num_of_ones > k:
        #         if s[i] == '1':
        #             num_of_ones-=1
        #         i+=1
        #         continue
        #     print(num_of_ones)
        #     if num_of_ones == k:
        #         print(s[i:j])
        #         if len(r) > len(s[i:j]):
        #             r = s[i:j]

        #     if s[i] =='1':
        #         num_of_ones+=1
        #     j+=1
        # return r
        r = ''
        for i in range(len(s)):
            num_of_ones = 0
            for j in range(i,len(s)):
                if s[j] == '1':
                    num_of_ones +=1
                if num_of_ones == k:
                    if r =='' or len(r)>len(s[i:j+1]) or (len(r) == len(s[i:j+1]) and r > s[i:j+1]):
                        r = s[i:j+1]
                    break
        return r
        