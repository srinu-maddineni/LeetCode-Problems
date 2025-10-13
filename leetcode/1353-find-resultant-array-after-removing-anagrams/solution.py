class Solution(object):
    def removeAnagrams(self, words):
        def anagram(m,n):
            m=m.replace(" ","").lower()
            n = n.replace(" ","").lower()
            return sorted(m) == sorted(n)
        result = [words[0]]
        for i in range(len(words)):
            
            if not anagram(words[i],result[-1]):
                result.append(words[i])
                

        return result

        """
        :type words: List[str]
        :rtype: List[str]
        """
        
