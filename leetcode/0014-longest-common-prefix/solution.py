class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str_1 = ""
        for i in range(len(strs)-1):

            str_2 = strs[i]
            str_3 = strs[i+1]
            if len(str_2) > len(str_3):
                num =len(str_3)
                for j in range(num):
                    if str_2[j] == str_3[j]:
                        
                        str_1 = str_1+str_3[j]
                    else:
                        break
            
            else:
                num = len(str_2)
                for j in range(num):
                    if str_2[j] == str_3[j]:
                        str_1 = str_1+str_2[j]
                    else:
                        break
            strs[i+1] = str_1
            str_1=""
            print(strs[i+1])
          
        return strs[-1]

        
