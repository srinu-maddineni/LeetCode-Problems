class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # use = [False]*len(nums)
        # print(use)
        # res = []
        # def back(path):
        #     if len(path) == len(nums):
        #         res.append(path[:])
        #         return
        #     for i in range(len(nums)):
        #         if use[i]:
        #             continue

        #         use[i] = True
        #         path.append(nums[i])
        #         back(path)
        #         path.pop()
        #         use[i] = False
        # back([])
        # print(res)
        # for i in range(len(res)):
        #     if i<len(res)-1 and nums == res[i]:
        #         nums[:] = res[i+1]
        #         return
        # nums[:] = res[0]
        # return


        index = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                index = i
                break
        print(index)
        if index == -1:
            nums.reverse()
            return
        
        else:
            j = -1
            for i in range(len(nums)-1,index,-1):
                if nums[index]<nums[i]:
                    [nums[i],nums[index]] = [nums[index],nums[i]]
                    j = i
                    break
            print(j)
            nums[index+1:] = nums[index+1:][::-1]
        

