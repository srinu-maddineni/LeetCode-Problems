class Solution(object):
    def numberOfBeams(self, bank):
        # n,m = len(bank),len(bank[0])

        # laser=0
        # r = []
        # for i in range(n):
        #     if '1' not in bank[i]:
        #         continue
        #     k=0
        #     for j in range(m):
        #         if bank[i][j] == '1':
        #             k+=1
        #     r.append(k)
        # print(r)
        # if len(r) == 1:
        #     return 0
        # for i in range(1,len(r)):
        #     laser += r[i-1]*r[i]
        # return laser
        prev = 0
        laser = 0
        for i in bank:
            curr = i.count('1')
            if curr>0:
                laser+=curr*prev
                prev = curr
        return laser
                

        
            

            




        """
        :type bank: List[str]
        :rtype: int
        """
        
