class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def help(n,s):
            if n<10:
                print(n,s)
                return s+n
            s+=n%10
            n//=10
            return help(n,s)
        for i in range(len(nums)):
            k = help(nums[i],0)
            print(k)
            if i == k:
                return i
        return -1
        