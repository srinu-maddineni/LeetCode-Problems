class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        i = 0
        mod = (10**9) + 7

        for ch in s:
            if ch == "1":
                i+=1
                count+=i
            else:
                i = 0


        # while i<len(s):
            # if s[i] == "1":
            #     k =0
            #     j = i
            #     while j < len(s) and s[j] == "1":
                    
            #         k+=1
            #         j+=1
            #     i = j
            #     count += (((k+1)*k)//2)%mod
            # else:
            #     i+=1    
        return count%mod
        
