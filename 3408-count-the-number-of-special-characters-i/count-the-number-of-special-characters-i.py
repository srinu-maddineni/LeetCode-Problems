class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        arr = [0]*52
        print(ord('A'))

        for i in range(len(word)):
            if word[i].isupper():
                arr[ord(word[i])-39]+=1
            else:
                arr[ord(word[i])-97] +=1
        res= 0

        for i in range(26):
            if(arr[i] >0 and arr[i+26]>0):
                res+=1
        return res

        