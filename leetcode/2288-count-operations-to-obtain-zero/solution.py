class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 == 0:
            return 0
        count = 0
        while num1 !=0 and num2 !=0:
            if num1>num2:
                count+=1
                num1 = num1-num2
            else:
                count+=1
                num2 = num2-num1
        # def con(n1,n2):
        #     nonlocal count
        #     if n1 == n2:
        #         return count
        #     elif n1>n2:
        #         count+=1
        #         con(n1-n2,n2)
        #     else:
        #         count+=1
        #         con(n1,n2-n1)
        # con(num1,num2)
        return count

            
        
