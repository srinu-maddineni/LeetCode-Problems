class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        # def help(n,s):
        #     if n<10:
        #         print(n,s)
        #         return s+n
        #     s+=n%10
        #     n//=10
        #     return help(n,s)
        for i in range(len(nums)):
            s = 0
            k = nums[i]
            while k>=10:
                s+=k%10
                k//=10
            print(k,s)
            if i == k+s:
                return i
        return -1
        