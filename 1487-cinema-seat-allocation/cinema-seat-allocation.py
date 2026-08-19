class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        m={}
        for i,j in reservedSeats:
            if i not in m:
                m[i] = set()
            m[i].add(j)
        print(m)
        
        count =2 * (n - len(m))
        for i in m.values():
            k = 0
            c = 0

            for x in [2, 3, 4, 5]:
                if x in i:
                    k += 1
                    break

            if k == 0:
                c += 1

            k = 0

            for x in [6, 7, 8, 9]:
                if x in i:
                    k += 1
                    break

            if k == 0:
                c += 1

            if c == 0:
                k = 0

                for x in [4, 5, 6, 7]:
                    if x in i:
                        k += 1
                        break

                if k==0: c+=1
            if c == 1:
                count += 1
            elif c==2:
                count+=2
        return count

                
