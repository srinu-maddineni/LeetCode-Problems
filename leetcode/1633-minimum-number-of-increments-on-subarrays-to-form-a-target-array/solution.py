class Solution(object):
    def minNumberOperations(self, target):
        # n = len(target)
        c = 0
        prev = 0
        for t in target:
            if t > prev:
                c += (t - prev)
            prev = t
        return c

        # nums = [0]*n
        # c = 0
        # print(nums)
        # i = 0 
        # while nums != target:
        #     i = 0
        #     j=0
        #     for i in range(n):

        #         while i<n:
        #             if nums[i]<target[i]:
        #                 j+=1
        #                 print(j)
        #                 i+=1

        #             else:
        #                 break
        #         k = i
        #         while k<j:
        #             nums[k] = nums[k]+1

        #             k+=1
        #         c+=1
        # return c




        """
        :type target: List[int]
        :rtype: int
        """
        
