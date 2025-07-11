class Solution(object):
    def maximum69Number (self, num):
        max1 = num
        num = str(num)
        n = str(num)
        
        for i in range(len(num)):
            num_list = list(num)
            if num_list[i]=='6':
                num_list[i] = '9'
                num = ''.join(num_list)
                if max1 <= int(num):
                    max1 = int(num)
                    print(max1)
            else:
                num_list[i] = '6'
                print(num_list)
                num = ''.join(num_list)
                if max1 <= int(num):
                    max1 = int(num) 
                    print(max1)
                    
            # print(num)
            num = n
            
        return int(max1)
        """
        :type num: int
        :rtype: int
        """
        
