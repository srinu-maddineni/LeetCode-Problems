class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        s = set(sentence)
        # n = 0
        # for i in range(len(sentence)):
        #     if sentence[i] not in s:
        #         n+=1
        # print(n)
        return len(s) ==26
        